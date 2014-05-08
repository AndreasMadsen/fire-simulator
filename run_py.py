
import parameters as params

import numpy as np
import scipy.misc
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load forest picture and enforce alpha layer and uint8 as datatype
forest = scipy.misc.imread('picture/forest.png')
if (forest.shape[2] != 4):
	forest = np.dstack((forest, np.ones(forest.shape[0:2]) * 255))
forest = forest.astype('uint8')

# Get and set forest fire position
start = params.initial_fire(forest)
forest[start[0], start[1], :] = params.cc["fire"]

# Iterate forest fire
def iter_forest_fire(picture):
	fire = picture[:,:,0] == params.cc["fire"][0]
	trees = picture[:,:,0] == params.cc["tree"][0]

	for row in range(1, picture.shape[0] - 1):
		for col in range(1, picture.shape[1] - 1):
			if (fire[row, col]):

				if (trees[row - 1, col]):
					picture[row - 1, col, :] = params.cc["fire"]
				if (trees[row + 1, col]):
					picture[row + 1, col, :] = params.cc["fire"]
				if (trees[row, col - 1]):
					picture[row, col - 1, :] = params.cc["fire"]
				if (trees[row, col + 1]):
					picture[row, col + 1, :] = params.cc["fire"]

	return picture

fig = plt.figure()
im = plt.imshow(np.zeros(forest.shape), interpolation='nearest')

# initialization function: plot the background of each frame
def init():
	global forest
	im.set_data(forest)
	return [im]

# animation function.  This is called sequentially
def animate(i):
	global forest
	forest = iter_forest_fire(forest)
	im.set_data(forest)
	return [im]

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=20, interval=20, blit=True, repeat=False)
plt.show()
