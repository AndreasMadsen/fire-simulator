
import parameters as params
from simulator import Simulator

import numpy as np
import scipy.misc
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Pictures --- CONFIGUREATION HERE ---
picture = 'forest2'
name = 'real_both-B'
kernel = 'random_wind_type'
pictures_at = [10, 50, 100, 200, 300, 400, 500, 600]
size = (8, 5)
start = [100, 550]

# Load forest picture
forest = np.load('picture/%s.npy' % (picture))

# Get and set forest fire position
forest[start[0], start[1], :] = params.cc["fire"]

# Initalize math model
model = Simulator(kernel, forest)

for i in range(1, np.max(pictures_at) + 1):
	model.iterate()

	if (i in pictures_at):
		fig = plt.figure(figsize=size)
		plt.imshow(model.picture[:, :, 0:3], interpolation='nearest')
		fig.savefig('figures/%s-%d.pdf' % (name, i))
