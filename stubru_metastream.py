import json
import urllib2
import time
import sys

noa_url = 'http://services.vrt.be/playlist/onair?channel_code=41&accept=application%2Fvnd.playlist.vrt.be.noa_1.0%2Bjson'

while 1:
  data = json.load(urllib2.urlopen(noa_url))
	
  onairs = data["onairs"];
  
  success = 0
  if onairs:
    for onair in onairs:
      if onair["type"] == "SONG" and onair["onairType"] == "NOW":
        for prop in onair["properties"]:
          if prop["key"] == "ARTISTNAME":
            artist = prop["value"]
          elif prop["key"] == "TITLE":
            title = prop["value"]
        
        if artist and title:
          success = 1

  if success:
    print "TITLE=" + title + "\nARTIST=" + artist + "\n."
    sys.stdout.flush()
  else:
    # broadcast is not music
    print "TITLE=none\nARTIST=\n."
    sys.stdout.flush()

  time.sleep(10)
