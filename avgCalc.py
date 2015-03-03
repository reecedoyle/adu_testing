def num(s):
	try:
		return int(s)
	except ValueError:
		return float(s)

avg = [0,0,0,0]
count = 0
with open('temperatures.log', 'r') as temps:
	for line in temps:
		values = [num(x) for x in line.rstrip().split()]
		if len(values) == 5:
			for x in xrange(0,4):
				print values[0], x
				avg[x] = ((avg[x]*count)+values[x+1])/(count+1)
				count = count +1
print avg
print count