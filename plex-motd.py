#!/usr/bin/env python3
from os import getenv
from re import search
from urllib import request, error
from xml.etree.ElementTree import XML

from dotenv import load_dotenv

# loads the environment variables from the .env file
load_dotenv()

# if your configuration for server/port is different from the defaults, edit them accordingly in the .env file
server = str(getenv('server'))
port = str(getenv('port'))
plex_token = str(getenv('plex_token'))
# ----------------COLORS-----------------
white = '\033[1;37m'
yellow = '\u001b[1;33m'
green = '\u001b[32m'
red = '\u001b[31m'
reset = '\u001b[0m'
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
            exit(str(e) + '\n Please make sure your Plex token is correct and try again')
    except error.URLError as e:
        exit(str(e.reason) + '\n Please make sure the server address is correct and try again')


fp, mybytes = request_open()

# parse text into XML document
xmlstr = mybytes.decode('utf8')
root = XML(xmlstr)


# calculate the bandwidth
def bandwidth():
    session_arr = []
    for item in root.findall('./Video/Session'):
        session_arr.append(item.attrib['bandwidth'])
    res = [float(i) for i in session_arr]
    calc = str(round(sum(res) * 0.001, 1)) + ' Mb/s' \
        if round(sum(res) * 0.001, 1) > 1 else str(round(sum(res), 1)) + ' Kb/s'
    return calc if float(calc[:1]) > 0 else None


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
print(white + 'CURRENT ' + yellow + 'PLEX ' + white + 'SESSIONS' + reset)
sessionNum = len(sessions)
if bandwidth():
    print(white + 'Estimated bandwidth usage: ' + bandwidth() + reset)
if sessionNum == 1:
    print(white + 'Currently, ' + green + str(sessionNum) + white + ' user is in a session:' + reset)
else:
    print(white + 'Currently, ' + red + '0' + white + ' users are in a session.' + reset
          if not sessions else
          white + 'Currently, ' + green + str(sessionNum) + white + ' users are in a session.' + reset)

for session in sessions:
    if session['Type'] == 'episode':
        print(
            white + f'- {session["User"]} is watching "{session["Series"]} - '
                    f'S{session["Season"]}E{session["Episode"]} '
                    f'- {session["Title"]}" on {session["Player"]} in {session["Media"]}'
            + reset if search('[a-zA-Z]', session["Media"]) else white + f'- {session["User"]} is watching '
                                                                         f'"{session["Series"]} - S{session["Season"]} '
                                                                         f'E{session["Episode"]} - '
                                                                         f'{session["Title"]}" on {session["Player"]} '
                                                                         f'in {session["Media"]}p' + reset)
    else:
        print(
            white + f'- {session["User"]} is watching "{session["Title"]}" on {session["Player"]} in {session["Media"]}'
            + reset if search('[a-zA-Z]', session["Media"]) else white + f'- {session["User"]} is watching '
                                                                         f'"{session["Title"]}" on {session["Player"]} '
                                                                         f'in {session["Media"]}p' + reset)