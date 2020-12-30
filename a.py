import numpy as np
from matplotlib import pyplot as plt
size = 150
x: np = np.random.randint(0,70,size)
print(x.shape)
y: np =np.array(3*x-5+5*np.random.randn(size))
plt.scatter(x, y, s=150)
# plt.show()

def lsm_regression(x,y):
    beta=[]
    avg_x = np.mean(x)
    sum((x-avg_x)**2)
    avg_x = np.mean(x)
    avg_y = np.mean(y)
    b1 = sum((x-avg_x)*(y-avg_y)) / sum((x-avg_x)**2)
    print(b1)
    b0 = avg_y - b1*avg_x
    print(b0)
    # b0 = intercept b1 = slope
    beta.append(b0)
    beta.append(b1)
    return beta



judy = lsm_regression(x,y)
xs=np.linspace(0,70,200)
ys2=judy[0]+judy[1]*xs
plt.plot(xs,ys2,'r','-')
plt.show()
