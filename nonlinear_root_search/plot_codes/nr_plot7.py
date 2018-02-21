import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi,2*np.pi,0.02)
plt.plot(x,np.sin(x),'navy', label='f(x)=sin(x)')
l=np.arange(0.0,np.sin(np.pi/2.3),0.02)
plt.plot([np.pi/2.3]*len(l),l,'r:')
m = np.arange(0.0,np.sin(np.pi/2.3),0.02)
plt.plot((m-np.sin(np.pi/2.3))/np.cos(np.pi/2.3)+np.pi/2.3,m,'g', label='tangent line')
n = np.arange(0.0,np.sin(-3.45),0.02)
plt.plot([-3.45]*len(n),n,'c:')
plt.plot(np.pi/2.3,0,'ro',label=r'$x_0$')
plt.plot(np.pi/2.3-(np.tan(np.pi/2.3)),0,'cyan',marker='o',ms=5.0,mew=2.0,linestyle='None',label=r'$x_1$')
plt.ylim(-1.5,1.5)
plt.xlim(-5.0,5.0)
plt.xticks(np.arange(-5.0,5.1,1.0))
plt.yticks(np.delete(np.arange(-1.5,1.6,0.5),3))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.gca().yaxis.set_label_coords(0.55,0.96)
plt.gca().xaxis.set_label_coords(0.98,0.55)

plt.text(np.pi/2.3+0.05,0.05,r'($\pi$/2.3,0)')
plt.text(np.pi/2.3-1.1,np.sin(np.pi/2.3)+0.1,r'($\pi$/2.3,$sin(\pi$/2.3))')
a=-np.sin(np.pi/2.3)/np.cos(np.pi/2.3)+np.pi/2.3
plt.text(a-1.2,0.05,'('+str(round(a,2))+',0)')

plt.title('Plot 2.7')
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
