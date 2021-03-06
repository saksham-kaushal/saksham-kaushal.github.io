import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-(np.pi/1.5),np.pi/1.5,0.02)
plt.plot(x,np.sin(x),'navy', label='f(x)=sin(x)')
plt.plot(-(np.pi/3),0,'ro',linewidth=3, label=r'$x_0$')
l=np.arange(np.sin(-(np.pi/3)),0.09,0.1)
plt.plot([-(np.pi/3)]*len(l),l,'r:')
m=np.arange(-(np.pi/3),0.09,0.1)
plt.plot(m,[-np.sin(np.pi/3)]*len(m),'r:')
plt.plot(np.pi/4,0,'go',linewidth=3, label='$x_1$')
n=np.arange(0.0,np.sin(np.pi/4)+0.01,0.1)
plt.plot([np.pi/4]*len(n),n,'g:')
o=np.arange(0.0,np.pi/4+0.09,0.1)
plt.plot(o,[np.sin(np.pi/4)]*len(o),'g:')
plt.plot((np.pi/4-np.pi/3)/2,0,color='cyan',marker='x',ms=7.0,mew=2.0,linestyle='None',label=r'$x_2$')
plt.ylim(-1.5,1.5)
plt.xlim(-2.5,2.5)
plt.xticks(np.arange(-2.5,2.6,0.5))
plt.yticks(np.delete(np.arange(-1.5,1.6,0.5),3))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.gca().yaxis.set_label_coords(0.55,0.96)
plt.gca().xaxis.set_label_coords(0.98,0.55)
plt.text(np.pi/4+0.05,0.05,r'$(\pi/4,0)$')
plt.text(-0.85,np.sin(np.pi/4),r'$(0,sin(\pi/4))$')
plt.text(np.pi/4+0.05,np.sin(np.pi/4)-0.1,'('+str(round(np.pi/4,2))+','+str(round(np.sin(np.pi/4),2))+')')
plt.text((np.pi/4-np.pi/3)/2-0.65,0.075,r'$(-\pi/24,0)$')

plt.text(-(np.pi/3)-0.65,0.05,r'$(-\pi/3,0)$')
plt.text(0.05,np.sin(-(np.pi/3)),r'$(0,sin(-\pi/3))$')
plt.text(-2.0,-0.85,'('+str(round((-np.pi/3),2))+','+str(round(np.sin(-np.pi/3),2))+')')

plt.title('Plot 1.1')
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
