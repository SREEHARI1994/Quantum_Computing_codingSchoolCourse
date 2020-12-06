import math
def cos(n):
	return math.cos(n)
def tan(n):
	return math.tan(n)

def cartesian_to_polar(x,y):
	# Calculating radius
	radius = math.sqrt( x * x + y * y )
	# Calculating angle (theta) in radian
	theta = math.atan(y/x)
	if x<0 and not y<0:
		theta=math.pi+theta
	return radius,theta

def polar_to_cartesian(radius,theta):
	x = radius * math.cos(theta)
	y = radius * math.sin(theta)
	return x,y

if __name__=="__main__":
	pi=math.pi
	#1st question
	a=pi/4
	print(f"1) {math.sin(a):.2f}")
	#2nd question
	a=pi/2
	print(f"2) {math.sin(a):.2f}")
	#3rd question
	a=pi/3
	print(f"3) {math.sin(a):.2f}")
	#4th question
	a=0
	print(f"4) {math.sin(a):.2f}")
	#fifth question
	b=0
	print(f"5) {math.cos(b):.2f}")
	#questions 6-10
	quantity={6:pi/3,7:3*pi/4,8:-pi/6,9:2*pi/3,10:5*pi/4}
	for i in range(6,11):
		if i in[6,7,8]:
			print(f"{i} {cos(quantity[i]): .2f}")
		else:
			print(f"{i} {tan(quantity[i]): .2f}")
	#questions 11-20
	quantity={11:[3,4],12:[math.sqrt(3),1],13:[-2,2],14:[0,1],15:[5,12],16:[1,0],17:[3,pi/4],18:[3,9*pi/4],
				19:[5,2*pi/3],20:[2,11*pi/6]}
	for i in range(11,21):
		
		if i in (11,12,13,15):
			
			print(f"{i} {cartesian_to_polar(*quantity[i])}")
		elif i==14:
			print(f"{i} {pi/2}")
		else:
			print(f"{i} {polar_to_cartesian(*quantity[i])}")



	

