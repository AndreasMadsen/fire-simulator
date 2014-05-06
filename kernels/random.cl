
#include "shared.h"

kernel void run(global const uchar4 *curr, global uchar4 *next, int rows, int cols, global const float *rands) {
	int row = get_global_id(0);
	int col = get_global_id(1);

	int c = row * cols + col;

	int v = (row + 0) * cols + (col - 1);
	int n = (row - 1) * cols + (col + 0);
	int e = (row + 0) * cols + (col + 1);
	int s = (row + 1) * cols + (col + 0);

	int nv = (row - 1) * cols + (col - 1);
	int ne = (row - 1) * cols + (col + 1);
	int sv = (row + 1) * cols + (col - 1);
	int se = (row + 1) * cols + (col + 1);

	if (row > 0 && row < (rows - 1) && col > 0 && col < (cols - 1)) {
		if (curr[ c ].x == tree.x) {
			float prop = 0.0f;
			if (curr[ n ].x == fire.x) { prop += 0.1f; }
			if (curr[ e ].x == fire.x) { prop += 0.1f; }
			if (curr[ s ].x == fire.x) { prop += 0.1f; }
			if (curr[ v ].x == fire.x) { prop += 0.8f; }

			if (curr[ nv ].x == fire.x) { prop += 0.1f; }
			if (curr[ ne ].x == fire.x) { prop += 0.1f; }
			if (curr[ sv ].x == fire.x) { prop += 0.1f; }
			if (curr[ se ].x == fire.x) { prop += 0.1f; }

			if (prop >= rands[c]) {
				next[c] = fire;
			}
		}
	}
}
