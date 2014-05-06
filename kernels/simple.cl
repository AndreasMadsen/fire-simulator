
#include "shared.h"

kernel void run(global const uchar4 *curr, global uchar4 *next, int rows, int cols, global const half *rands) {
	int row = get_global_id(0);
	int col = get_global_id(1);

	int this = row * cols + col;
	int left = row * cols + (col - 1);
	int top = (row - 1) * cols + col;
	int right = row * cols + (col + 1);
	int bottom = (row + 1) * cols + col;

	if (row > 0 && row < (rows - 1) && col > 0 && col < (cols - 1)) {
		if (curr[ this ].x == fire.x) {
			if (curr[ left ].x == tree.x) { next[ left ] = fire; }
			if (curr[ top ].x == tree.x) { next[ top ] = fire; }
			if (curr[ right ].x == tree.x) { next[ right ] = fire; }
			if (curr[ bottom ].x == tree.x) { next[ bottom ] = fire; }
		}
	}
}
