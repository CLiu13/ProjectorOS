m = {{0, 300, 1, 0, 0, 0, 0, -45000}, {400, 300, 1, 0, 0, 
   0, -100000, -75000}, {0, 0, 1, 0, 0, 0, 0, 0}, {400, 0, 1, 0, 0, 
   0, -160000, 0}, {0, 0, 0, 0, 300, 1, 0, -90000}, {0, 0, 0, 400, 
   300, 1, -120000, -90000}, {0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 400, 
   0, 1, 0, 0}}
n = {{a0}, {a1}, {a2}, {b0}, {b1}, {b2}, {c0}, {c1}}

m.n == {{150}, {250}, {0}, {400}, {300}, {300}, {0}, {0}}
Solve[%, {a0, a1, a2, b0, b1, b2, c0, c1}]