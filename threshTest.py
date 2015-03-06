#import thresholds.py
import glob
#'thresholds.'+testNum+'.'+scoreNum+'.txt'
scoreFiles = []
for filename in sorted(glob.glob("scores/scores.*.*.txt")):
	testNum, scoreNum = [int(x) for x in filename.split('scores.')[1].split('.txt')[0].split('.')]
	if len(scoreFiles) == testNum:
		scoreFiles.append([])
	scoreFiles[testNum].append(filename)
print scoreFiles
#runTest(scoreFiles)