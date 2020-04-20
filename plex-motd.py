#!/usr/bin/env python3.5

import urllib.request
import xml.etree.ElementTree as ET

server = 'localhost'
port = '32400'
plex_token = ''
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

print ("There are currently {0} sessions:\n".format(len(sessions)))
for session in sessions:
	if session['Type'] == 'episode':
		print ('* {0} is watching "{1} - S{2}E{3} - {4}" on {5}'.format(session['User'], session['Series'], session['Season'], session['Episode'], session['Title'], session['Player']))
	else:
		print ('* {0} is watching "{1}" on {2}'.format(session['User'], session['Title'], session['Player']))
