import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1.0,1.0,0.02)
plt.plot(x,x**3+0.1,'navy', label='f(x)=$x^3+0.1$')
l=np.arange(0.0,(0.2)**3+0.1,0.02)
plt.plot([0.2]*len(l),l,'r:')
m = np.arange(0.0,(0.2)**3+0.102,0.02)
plt.plot(0.2+((m-(0.2*0.2*0.2+0.1))/(3*0.2*0.2)),m,'g', label='tangent line')
plt.plot(0.2,0.0,'ro',label=r'$x$')
plt.ylim(-1.0,1.0)
plt.xlim(-1.5,1.5)
plt.xticks(np.arange(-1.5,1.6,0.5))
plt.yticks(np.delete(np.arange(-1.0,1.1,0.5),2))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.gca().yaxis.set_label_coords(0.55,0.96)
plt.gca().xaxis.set_label_coords(0.98,0.55)

plt.text(0.2+0.05,0.04,r'(0.2,0)')

plt.title('Plot 2.5')
plt.gca().title.set_position([0.5,1.05])
plt.legend()
plt.grid(True)

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
#plt.xaxis.set_ticks_position('bottom')
plt.gca().spines['bottom'].set_position(('data',0))
#plt.yaxis.set_ticks_position('left')
plt.gca().spines['left'].set_position(('data',0))

plt.show()
