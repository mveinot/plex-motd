# plex-motd
Display current Plex sessions in Ubuntu MOTD output

Additionally, edit `server` and `port` if they are different than the defaults.

You will need Python 3.5 or later - it may (probably will) work with Python 3 or later, but I haven't tested it.

Once you have edited the script and confirmed it is working, copy it to `/etc/update-motd.d/` with an appropriate name - `95-plex` is recommended.
Additionally create a file called `plex_token.py` in the `/etc/update-motd.d/` directory with a single line:

```
plex_token = 'YOUR_TOKEN_HERE'
```

Replacing `YOUR_TOKEN_HERE` with your X-Plex-Token string obtained from your server. Ensure this file is not executable.

Before:

![alt text](https://raw.githubusercontent.com/mveinot/plex-motd/master/README/plex-motd.png)

After:

![alt text](https://raw.githubusercontent.com/ejach/plex-motd/patch-1/README/1.PNG)
