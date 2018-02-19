import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-(np.pi/2.0),np.pi/2.0,0.02)
plt.plot(x,np.sin(x),'navy', label='f(x)=sin(x)')
plt.plot(-(np.pi/24),0,'ro',linewidth=3, label=r'$x_2$')
l=np.arange(np.sin(-(np.pi/24)),0.05,0.07)
plt.plot([-(np.pi/24)]*len(l),l,'r:')
m=np.arange(-(np.pi/24),0.05,0.07)
plt.plot(m,[-np.sin(np.pi/24)]*len(m),'r:')
plt.plot(np.pi/4,0,'go',linewidth=3, label='$x_1$')
n=np.arange(0.0,np.sin(np.pi/4)+0.01,0.1)
plt.plot([np.pi/4]*len(n),n,'g:')
o=np.arange(0.0,np.pi/4+0.09,0.1)
plt.plot(o,[np.sin(np.pi/4)]*len(o),'g:')
plt.plot((np.pi/4-np.pi/24)/2,0,color='cyan',marker='x',ms=7.0,mew=2.0,linestyle='None',label=r'$x_3$')
plt.ylim(-1.0,1.0)
plt.xlim(-1.5,1.5)
plt.xticks(np.delete(np.arange(-1.5,1.6,0.5),3))
plt.yticks(np.delete(np.arange(-1.0,1.1,0.5),2))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.gca().yaxis.set_label_coords(0.55,0.95)
plt.gca().xaxis.set_label_coords(0.98,0.55)

plt.text(np.pi/4+0.05,0.05,r'$(\pi/4,0)$')
plt.text(-0.5,np.sin(np.pi/4),r'$(0,sin(\pi/4))$')
plt.text(np.pi/4+0.05,np.sin(np.pi/4)-0.1,'('+str(round(np.pi/4,2))+','+str(round(np.sin(np.pi/4),2))+')')

plt.text((np.pi/4-np.pi/24)/2-0.2,0.05,r'$(5\pi/48,0)$')

plt.text(-(np.pi/24)-0.3,0.075,r'$(-\pi/24,0)$')
plt.text(0.03,np.sin(-(np.pi/24)-0.07),r'$(0,sin(-\pi/24))$')
plt.text(-0.7,-0.19,'('+str(round((-np.pi/24),2))+','+str(round(np.sin(-np.pi/24),2))+')')

plt.title('Plot 1.2')
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
