from math import*
def simpson(f,a,b,n):
	h=(b-a)/n
	s=0
	x=a
	for i in range (1,n):
		s=s+2*(i%2+1)*f(x+i*h)
	s=h/3*(f(a)+s+f(b))
	return s

def f(x): return sqrt(1+cos(x)**2)
r=simpson(f,0,2,16)
print(r)