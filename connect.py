import requests

server = "http://localhost:5000"

# get list of GPIOs
url = "%s/gpio"%(server, )
print "Getting from", url
r = requests.get(url)
print "- return code", r.status_code
print "- data:", r.json()
print ""

# get value for A0
url = "%s/gpio/A0"%(server, )
print "Getting from", url
r = requests.get(url)
getData = r.json()
print "- return code", r.status_code
print "- data:", getData
print ""

# set (using put) value for A0
putData = {'data': str(int(getData['value'])+2) }
print "Putting data", putData, "to", url
r = requests.put(url, json=putData)
print "- return code", r.status_code
print ""

# get newvalue for A0
print "Getting from", url
r = requests.get(url)
getData = r.json()
print "- return code", r.status_code
print "- data:", getData
print ""


