
import parameters as params
from simulator import Simulator
import os.path as path

import numpy as np
import scipy.misc
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation

thisdir = path.dirname(path.realpath(__file__))

# Load forest picture and enforce alpha layer and uint8 as datatype
#forest = scipy.misc.imread('forest.png')
forest = np.dstack((
	np.ones((400, 400)) * params.cc["tree"][0],
	np.ones((400, 400)) * params.cc["tree"][1],
	np.ones((400, 400)) * params.cc["tree"][2],
	np.ones((400, 400)) * 255
))
forest = forest.astype('uint8')

# Get and set forest fire position
start = params.initial_fire(forest)
forest[start[0], start[1], :] = params.cc["fire"]

# Initalize math model
model = Simulator("random_wind", forest)

fig = plt.figure()
im = plt.imshow(model.picture[:, :, 0:3], interpolation='nearest')

# initialization function: plot the background of each frame
def init():
	im.set_data(model.picture[:, :, 0:3])
	return [im]

# animation function.  This is called sequentially
def animate(i):
	model.iterate()
	forest = np.array(model.picture[:, :, 0:3], copy=True)
	im.set_data(forest)
	return [im]

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True, repeat=False)
#anim.save('basic_animation_2.mp4', writer=animation.writers['ffmpeg'](fps=30), dpi=100)

plt.show()
