import json
import urllib2
import time
import sys

while 1:
	data = json.load(urllib2.urlopen('http://services.vrt.be/epg/playlists/now-on-air?channel_code=41&accept=application%2Fvnd.epg.vrt.be.onair_1.1%2Bjson'))
	
	if data["noa"]["songs"]:
		print "TITLE=" + data["noa"]["songs"][0]["title"] + "\nARTIST=" + data["noa"]["songs"][0]["artist"] + "\n."
		sys.stdout.flush()
	else:
		sys.stdout.flush()

	time.sleep(10)