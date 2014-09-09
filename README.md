Studio Brussel Metastream Ripper
================================

This script lets you scrobble the Studio Brussel online radio station automatically through Winamp using Streamripper.

How to install
--------------

1. Install [Streamripper](http://streamripper.sourceforge.net) and link it to Winamp, as described in [this last.fm journal](http://www.last.fm/user/w-sky/journal/2008/12/31/2d7onq_scrobble_internet_radio_using_winamp_and_audioscrobbler_plugin) or the streamripper_options.md included here.
2. Install Python 2.x and add it to your path.  
3. Download `stubru_metastream.py`.  
4. In the Streamripper options dialog, in the tab Ext/Codeset, tick the External interface option and fill in `python "PATH_TO_SCRIPT"` where `PATH_TO_SCRIPT` is the local path of `stubru_metastream.py`.
5. Play the live stream from http://mp3.streampower.be/stubru-high through Winamp and start streamripper. Stop winamp playback and restart it when sufficient songs are in the playlist.

Troubleshooting
---------------

Tags not appearing? Check the following:  

1. Visit http://www.stubru.be/live and check if the song tags are appearing correctly on the live stream. The script will not work if the song tags don't appear here.  
2. Check if the song appears in http://services.vrt.be/playlist/onair?channel_code=41  

If the tags don't appear in any of these two, they are simply not being broadcasted. If they do appear, it should be possible to solve through the streamripper config.

More info
---------

http://streamripper.sourceforge.net/history.php  
http://services.vrt.be/  
http://services.vrt.be/epg/playlists/now-on-air  
