# plex-motd
Display current Plex sessions in Ubuntu MOTD output

# Installation

- **You will need Python 3.5 or later** - it may (probably will) work with Python 3 or later, but I haven't tested it.

- Run `pip3 install -r requirements.txt` to install the required Python packages.

- Edit `plex_server` and `plex_port` in the `.env` file if they are different than the defaults.

- Replace `YOUR_TOKEN_HERE` with your X-Plex-Token string obtained from your server.

- Once you have edited the script and the `.env` file and confirmed it is working, copy them to `/etc/update-motd.d/` with an appropriate name - (`95-plex` is recommended) by running

```bash
mv plex_motd.py 95-plex 
mv .env /etc/update-motd.d/
mv 95-plex /etc/update-motd.d/
```

- Make sure the file is executable and will show up on login by running

```bash
chmod +x 95-plex
```

![alt text](https://raw.githubusercontent.com/mveinot/plex-motd/master/README/1.png)
