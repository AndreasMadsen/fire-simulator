
import numpy as np

cc = {
	"tree" : np.asarray([125, 191, 128, 255]),
	"road" : np.asarray([236, 184, 70, 255]),
	"water": np.asarray([70, 124, 182, 255]),
	"fire" : np.asarray([243, 84, 83, 255])
}

def initial_fire(picture):
	return [200, 200]
