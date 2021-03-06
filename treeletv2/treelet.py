import numpy as np 
from jacobi_rotation import jacobi_rotation

class treelet:
	def __init__ (self, A, psi): 
		self.A = np.matrix(A)
		self.psi = psi
		self.phi = lambda x,y : psi(self.A[x,y], self.A[x,x], self.A[y,y])
		self.n = self.A.shape[0]
		self.max_row = {i:0 for i in range(self.n)}
		self.transform_list = []
		
	def fullrotate (self):
		self.rotate(self.n - 1)
		self.root = list(self.max_row)[0]

	def rotate (self, multi=False):
		if multi:
			for i in range(multi):
				self.rotate()
			self.dfrk = [self.transform_list[i][1] for i in range(self.n-1)].append(self.transform_list[-1][0])
		else:
			(p, q) = self._find()
			(cos_val, sin_val) = jacobi_rotation (self.A, p, q)
			self._record(p, q, cos_val, sin_val)
		
	def _find (self):
		if self.transform_list == []:
			self.max_row_val = {}
			for i in self.max_row:
				self._max(i)
		else:
			(l, k, cos_val, sin_val) = self.current
			for i in self.max_row:
				if i == k or i == l:
					self._max(i)
				if self.phi(self.max_row[i], i) < self.phi(k, i):
					self.max_row[i] = k
				if self.phi(self.max_row[i], i) < self.phi(l, i):
					self.max_row[i] = l
				if self.max_row[i] == k or self.max_row[i] == l:
					self._max(i)
		v = list(self.max_row_val.values())
		k = list(self.max_row_val.keys())
		i = k[v.index(max(v))]
		return (self.max_row[i], i)
	
	def _max (self, col_num):
		temp_max_row = 0
		max_temp = 0
		for i in self.max_row:
			if i == col_num:
				continue
			temp = self.phi(i, col_num)
			if temp >= max_temp:
				temp_max_row = i
				max_temp = temp
		self.max_row [col_num] = temp_max_row
		self.max_row_val [col_num] = max_temp 
	
	def _pair_gen (self):
		v = list(self.max_row_val.values())
		k = list(self.max_row_val.keys())
		i = k[v.index(max(v))]
		return (self.max_row[i], i)
		
	def _record (self, l, k, cos_val, sin_val, drop=True):
		if self.A[l,l] < self.A[k,k]:
			self.current = (k, l, cos_val, sin_val)
		else:
			self.current = (l, k, cos_val, sin_val)
		self.transform_list.append(self.current)
		del self.max_row[self.current[1]]
		del self.max_row_val[self.current[1]]

	#Treelet Tree 
	def tree (self):
		return [I[0:2] for I in self.transform_list]