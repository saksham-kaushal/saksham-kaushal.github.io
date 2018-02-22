import matplotlib.pyplot as plt
import numpy as np


def f(x):
	return x*x*x*x-1
	
def f_dev(x):
	return 4*x*x*x

def roots_list():
	return [1.0,-1.0,1j,-1j]

def colors_dict():
	return {1.0:'r.',-1.0:'g.',1j:'b.',-1j:'k.'}

def newton(a,maxiter,tolerance,roots):
	x=a
	iters=0
	for i in range(maxiter):
		if (f_dev(x)!=0):
			x-=f(x)/f_dev(x)
		iters = i
		for root in roots:
			if (abs(x.real-root.real)<=tolerance.real and abs(x.imag-root.imag)<=tolerance.imag):
				return root , iters
	return None, maxiter

def color(root,i,m):
	colors=colors_dict()
#	print(m.real,m.imag,colors[root])
	plt.plot(m.real,m.imag,colors[root],linewidth=0.1)


if __name__ == '__main__':
	m = -1.0-1.0j
	maxiter = 75
	tolerance = 0.00001+0.00001j
	roots = roots_list()
	plt.xlim(-1.0,1.0)
	plt.ylim(-1.0,1.0)
	plt.xticks([-1.0,0.0,1.0])
	plt.yticks([-1.0,1.0])
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.gca().xaxis.set_label_coords(0.98,0.55)
	plt.gca().yaxis.set_label_coords(0.55,0.96)
	maxi=0
	for j in range(200):
		for k in range(200):
			root,i = newton(m, maxiter, tolerance, roots)
			if(i>maxi): maxi = i
#			print (root,i)
			if(root!=None): color(root,i,m)
#			print(m)
			m+=0.01j
		print('countdown',200-j,' i=',maxi)
		maxi=0
		m-=200*0.01j
		m+=0.01
	
	plt.show()
