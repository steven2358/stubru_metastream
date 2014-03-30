Recommended Streamripper Options
================================
Adapted from [w-sky's Last.fm journal](http://www.last.fm/user/w-sky/journal/2008/12/31/2d7onq_scrobble_internet_radio_using_winamp_and_audioscrobbler_plugin)

Connection
----------
- Try to reconnect to the stream if it drops [yes]  
- Create relay stream [yes if you want to be able to get playback on another computer]  
- Don't rip over X megs [yes and a value if your hard disk space is quite limited]  
- Use the old way of retrieving the current track from winamp [typically not necessary]  
- Pretend to be (UserAgent) [default]
- Proxy Server [empty]
- Local Machine Name: localhost  

File
----
- Output directory [choose a directory on a drive with at least 1 GB of free space, preferably not the system drive (C: usually) - or set "don't rip over X megs" to a value of at least ~1000 MB less than your free space]  
- Rip to seperate files [yes]  
- Rip to single file [no]  
- Overwrite tracks in complete: [Make version]  
- Never overwrite files in complete folder [yes]
- Add ID3 V1 info to the tracks [yes]  
- Add ID3 V2.3 info to the tracks [yes]  
- Add finished tracks to winamp playlist [yes]  
- Number of initial songs to leave incomplete: 0  

Pattern
-------
- Output file pattern: `%S/%1q`  

Skins
-----
[as you wish]

Splitting
---------
[leave at default]

Ext/Codeset
-----------
Run external helper program to get metadata [yes]: `python YOURPATH/stubru_metastream.py`  
Codeset options [leave at default]  

