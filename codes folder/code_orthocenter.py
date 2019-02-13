import numpy as np
import matplotlib.pyplot as plt

def dir_vec(BC):
	return np.matmul(BC,dvec)
	
def ortocenterH1(BC,CA):
	d1 = dir_vec(BC)
	d2 = dir_vec(CA)
	N1 = np.vstack((d1,d2))
	pa = np.zeros(2)
	pa[0] = np.matmul(d1,A)
	pa[1] = np.matmul(d2,B)
	return np.matmul(np.linalg.inv(N1),pa)

def ortocenterH2(CA,AB):
	d2 = dir_vec(CA)
	d3 = dir_vec(AB)
	N2 = np.vstack((d2,d3))
	pb = np.zeros(2)
	pb[0] = np.matmul(d2,B)
	pb[1] = np.matmul(d3,C)
	return np.matmul(np.linalg.inv(N2),pb
	)
def ortocenterH3(AB,BC):
	d3 = dir_vec(AB)
	d1 = dir_vec(BC)
	N3 = np.vstack((d3,d1))
	pc = np.zeros(2)
	pc[0] = np.matmul(d3,C)
	pc[1] = np.matmul(d1,A)
	return np.matmul(np.linalg.inv(N3),pc)
		
A = np.array([2,-6])
B = np.array([5,2])
C = np.array([-2,2])

AB = np.vstack((A,B)).T
BC = np.vstack((B,C)).T
CA = np.vstack((C,A)).T
dvec = np.array([-1,1])

print(ortocenterH1(BC,CA))
print(ortocenterH2(CA,AB))
print(ortocenterH3(AB,BC))
