def vector_inner_product(a,b):
    if len(a)!=len(b):
        return "The two vectors should be of same dimensions"
    product=0
    for i in range(len(a)):
        product=product+a[i]*b[i]
    return product

def check_orthogonal(a,b):
	if vector_inner_product(a,b)==0:
		return True
	else:
		return False

def linear_combination_len2(r,a,b):
	"""
	returns a linear combinations of vectors of length 2,solving by elimination
	1st equation coefficients-
	rightside=r[0]
	x_coefficient=a[0]
	y_coefficient=b[0]
	2nd equation coefficients
	rightside=r[1]
	x_coefficient=a[1]
	y_coefficient=b[1]
	"""
	original=(r[0],a[0],b[0])
	if a[0]>=a[1]:
		multiplier=a[0]/a[1]
		r[1]=r[1]*multiplier
		a[1]=a[1]*multiplier
		b[1]=b[1]*multiplier
	else:
		multiplier=a[1]/a[0]
		r[0]=multiplier*r[0]
		a[0]=multiplier*a[0]
		b[0]=multiplier*b[0]
	
	assert a[0]-a[1]==0
	y=(r[0]-r[1])/(b[0]-b[1])
	x=(original[0]-y*original[2])/original[1]
	return x,y

def transpose(p):
	"""returns the transpose t of a matrix p"""
	t=[]
	for i in range(len(p)):
		row=[]
		for j in range(len(p[i])):
			row.append(p[j][i])
		t.append(row)
	return t

def matrix_multiply(a,b):
	res=[]
	for row in a:
		r=[]
		for column in b:
			r.append(vector_inner_product(row,column))
		res.append(r)
	return res
			

		


if __name__ == "__main__":
	print("1) ",vector_inner_product([5,2],[6,8]))
	print("2) ",vector_inner_product([3,10],[1,7]))
	print("3) ",vector_inner_product([1,-2,4],[2,3,3]))
	print("4) ",check_orthogonal([1,5],[-5,1]))
	print("5) ",check_orthogonal([3,6,2],[1,4,3]))
	print("6) ", linear_combination_len2([5,5],[1,2],[3,1]))
	print("7) ", linear_combination_len2([-7,16],[1,2],[3,1]))
	print("8 ",matrix_multiply([[2,3],[1,4]],[[3,-2]]))
	print("9 ",matrix_multiply([[1,4],[0,5]],[[1,1]]))
	print("10 ",matrix_multiply([[-2,6],[9,4]],[[3,-5],[3,1]]))



