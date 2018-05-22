

class MLTC ():
	def __init__ (train_data, train_label, slice, kernel, CLM):
		self.dataset = train_data 
		self.label = train_label
		self.__slice = slice 
		self.K = kernel
		self.CLM = CLM
		self.leaf = False
		self.did_tree = False
		
	def assign (self, test_data):
		f = lambda one_data: self.clust.aff(self.clust.clust_dict[one_cluster], one_data, (True, False), True)
		return argmax(self.clust.clust_dict, f)
		
	def predict (self, test_data):
		if self.did_tree is False:
			self.tree()
		if self.leaf:
			return self.C.predict([test_data])[0]
		else:
			temp_next = self.assign(test_data)
			return self.C[temp_next].predict(test_data)
	
	def tree (self):
		self.did_tree = True
		#Do some checking 
		"""
		if :
			self.tree_SA()
		elif:
			self.tree_CPM()
			self.leaf = True
		else:
			self.notree()
			self.leaf = True
		"""
	
	def tree_SA (self, SACSA=False):
		if SACSA:
			self.clust = SACSA_clust(self.dataset, self.__slice, sample_para, num_clust, self.K)
		else:
			self.clust = SA_clust(self.dataset, self.__slice, sample_para, self.K)
		self.clust.tree()
		self.C = self.clust.clusters(num_clust, "D")
		for each_cluster in self.clusters:
			temp_dataset = temp_clusters[each_cluster]
			self.C[each_cluster] = MLTC(self.dataset, [self.__slice[i] for i in self.C[each_cluster]], self.K)
			
	def tree_CPM()
		pass 
		
	def notree(self):
		self.C = self.CLM(self.dataset, train_label, self.__slice)