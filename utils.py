# formula for line to determine 'in' and 'out'
def get_y_from_x(x, gradient, y_intercept=0):
	y = gradient * x + y_intercept
	return y

def get_x_from_y(y, gradient, y_intercept=0):
	x = (y - y_intercept) / gradient
	return x
