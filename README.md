# plex-motd
Display current Plex sessions in Ubuntu MOTD output

Edit `plex-motd.py` and set the X-Plex-Token to the token from your server.
Additionally, edit `server` and `port` if they are different than the defaults.

You will need Python 3 or later.

Once you have edited the script and confirmed it is working, copy it to `/etc/update-motd.d/` with an appropriate name - `95-plex` is recommended.
