import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return (x*x*x*x-1)
	
def f_dev(x):
	return (4*x*x*x)
	
def x_roots():
	return ([1,-1,1j,-1j])
	
def x_colors():
#	return ({1:'r.',-1:'g.',1j:'b.',-1j:'y.'})
	return ({1:1,-1:2,1j:3,-1j:4})
	
def newton(a,maxiter,tolerance,roots):
	x=a
	for i in range(maxiter):
		if (f_dev(x)==0):
			return None,i
		x-=f(x)/f_dev(x)
		for root in roots:
			if (abs(x.real-root.real)<=tolerance.real and abs(x.imag-root.imag)<=tolerance.imag):
				return root, i
	return None, maxiter
	
def color(m,color):
	plt.plot(m.real,m.imag,color,linewidth=0.005)
	
if __name__=='__main__':
	roots = x_roots()
	colors = x_colors()
	x_i=-1.0
	x_f=1.0
	y_i=-1.0
	y_f=1.0
#	plt.xlim(x_i,x_f)
#	plt.ylim(y_i,y_f)
#	plt.xticks([])
#	plt.yticks([])
#	plt.grid(True)
	each_diff=0.001
	real_nums=int((x_f-x_i)/each_diff)
	imag_nums=int((y_f-y_i)/each_diff)
#	dot=x_i+x_f*1j
	maxiters=75
	tolerance=0.00001+0.00001j
	image=np.zeros((real_nums,imag_nums))
	i=0;j=0
	for x in np.arange(x_i,x_f,each_diff):
		for y in np.arange(y_i,y_f,each_diff):
			root,iters = newton(x+y*1j,maxiters,tolerance,roots)
			if (root!=None): image[i][j] =colors[root]
			j+=1
		j=0
		i+=1
#			if (root!=None): color_(dot,colors[root])
#			dot+=each_diff*1j
#		dot-=each_diff*1j*imag_nums
#		dot+=each_diff
		
	plt.imshow(image,extent=[x_i, x_f, y_i, y_f], interpolation="bicubic")
#	plt.show()
	plt.savefig('frac3img_bicubic_nogrid_0_001.png',dpi=400,bbox_inches='tight',pad_inches=0.05)

