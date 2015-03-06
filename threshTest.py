import thresholds.py

for testname in glob.glob("tests/scores.*.*.txt"):
	for x in xrange(0,6):
		testname.split('test.')[1].split('.')[1].split('.txt')[0]
		runTest(testname, 'tests/thresholds.'+testname.split('test.')[1].split('.txt')[0]+'.'+repr(x)+'.txt', x)