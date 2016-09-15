import requests
#import json

server = "http://localhost:5000"

url = "%s/gpio"%(server, )
print "Getting from", url
r = requests.get(url)
print "- return code", r.status_code
print "-", r.json()
print ""

url = "%s/gpio/A0"%(server, )
print "Getting from", url
r = requests.get(url)
getData = r.json()
print "- return code", r.status_code
print "- data:", getData
print ""

putData = {'data': str(int(getData['value'])+2) }
#putDataJson = json.dumps( putData )
print "Putting data", putData, "to", url
r = requests.put(url, json=putData)
print "- return code", r.status_code
print ""

print "Getting from", url
r = requests.get(url)
getData = r.json()
print "- return code", r.status_code
print "- data:", getData
print ""


