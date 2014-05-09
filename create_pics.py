import os
import os.path as path

import numpy as np
import scipy.misc

for name in os.listdir('picture'):
	filepath = path.join('picture', name)
	if (path.isfile(filepath) and path.splitext(filepath)[1] == '.png'):
		picture = scipy.misc.imread(filepath)
		np.save(path.join(path.splitext(filepath)[0] + '.npy'), picture)
