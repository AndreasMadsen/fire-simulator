
#include "shared.h"

kernel void run(global const uchar4 *curr, global uchar4 *next, int rows, int cols) {
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
			int a = curr[ n ].w  + curr[ e ].w  + curr[ s ].w  + curr[ v ].w ;
			int b = curr[ nv ].w + curr[ ne ].w + curr[ se ].w + curr[ sv ].w;

			int fireratio = curr[c].w + a + 211 * b;
				fireratio = min(255, fireratio);
			next[ c ].w = fireratio;

			if (fireratio == 255) {
				next[c] = fire;
			}
		}
	}
}
