#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
from colored import fg, bg, attr, stylize

server = 'localhost'
port = '32400'
plex_token = ''
#----------------COLORS-----------------
white = fg('white')
yellow = fg('yellow')
green = fg('green')
red = fg('red')
reset = attr('reset')
#---------------------------------------

# session array
sessions = []

# get session status
fp = urllib.request.urlopen('http://'+server+':'+port+'/status/sessions?X-Plex-Token='+plex_token)
mybytes = fp.read()
fp.close()

# parse text into XML document
xmlstr = mybytes.decode("utf8")
root = ET.XML(xmlstr)

# traverse the XML looking for session data
for item in root.findall('./Video'):
	session = {}

	session['Title'] = item.attrib['title']

	# figure out if it's an episode, if so, get more data
	session['Type'] = item.attrib['type']
	if session['Type'] == 'episode':
		session['Series'] = item.attrib['grandparentTitle']
		session['Season'] = item.attrib['parentIndex'].zfill(2)
		session['Episode'] = item.attrib['index'].zfill(2)

	for child in item:
		if child.tag == 'User':
			session[child.tag] = child.attrib['title']
		if child.tag == 'Player':
			session[child.tag] = child.attrib['title']

	sessions.append(session)
print (stylize("CURRENT ", white) + stylize("PLEX ", yellow) + stylize("SESSIONS", white))
sessionNum = len(sessions)
print (stylize("Currently, ", white) + stylize('0', red) + stylize(" users are in a session.", white) if not sessions else stylize("Currently, ", white) + stylize(sessionNum, green) +  stylize(" user(s) are in a session:", white))
for session in sessions:
	if session['Type'] == 'episode':
		print (white + '- {0} is watching "{1} - S{2}E{3} - {4}" on {5}'.format(session['User'], session['Series'], session['Season'], session['Episode'], session['Title'], session['Player']) + reset)
	else:
		print (white + '- {0} is watching "{1}" on {2}'.format(session['User'], session['Title'], session['Player']) + reset)
