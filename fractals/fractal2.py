import matplotlib.pyplot as plt

def f(x):
	return (x*x*x*x-1)
	
def f_dev(x):
	return (4*x*x*x)
	
def x_roots():
	return ([1,-1,1j,-1j])
	
def x_colors():
	return ({1:'r.',-1:'g.',1j:'b.',-1j:'y.'})
	
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
	plt.xlim(-2,2)
	plt.ylim(-2,2)
	plt.xticks([])
	plt.yticks([])
	plt.grid(False)
	each_diff=0.01
	real_nums=int(4/each_diff)
	imag_nums=int(4/each_diff)
	dot=-2-2j
	maxiters=75
	tolerance=0.00001+0.00001j
	for x in range(real_nums):
		for y in range(imag_nums):
			root,iters = newton(dot,maxiters,tolerance,roots)
			if (root!=None): color(dot,colors[root])
			dot+=each_diff*1j
		dot-=each_diff*1j*imag_nums
		dot+=each_diff
		print(x)
		
	plt.savefig('frac2img400x400.png')
