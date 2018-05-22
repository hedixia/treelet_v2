

class MLT ():
	def __init__ (self):
		self.clust = SA_clust(dataset, slice, sample_para, kernel)
		self.clust.tree()
		temp_clusters = self.clust.clusters(num_clust, "D")
		for each_cluster in temp_clusters:
			temp_dataset = temp_clusters[each_cluster]
			reg_MLT = MLT()
			