m = {{3, 5, 1, 0, 0, 0, 0, 0}, {5, 5, 1, 0, 0, 0, -15, -15}, {2, 2, 1,
    0, 0, 0, 0, 0}, {6, 1, 1, 0, 0, 0, -18, -3}, {0, 0, 0, 3, 5, 
   1, -9, -15}, {0, 0, 0, 5, 5, 1, -15, -15}, {0, 0, 0, 2, 2, 1, 0, 
   0}, {0, 0, 0, 6, 1, 1, 0, 0}}
n = {{a0}, {a1}, {a2}, {b0}, {b1}, {b2}, {c0}, {c1}}

m.n == {{0}, {3}, {0}, {3}, {3}, {3}, {0}, {0}}
Solve[%, {a0, a1, a2, b0, b1, b2, c0, c1}]