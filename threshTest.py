#import thresholds.py
import glob
AMBER_DEFAULT = 0.05
RED_DEFAULT = 0.5
RED_TARGET = 0.01 #1%
AMBER_TARGET = 0.05 #5%

def runTest(files):
	first = True
	prevScores = []
	amber = AMBER_DEFAULT
	red = RED_DEFAULT
	#print 'Amber (start): %s'%amber
	#print 'Red (start): %s'%red
	for filename in files:
		classFilename = 'classifications/classification.'+filename.split('scores.')[1]
		if first:
			first = False
		else:
			#set thresholds
			amber, red = getAutoThresh(prevScores, amber, red)
			#print 'Amber: %s'%amber
			#print 'Red: %s'%red
			prevScores = []
		with open(filename, 'r') as scores, open(classFilename, 'w') as classFile:
			classFile.write('Amber: %s, Red: %s\n'%(amber, red))
			for line in scores:
				score = float(line.rstrip())
				prevScores.append(score)
				classification = classify(score, amber, red)
				classFile.write('%s\n'%classification)

def classify(score, amber, red):
	if score >= red:
		return 'red'
	else:
		if score >= amber:
			return 'amber'
		else:
			return 'green'

def getAutoThresh(scores, prevAmber, prevRed):
	red = prevRed + (getThreshold(RED_TARGET, scores) - prevRed)/2
	amber = prevAmber + (getThreshold(AMBER_TARGET, scores) - prevAmber)/2
	return amber, red

def getThreshold(percentage, points):
	points = sorted(points)
	index = (len(points)-1) - int((len(points)*percentage))
	#print points
	#print 'Index: %d'%index
	#print 'Return: %f'%((points[index] + points[index-1])/2)
	return (points[index] + points[index-1])/2

def do():
	scoreFiles = []
	for filename in sorted(glob.glob("scores/scores.*.*.txt")):
		testNum, scoreNum = [int(x) for x in filename.split('scores.')[1].split('.txt')[0].split('.')]
		if len(scoreFiles) == testNum:
			scoreFiles.append([])
		scoreFiles[testNum].append(filename)
	#print scoreFiles
	for files in scoreFiles:
		runTest(files)
do()