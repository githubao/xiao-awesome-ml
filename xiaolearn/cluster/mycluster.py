#!/usr/bin/env python
# encoding: utf-8



"""
@description: 数据聚类demo

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: mycluster.py
@time: 2016/11/23 14:43
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

def demo():
    cluster1 = np.random.uniform(0.5,1.5,(2,10))
    cluster2 = np.random.uniform(3.5,4.5,(2,10))

    X = np.hstack((cluster1,cluster2)).T

    plt.figure()
    plt.axis([0,5,0,5])
    plt.grid(True)
    plt.plot(X[:,0],X[:,1],'k.')
    # plt.show()

    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)
    plt.plot(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],'ro')
    plt.show()


# 算法确定聚几类合适
def cluster_num():
    cluster1 = np.random.uniform(0.5,1.5,(2,10))
    cluster2 = np.random.uniform(1.5,2.5,(2,10))
    cluster3 = np.random.uniform(2.5,3.5,(2,10))
    cluster4 = np.random.uniform(3.5,4.5,(2,10))

    X1 = np.hstack((cluster1,cluster2))
    X2 = np.hstack((cluster3,cluster4))
    X = np.hstack((X1,X2)).T

    K = range(1,10)
    meandistortions = []
    for k in K:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(X)

        cost = sum(np.min(cdist(X,kmeans.cluster_centers_,'euclidean'),axis=1))/X.shape[0]
        meandistortions.append(cost)

    plt.figure()
    plt.grid(True)
    plt1 = plt.subplot(2,1,1)
    plt1.plot(X[:,0],X[:,1],'k.')

    plt2 = plt.subplot(2,1,2)
    plt2.plot(K,meandistortions,'bx-')
    plt.show()



def main():
    demo()
    # cluster_num()


if __name__ == '__main__':
    main()

