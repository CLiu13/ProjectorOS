x0=0
y0=0
x1=400
y1=0
x2=0
y2=300
x3=400
y3=300

u0=0
v0=0
u1=400
v1=0
u2=100
v2=300
u3=300
v3=300

denom0=g*x0+h*y0+1
denom1=g*x1+h*y1+1
denom2=g*x2+h*y2+1
denom3=g*x3+h*y3+1

eu0=u0==(a*x0+b*y0+c)/denom0
ev0=v0==(d*x0+e*y0+f)/denom0
eu1=u1==(a*x1+b*y1+c)/denom1
ev1=v1==(d*x1+e*y1+f)/denom1
eu2=u2==(a*x2+b*y2+c)/denom2
ev2=v2==(d*x2+e*y2+f)/denom2
eu3=u3==(a*x3+b*y3+c)/denom3
ev3=v3==(d*x3+e*y3+f)/denom3

es={eu0,ev0,eu1,ev1,eu2,ev2,eu3,ev3}
vars={a,b,c,d,e,f,g,h}
Solve[es,vars]

#MAY NOT WORK!


