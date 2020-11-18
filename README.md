# plex-motd
Display current Plex sessions in Ubuntu MOTD output

Edit `plex-motd.py` and set the X-Plex-Token to the token from your server.
Additionally, edit `server` and `port` if they are different than the defaults.

You will need Python 3.5 or later - it may (probably will) work with Python 3 or later, but I haven't tested it.

Once you have edited the script and confirmed it is working, copy it to `/etc/update-motd.d/` with an appropriate name - `95-plex` is recommended.

Before:
![alt text](https://raw.githubusercontent.com/mveinot/plex-motd/master/README/plex-motd.png)

After:

![alt text](https://raw.githubusercontent.com/ejach/plex-motd/master/README/1.png)
