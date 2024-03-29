
import numpy
import os
import sys
import argparse
import pandas as pd
import datetime

def DBSCAN(D, eps, MinPts):

	labels = [0]*(len(D))

	C = 0

	for P in range(0, len(D)):

		if not (labels[P] == 0):
		   continue

		NeighborPts = regionQuery(D, P, eps)

		if len(NeighborPts) < MinPts:
			labels[P] = -1

		else:
		   C += 1
		   growCluster(D, labels, P, NeighborPts, C, eps, MinPts)

	return labels


def growCluster(D, labels, P, NeighborPts, C, eps, MinPts,rq):

	labels[P] = C

	i = 0
	while i < len(NeighborPts):

		Pn = NeighborPts[i]

		if labels[Pn] == -1:
		   labels[Pn] = C

		elif labels[Pn] == 0:

			labels[Pn] = C

			PnNeighborPts = regionQuery(D, Pn, eps)
			
			if len(PnNeighborPts) >= MinPts:
				NeighborPts = NeighborPts + PnNeighborPts

		i += 1



def regionQuery(D, P, eps):

	neighbors = []

	for Pn in range(0, len(D)):
		#distance between points is determined by using  percentge threshold, it can be replaced by ny other distance metric
		if abs(D[P][3] - D[Pn][3]) < D[P][3]*eps and D[P][2] == D[Pn][2]:
			neighbors.append(Pn)

	return neighbors
