---
share: true
tags:
  - project
title: Plex_Media_Server
status: DONE
priority: medium
start: 2024-07-10
due: 
completion: 2024-07-10
---

## Install

### Snap Repo

Add the snappy repository

```
sudo zypper addrepo --refresh \
  https://download.opensuse.org/repositories/system:/snappy/openSUSE_Tumbleweed \
  snappy
```

Import GPG key

```
sudo zypper --gpg-auto-import-keys refresh
```

Upgrade the package cache

```
sudo zypper dup --from snappy
```

### Snap

Install snap

```
sudo zypper install snapd
```

Run `source /etc/profile` to have /snap/bin added to PATH.

Start the snapd service

```
sudo systemctl enable --now snapd
```

Enable and start the service

```
sudo systemctl enable --now snapd.apparmor
```

### Plex Media Server

```
sudo snap install plexmediaserver
```

### PPP

`PPP.sh`

```bash
#!/bin/bash
set -e

# Move to the script directory (PPP)
cd "$(dirname "$0")"

# Extract local_playlists path from variables.json
playlist_dir=$(jq -r '.local_playlists' variables.json)

# Check if the directory exists
if [ ! -d "$playlist_dir" ]; then
  echo "Playlist directory not found: $playlist_dir"
  exit 1
fi

echo "Processing .m3u8 files in: $playlist_dir"

# Convert .m3u8 files to .m3 with UTF-8 encoding
for file in "$playlist_dir"/*.m3u8; do
  [ -e "$file" ] || continue  # skip if no files
  base=$(basename "$file" .m3u8)
  target="$playlist_dir/$base.m3u"
  echo "Converting $file → $target"
  iconv -f UTF-8 -t UTF-8 "$file" -o "$target" && rm -f "$file"
done

echo "Preprocessing complete. Running PPP..."
python3 PPP.py
```

`sudo zypper install jq glibc-locale`
`chmod 700 "/home/nugget/Sync/Plex Media Server/PPP/PPP.sh"`

`bash "/home/nugget/Sync/Plex Media Server/PPP/PPP.sh"`

## Moving Plex Media Server to Pi4

[Move an Install to Another System](https://support.plex.tv/articles/201370363-move-an-install-to-another-system/)

1. `sudo apt update`
2. `sudo apt upgrade`
3. `curl https://downloads.plex.tv/plex-keys/PlexSign.key | gpg --dearmor | sudo tee /usr/share/keyrings/plex-archive-keyring.gpg >/dev/null`
4. `echo deb [signed-by=/usr/share/keyrings/plex-archive-keyring.gpg] https://downloads.plex.tv/repo/deb public main | sudo tee /etc/apt/sources.list.d/plexmediaserver.list`
5. `sudo apt update`
6. `sudo apt install plexmediaserver`
7. `sudo service plexmediaserver stop`
8. Stop original server and move all files to hard drive
9. `mkdir /mnt/usb`
10. `sudo nano /etc/fstab`
11. `UUID= /mnt/usb ext4 defaults 0 0`
12. `sudo rm -r "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server"`
13. `sudo ln -s "/mnt/usb/<path_to_custom_library>/Plex Media Server" "/var/lib/plexmediaserver/Library/Application Support/"`
14. `ls -l "/var/lib/plexmediaserver/Library/Application Support"`
15. `sudo reboot`
16. `sudo service plexmediaserver start`
17. [Command Line Loudness Analysis](https://www.reddit.com/r/PleX/comments/yytqdy/forcing_loudness_analysis/), [via cron](https://forums.plex.tv/t/make-media-analysis-stop-wasting-cpu-on-duplicate-repeated-analysis/853275)
