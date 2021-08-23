#!/usr/bin/env python3
from os import getenv
from re import search
from urllib import request, error
from xml.etree.ElementTree import XML

from colored import fg, attr, stylize
from dotenv import load_dotenv

# loads the environment variables from the .env file
load_dotenv()

# if your configuration for server/port is different than the defaults, edit them accordingly in the .env file
server = str(getenv('server'))
port = str(getenv('port'))
plex_token = str(getenv('plex_token'))
# ----------------COLORS-----------------
white = fg('white')
yellow = fg('yellow')
green = fg('green')
red = fg('red')
reset = attr('reset')
# ---------------------------------------

# session array
sessions = []


# open the url
def request_open():
	# get session status
	try:
		_fp = request.urlopen('http://' + server + ':' + port + '/status/sessions?X-Plex-Token=' + plex_token)
		_mybytes = _fp.read()
		_fp.close()
		return _fp, _mybytes
	except error.HTTPError as e:
		if e.code == 401:
			print(str(e) + '\n Please make sure your Plex token is correct and try again')
	except error.URLError as e:
		print(str(e.reason) + '\n Please make sure the Plex host is pointing to the right address and try again')


fp, mybytes = request_open()


# parse text into XML document
xmlstr = mybytes.decode("utf8")
root = XML(xmlstr)

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
		if child.tag == 'Media':
			session[child.tag] = child.attrib['videoResolution']

	sessions.append(session)
print(stylize('CURRENT ', white) + stylize('PLEX ', yellow) + stylize('SESSIONS', white))
sessionNum = len(sessions)
if sessionNum == 1:
	print(stylize('Currently, ', white) + stylize(sessionNum, green) + stylize(' user is in a session:', white))
else:
	print(stylize('Currently, ', white) + stylize('0', red) + stylize(' users are in a session.', white) if not sessions else stylize('Currently, ', white) + stylize(sessionNum, green) + stylize(' users are in a session:', white))

for session in sessions:
	if session['Type'] == 'episode':
		print(white + f'- {session["User"]} is watching "{session["Series"]} - S{session["Season"]}E{session["Episode"]} - {session["Title"]}" on {session["Player"]} in {session["Media"]}' + reset if search('[a-zA-Z]', session["Media"]) else f'- {session["User"]} is watching "{session["Series"]} - S{session["Season"]}E{session["Episode"]} - {session["Title"]}" on {session["Player"]} in {session["Media"]}p' + reset)
	else:
		print(white + f'- {session["User"]} is watching "{session["Title"]}" on {session["Player"]} in {session["Media"]}' + reset if search('[a-zA-Z]', session["Media"]) else white + f'- {session["User"]} is watching "{session["Title"]}" on {session["Player"]} in {session["Media"]}p' + reset)
