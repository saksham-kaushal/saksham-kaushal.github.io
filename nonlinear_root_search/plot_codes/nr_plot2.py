import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-(np.pi/2.0),np.pi/2.0,0.02)
plt.plot(x,np.sin(x),'navy', label='f(x)=sin(x)')
l=np.arange(np.sin(-0.68),0.0,0.02)
plt.plot([-0.68]*len(l),l,'r:')
m = np.arange(np.sin(-0.68),0.0,0.02)
plt.plot((m-np.sin(-0.68))/np.cos(-0.68)-0.68,m,'g', label='tangent line')
plt.plot(-0.68,0,'ro',label=r'$x_1$')
plt.plot(-0.68-(np.tan(-0.68)),0,'cyan',marker='o',ms=5.0,mew=2.0,linestyle='None',label=r'$x_2$')
plt.ylim(-1.0,1.0)
plt.xlim(-1.5,1.5)
plt.xticks(np.arange(-1.5,1.6,0.5))
plt.yticks(np.delete(np.arange(-1.0,1.1,0.5),2))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.gca().yaxis.set_label_coords(0.55,0.96)
plt.gca().xaxis.set_label_coords(0.98,0.55)

plt.text(-0.68-0.05,0.05,r'(-0.68,0)')
plt.text(-0.68-0.75,np.sin(-0.68),'(-0.68,sin(-0.68))')
a=-np.sin(-0.68)/np.cos(-0.68)-0.68
plt.text(a,0.05,'('+str(round(a,2))+',0)')

plt.title('Plot 2.2')
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
