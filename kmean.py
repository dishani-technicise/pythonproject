iterations = 20
nclusters = 12

nelms = 2000
ncoords = 2 

spreading = 0.3
clumpiness = 4

def distance(v1,v2):
	
	if len(v1)==0 or len(v2)==0:
		return 1000 
	sum = 0
	for i in range(len(v1)):
		sum += ((v2[i]-v1[i])**2)
	return sqrt(sum)




def centroid(l):
	if len(l)==0:
		return [0,0]
	res = [0,0]
	for i in range(len(res)):
		for a in l:
			res[i]+=elms[a][i]
	for i in range(len(res)):
		res[i]/=len(l)
	return res

def calculateCentroids(l):
	res = []
	for i in l:
		res.append(centroid(i))
	return res

def printClusters(l):
	for n,c in enumerate(l):
		print("cluster: "+str(n))
		for x in c:
			print(elms[x])
		print()
	print()
	


elms = []
for i in range(nelms):
	v = []
		
	if ncoords > 2: 
		for n in range(ncoords):
			val = int(cos(n)+i)%clumpiness 
			if myrand(i+myrand(n))>0.5: 
				val = -val
			else:
				val = +val
		
			if myrand(i+myrand(n))>0.5: 
				noise = sin(myrand(i+myrand(n)))*spreading
			else:
				noise = -sin(myrand(i+myrand(n)))*spreading
				
			v.append(val+noise)
	elif ncoords==2: 
		center = []
		for n in range(ncoords):
			val = int(cos(n)+i)%clumpiness 
			if myrand(i+myrand(n))>0.5: 
				val = -val
			else:
				val = +val
			center.append(val)

		for n in range(ncoords):
			for a in range(1,1000): 
				x = myrand(i+myrand(n)*a) 
				y = myrand(n+myrand(i)/a) 
							
				x = x if myrand(i+myrand(n))>0.5 else -x
				y = y if myrand(n+myrand(i))>0.5 else -y
				
				if x**2 + y**2 < spreading:
					center[0] = center[0]+x
					center[1] = center[1]+y
					break 
		v = center
	elms.append(v)


clusters= []
for i in range(nclusters):
	clusters.append([])
for i in range(len(elms)):
	pos = i%nclusters
	clusters[pos].append(i)

print("kmeans")
print("clustering "+str(nelms)+" vectors with "+str(ncoords)+" components in "+str(nclusters)+" clustets")
centroids = calculateCentroids(clusters)
print("centroids")
print(centroids)
print()


print("-----")
	
new_assignment = []
for n in range(iterations):
	


	centroids=calculateCentroids(clusters) 
	for i in range(nclusters):
		clusters[i]=[]
	for e in range(len(elms)): 
		best = 0
		bestd = 1000
		for c in range(nclusters): 
			d = distance(centroids[c],elms[e])
			if d < bestd:
				best = c
				bestd = d
		if len(clusters[best])==0:
			clusters[best]=[]
		clusters[best].append(e)

printClusters(clusters)
print()