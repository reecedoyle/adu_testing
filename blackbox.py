import math
from random import randint
import glob

WINDOW_SIZE = 3
BANDWIDTH = [0.302494, 0.597704, 0.467658, 0.768034]

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def calcScore(test, other):
	value = 0
	for x in xrange(0, 4):
		value += -(((test[x]-other[x])**2)/(2*(BANDWIDTH[x]**2)))
		value = math.e ** value
	return value

def runTest(testIn, temperaturesIn, scoresOut, offset):
	with open(testIn, 'r') as test, open(scoresOut, 'w') as scores:
		count = 0 #counts line in test file
		testList = [] #to store each previous data point in the test file
		for line in test: #iterate through each test data point
			testList.append([num(x) for x in line.rstrip().split(' ')])
			score = 0
			with open(temperaturesIn, 'r') as temps:
				#skip to a particular window
				for x in xrange(0,offset*WINDOW_SIZE):
					next(temps)
				#perform calculations on previous test data
				for x in xrange(0, count):
					next(temps)
					score += calcScore(testList[count], testList[x])
				#perform calculations on temps data
				tempCount = 0 #keep track of number of temp data points used
				for tempLine in temps:
					if tempCount >= WINDOW_SIZE - count:
						break
					values = [num(x) for x in tempLine.rstrip().split()]
					if len(values) == 5:
						score += calcScore(testList[count], values[1:])
						tempCount += 1
			#limit score
			score = 1/score
			if score > 1:
				score = 1
			#WRITE SCORES TO FILE OR WHATEVER
			scores.write('%f\n'%score)
			count += 1 #keep track of line in the test file

for testname in glob.glob("tests/test.*.txt"):
	for x in xrange(0,6):
		runTest(testname, 'temperatures.log', 'tests/scores.'+testname.split('test.')[1].split('.txt')[0]+'.'+repr(x)+'.txt', x)



