sudo cp automation/systemd/forty.service /lib/systemd/system/

systemctl daemon-reload

systemctl enable forty.service
systemctl start forty.service
systemctl status forty.service

sudo chmod 777 /lib/systemd/system/forty.service
