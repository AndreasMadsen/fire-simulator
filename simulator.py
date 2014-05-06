
import numpy as np
import pyopencl as cl
import os.path as path

thisdir = path.dirname(path.realpath(__file__))
kerneldir = path.join(thisdir, 'kernels')

def read_kernel(name):
	fullpath = path.join(kerneldir, name + '.cl')
	with open (fullpath, "rb") as myfile:
		return myfile.read()

def save_device_fetch(type):
	devices = []
	for platform in cl.get_platforms():
		devices = devices + platform.get_devices(device_type=cl.device_type.GPU)

	# Just use the first GPU device, they are all good
	return [devices[0]]

class Simulator:
	def __init__(self, name, init_picture):
		# Setup context and queue
		self._ctx = cl.Context(devices=save_device_fetch(cl.device_type.GPU))
		self._queue = cl.CommandQueue(self._ctx)

		# Read source code and compile
		self._program = cl.Program(self._ctx, read_kernel(name)).build('-I ' + kerneldir.replace(" ", "\ "))

		# Dublicate initial picture using C ordered memory
		self._size = init_picture.shape[0:2]
		self.picture = np.copy(init_picture, order='C').astype('uint8')

		# Setup openCL buffers
		self._curr_buffer = cl.Buffer(self._ctx, cl.mem_flags.READ_WRITE, size=self.picture.nbytes)
		self._next_buffer = cl.Buffer(self._ctx, cl.mem_flags.READ_WRITE, size=self.picture.nbytes)

		# Setup random numbers
		rands = np.random.random(self._size).astype('float32')
		self._random_buffer = cl.Buffer(self._ctx, cl.mem_flags.READ_ONLY, size=rands.nbytes)
		cl.enqueue_copy(self._queue, self._random_buffer, rands)

		# Copy current picture to host memory
		cl.enqueue_copy(self._queue, self._curr_buffer, self.picture)
		# Sync also wth the next buffer, so pixels aren't required to be copied in kernel
		cl.enqueue_copy(self._queue, self._next_buffer, self._curr_buffer)
		# Sync queue
		self._queue.finish()

	def iterate(self):
		args = (
			self._curr_buffer,
			self._next_buffer,
			np.asarray(self._size[0], dtype='int32'),
			np.asarray(self._size[1], dtype='int32'),
			self._random_buffer
		)

		# Run main function, using curr_picture.shape as the problem size
		self._program.run(self._queue, self._size, None, *args)

		# Copy next buffer (new current) intro the picture array
		cl.enqueue_copy(self._queue, self.picture, self._next_buffer)
		# and sync with current buffer, to prepear for next iteration
		cl.enqueue_copy(self._queue, self._curr_buffer, self._next_buffer)

		# Update random numbers
		cl.enqueue_copy(self._queue, self._random_buffer, np.random.random(self._size).astype('float32'))

		# Sync queue
		self._queue.finish()

		# The next buffer contains the current buffer, so swap them
		swap = self._curr_buffer
		self._curr_buffer = self._next_buffer
		self._next_buffer = swap

		# At this point the current buffer, contain the newest picture with can be
		# read from self.picture.
