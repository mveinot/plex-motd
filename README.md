# plex-motd
Display current Plex sessions in Ubuntu MOTD output

# Installation

- **You will need Python 3.5 or later** - it may (probably will) work with Python 3 or later, but I haven't tested it.

- Run `pip3 install -r requirements.txt` to install the required Python packages.

- Edit `server` and `port` if they are different than the defaults.

- Once you have edited the script and confirmed it is working, copy it to `/etc/update-motd.d/` with an appropriate name - (`95-plex` is recommended)

- Move the file `plex_token.py` in the `/etc/update-motd.d/` directory.

- Replace `YOUR_TOKEN_HERE` with your X-Plex-Token string obtained from your server. **Ensure this file is not executable**.

![alt text](https://raw.githubusercontent.com/ejach/plex-motd/patch-1/README/1.PNG)
