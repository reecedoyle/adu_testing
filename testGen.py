TEST_SIZE = 60 #1 hour
#declare blank list to start
altList = [[0 for x in xrange(4)] for x in xrange(TEST_SIZE)]

def writeList(filename):
	#calculated average using avgCalc.py
	i = [17.7, 14.1, 21.6, 20.6]
	with open(filename, 'w') as f:
		for l in altList:
			for x in xrange(4):
				i[x] = i[x] + l[x]
				f.write('%f '%i[x])
			f.write('\n')
#revert to empty list
def resetList():
	global altList
	altList = [[0 for x in xrange(4)] for x in xrange(TEST_SIZE)]
#alter data points
def alt(temp, amount, start, end):
	for x in xrange(start,end):
		altList[x][temp] = amount

def do():
	resetList()
	alt(0, 0.1, 0, 3)
	writeList('testtest.txt')
do()