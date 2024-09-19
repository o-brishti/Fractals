import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x, n):
	return x**n - 1
	
def derivative(x, n):
	return n*x**(n-1)
	
def fractal(n, tol = 0.001):

	roots = np.array([np.exp(2j*np.pi*k/n) for k in range(n)]) 

	res = 600
	X = np.linspace(-2, 2, res)
	Y = np.linspace(-2, 2, res)

	x,y = np.meshgrid(X,Y)

	Z = x + 1j*y

	for i in range(100):
		Z = Z - f(Z, n)/derivative(Z, n)
		

	distances = np.array([np.abs(Z - r) < tol for r in roots])
	colors = np.argmax(distances, axis=0)
	
	return colors
	
	
fig, ax = plt.subplots(figsize=(12,12))


def animate(frames):
	ax.clear()
	n = 3 + frames;
	colors = fractal(n)
	ax.imshow(colors, cmap = 'viridis')
	ax.set_title(f"n = {n}")
	ax.axis('off')

anim = animation.FuncAnimation(fig, animate, frames=range(10), repeat=True)
text = fig.text(0.50, 0.02, 
	'z = z^n - 1',
	horizontalalignment='center', wrap=True )
plt.show()











