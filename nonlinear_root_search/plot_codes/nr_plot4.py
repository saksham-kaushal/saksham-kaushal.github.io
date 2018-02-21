import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-(np.pi/1.5),np.pi/1.5,0.02)
plt.plot(x,np.sin(x),'navy', label='f(x)=sin(x)')
l=np.arange(0.0,np.sin(np.pi/2.693)+0.02,0.02)
plt.plot([np.pi/2.693]*len(l),l,'r:')
m = np.arange(0.0,np.sin(np.pi/2.693),0.02)
plt.plot((m-np.sin(np.pi/2.693))/np.cos(np.pi/2.693)+np.pi/2.693,m,'g', label='tangent line')
plt.plot(np.pi/2.693,0,'ro',label=r'$x_0,x_2.x_4...$')
n=np.arange(np.sin(-1.167),0.0,0.02)
plt.plot([-1.167]*len(n),n,'r:')
o = np.arange(np.sin(-1.167),0.0,0.02)
plt.plot((o-np.sin(-1.167))/np.cos(-1.167)-1.167,o,'g')

plt.plot(np.pi/2.693-(np.tan(np.pi/2.693)),0,'cyan',marker='o',ms=5.0,mew=2.0,linestyle='None',label=r'$x_1,x_3,x_5...$')
plt.ylim(-1.5,1.5)
plt.xlim(-2.5,2.5)
plt.xticks(np.arange(-2.5,2.6,0.5))
plt.yticks(np.delete(np.arange(-1.5,1.6,0.5),3))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.gca().yaxis.set_label_coords(0.55,0.96)
plt.gca().xaxis.set_label_coords(0.98,0.55)

plt.text(np.pi/2.693+0.05,0.05,r'(1.17,0)')
plt.text(np.pi/2.693+0.05,np.sin(np.pi/2.693)-0.15,r'(1.17,sin(1.17))')
plt.text(-np.pi/2.693-1.25,np.sin(-np.pi/2.693)+0.1,r'(-1.17,sin(-1.17))')
a=-np.sin(np.pi/2.693)/np.cos(np.pi/2.693)+np.pi/2.693
plt.text(a-0.65,0.05,'('+str(round(a,2))+',0)')

plt.title('Plot 2.4')
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
