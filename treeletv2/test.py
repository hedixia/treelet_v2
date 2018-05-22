import treelet
from treelet_clust import treelet_clust
from treelet_CPM import treelet_CPM, compare
from SA_method import SA_clust
from SACSA_method import SACSA_clust
import numpy as np
import csv 
import os 
from kernel import kernel 
import random 
import matplotlib.pyplot as plt

x = 10
dataset = [[i//10, i//10] for i in range(10*x)]
ker = kernel("ra", [1])
temp_sac = SACSA_clust(dataset, 10*x, 5*x, 10, ker)
temp_sac.tree()
print(temp_sac.sample_index)
temp_dl = temp_sac.clusters(10, "L")
print(temp_dl)