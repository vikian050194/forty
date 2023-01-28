DIR="$HOME/forty"
# rm -rf "$DIR"

systemctl stop forty.service
systemctl disable forty.service

sudo rm automation/systemd/forty.service

systemctl daemon-reload
