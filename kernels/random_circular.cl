
#include "shared.h"

kernel void run(global const uchar4 *curr, global uchar4 *next, int rows, int cols, global const float *rands) {
	int row = get_global_id(0);
	int col = get_global_id(1);

	int ci = row * cols + col;

	int vi = (row + 0) * cols + (col - 1);
	int ni = (row - 1) * cols + (col + 0);
	int ei = (row + 0) * cols + (col + 1);
	int si = (row + 1) * cols + (col + 0);

	int nvi = (row - 1) * cols + (col - 1);
	int nei = (row - 1) * cols + (col + 1);
	int svi = (row + 1) * cols + (col - 1);
	int sei = (row + 1) * cols + (col + 1);

	if (row > 0 && row < (rows - 1) && col > 0 && col < (cols - 1)) {
		if (curr[ ci ].x == tree.x) {
			float n = (float)(curr[ ni ].x == fire.x);
			float e = (float)(curr[ ei ].x == fire.x);
			float s = (float)(curr[ si ].x == fire.x);
			float v = (float)(curr[ vi ].x == fire.x);

			float nv = (float)(curr[ nvi ].x == fire.x);
			float ne = (float)(curr[ nei ].x == fire.x);
			float sv = (float)(curr[ svi ].x == fire.x);
			float se = (float)(curr[ sei ].x == fire.x);

			float prop = 0.5f * (n + e + s + v) + 0.1019671561f * (nv + ne + sv + se);

			if (prop >= rands[ci]) {
				next[ci] = fire;
			}
		}
	}
}
