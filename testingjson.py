import json

data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}
moreData = {
	'name' : 'Google',
	'shares' : 20,
	'price' : 123.4
}
allData = {
	'data' : data,
	'moreData' : moreData
}
print(allData['data'])
# Writing JSON data
with open('data.json', 'w') as f:
	json.dump(allData, f)
# Reading data back
with open('data.json', 'r') as f:
     allData = json.load(f)
print(allData['data'])