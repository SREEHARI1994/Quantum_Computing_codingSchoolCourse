from week4 import matrix_multiply
def calculate_determinant4_2D(*m):
	"""
	Calculates and returns the determinants of a two by two real matrix.
	Arguments can be passed as either two (2 X 1) vectorsi.e 2 python 1D lists
	or as a single matrix of dim 2 X 2 or As a single 2D python list.
	"""
	if len(m)==2:
		matrix=[m[0],m[1]]
	else:
		matrix=m[0]
	return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])


def check4_linearIndependence(a,b):
	""" 
	It works on the principal that if the matrix formed by
	the two vectors a and b passed here as columns has a non zero determinant, then
	the vectors are linearly independent
	"""
	if calculate_determinant4_2D(a,b)==0:
		return False
	else:
		return True

def check_span_inR2(a,b):
	"""
	Takes in 2 vectors as arguments and finds out if the
	vectors spans R2 by checking if the determinant of the
	resulting matrix is non-zero. Refer-
	https://ltcconline.net/greenl/courses/203/Vectors/linIndSpan.htm
	"""
	if calculate_determinant4_2D(a,b)==0:
		return False
	else:
		return True
def eigen_equation(a,b):
	"""
	Takes in two matrix a and eigen vector b, multiplies them
	using matrix_multiply from week4.py. Then lambda X first value of 
	product vector = first value of b is used to calculate eigen value
	lambda by doing division. Note product vector is returned
	as a 2d list consisting of two single lists having only one element
	and also that b is passed in as a 2d list
	"""
	product_vector=[]
	result=matrix_multiply(a,b)
	product_vector.append(result[0][0])
	product_vector.append(result[1][0])
	eigen_value=product_vector[0]/b[0][0]
	return eigen_value
	
if __name__ =="__main__":
	print("1 True")
	print("2 True")
	print("3 False")
	print("4 True")
	print("5 b")
	print("6 a")
	print("7 a")
	print("8 b")
	#print(calculate_determinant4_2D([1,0],[0,1]))
	#print(calculate_determinant4_2D([[1,2],[3,4]]))
	print ("9",check4_linearIndependence([1,0],[0,1]))
	print ("10",check4_linearIndependence([1,2],[3,6]))
	print ("11",check4_linearIndependence([3,4],[7,1]))
	print ("12",check_span_inR2([1,3],[2,1]))
	print ("13",check_span_inR2([2,8],[1,4]))
	print ("14",check_span_inR2([5,5],[1,1]))
	print("15",eigen_equation([[1,4],[0,5]],[[1,1]]))
	print("16",eigen_equation([[7,0],[3,4]],[[-1,1]]))
	print("17",eigen_equation([[7,-1],[2,4]],[[0.5,1]]))
	exit()
	
	"""
	1 True
	2 True
	3 False
	4 True
	5 b
	6 a
	7 a
	8 b
	9 True
	10 False
	11 True
	12 True
	13 False
	14 False
	15 5.0
	16 7.0
	17 5.0
	"""	
		