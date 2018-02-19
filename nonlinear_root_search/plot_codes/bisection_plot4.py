import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5,5,0.05)
plt.plot(x,x**2,'navy', label='$f(x)=sin(x)$')
l=np.arange(0,1.5*1.5+0.05,0.1)
plt.plot([-1.5]*len(l),l,'k:')
plt.plot(-1.5,0,'ko',linewidth=2,label=r'$x_i$')
m=np.arange(0,1.75*1.75+0.05,0.1)
plt.plot([1.75]*len(m),m,'k:')
plt.plot(1.75,0,'ko',linewidth=2)
plt.ylim(-1,5)
plt.xlim(-2.5,2.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.gca().yaxis.set_label_coords(0.55,0.95)
plt.gca().xaxis.set_label_coords(0.98,0.2)

plt.title('Plot 1.4')
plt.gca().title.set_position([0.5,1.05])
plt.legend()
plt.grid(True)

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data',0))
plt.gca().spines['left'].set_position(('data',0))

plt.show()
