# plex-motd
Display current Plex sessions in Ubuntu MOTD output

# Installation

- **You will need Python 3.5 or later** - it may (probably will) work with Python 3 or later, but I haven't tested it.

- [Export](https://help.ubuntu.com/community/EnvironmentVariables) the following environment variables
```bash
# if your configuration for server/port is different than the defaults, edit them accordingly
server=localhost
port=32400
# Replace 'YOUR_TOKEN_HERE' with your X-Plex-Token string obtained from your server.
plex_token=YOUR_TOKEN_HERE
```

- Once you have edited the script and confirmed it is working, copy it to `/etc/update-motd.d/` with an appropriate name - (`95-plex` is recommended)


![alt text](https://raw.githubusercontent.com/mveinot/plex-motd/master/README/1.png)
