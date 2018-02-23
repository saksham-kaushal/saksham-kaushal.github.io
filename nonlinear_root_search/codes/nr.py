def f(x):
	return (x*x)
	
def f_dev(x):
	return (2*x)

def newton(a,maxiter,tolerance):
	x=a
	x_prev=a
	for i in range(maxiter):
		if (f_dev(x)==0):
			raise ZeroDivisionError
#			return None,i
		
		x-=f(x)/f_dev(x)
		if (abs(x.real-x_prev.real)<=abs(tolerance.real) and abs(x.imag-x_prev.imag)<=abs(tolerance.imag)):
			return x,i
		x_prev = x
	return x,maxiter
	
if __name__ == '__main__':
	m=20+100j
	maxiter = 50
	tolerance = 0.00001+0.00001j
	root,i=newton(m,maxiter,tolerance)
	print(root,i)
