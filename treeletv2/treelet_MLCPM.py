import treelet
from treelet_clust import treelet_clust
from treelet_CPM import treelet_CPM, compare
import numpy as np
from kernel import kernel 
from random import sample
from copy import copy

class treelet_MLCPM:
	standard_sample_size = 300
	def __init__ (self, cpm, slice = None, proceed = False):
		self.cpm = cpm
		if slice != None:
			self.slice = slice
			self.n = len(slice)
		else:
			self.slice = cpm.slice 
			self.n = cpm.n
		self.pure = self.check()
		if proceed and not self.pure:
			self.sample(standard_sample_size)
			self.train()
			
	def check (self, tol):
		return self.cpm.purity(self.slice) > 1 - tol
		
	def sample (self, k):
		if k <= self.n:
			self.samp = sample(range(self.n), k)
		else:
			self.samp = range(self.n)
		
	def train (self):
		self.sa_tr = copy(self.cpm)
		self.sa_tr.slice = self.samp
		self.sa_tr.cor()
		self.sa_tr.tree()
		self.sa_tr.train()
		cluster_assignment, cluster_tsdata = self.sa_tr.predict(self.tr_data, clust_info = True)
		self.next_level = {one_cluster:treelet_MLCPM(self.cpm, [self.slice[i] for i in cluster_tsdata[one_cluster]], True) for one_cluster in keys(cluster_tsdata)}

	def predict (self, test_dataset):
		