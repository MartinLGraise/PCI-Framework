import numpy as np
r=0.7
# scalar 1D proxy for R=I, bA=1,bB=-1 opposed biases
for th in [0,0.1,0.5,1.57079632679]:
    c=np.cos(th); s=np.sin(th)
    M=np.array([[1-r*c, r*s],[-r*s,1-r*c]])
    b=np.array([1,-1.])
    x,y=np.linalg.solve(M,b)
    C1=np.sign(x) if abs(x)>1e-12 else 0
    C2=np.sign(-y) if abs(y)>1e-12 else 0
    print(th, x,y,C1,C2, min(C1,C2))
# compare paper general theta=pi/2 formula against true for non equal b
R=1.0; bA=2.0; bB=3.0
A=1+r*r
x_true=(bA-r*bB)/A
y_true=(r*bA+bB)/A
x_paper=(1-r)/A*bA - r/A*bB
y_paper=r/A*bA + (1+r)/A*bB
print('true',x_true,y_true,'paper',x_paper,y_paper)
