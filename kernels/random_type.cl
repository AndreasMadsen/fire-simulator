
#include "shared.h"

inline float isfire(global const uchar4 *curr, int cols, char r, char c) {
	int row = get_global_id(0);
	int col = get_global_id(1);
	int index = (row + r) * cols + (col + c);

	return (float)(curr[ index ].x == fire.x);
}

inline float typefactor(const uchar4 cell) {
	if (cell.x == tree1.x) {
		return 1.0f;
	} else if (cell.x == tree2.x) {
		return 0.5f;
	} else {
		return -0.1f; // random numbers are [0, 1[ so 0.0 is actually possible
	}
}

kernel void run(global const uchar4 *curr, global uchar4 *next, int rows, int cols, global const float *rands) {
	int row = get_global_id(0);
	int col = get_global_id(1);

	int ci = row * cols + col;

	if (row > 0 && row < (rows - 1) && col > 0 && col < (cols - 1)) {
		float t = typefactor(curr[ci]);

		float n = isfire(curr, cols, -1, +0);
		float e = isfire(curr, cols, +0, +1);
		float s = isfire(curr, cols, +1, +0);
		float v = isfire(curr, cols, +0, -1);

		float nv = isfire(curr, cols, -1, -1);
		float ne = isfire(curr, cols, -1, +1);
		float sv = isfire(curr, cols, +1, -1);
		float se = isfire(curr, cols, +1, +1);

		float prop = t * (0.5f * (n + e + s + v) + 0.1019671561f * (nv + ne + sv + se));

		if (prop >= rands[ci]) {
			next[ci] = fire;
		}
	}
}
