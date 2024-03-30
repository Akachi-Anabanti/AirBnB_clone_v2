#!/usr/bin/env bash
# A cript to setup nginx and for servers

if ! [ -x "$(command -v nginx)" ] ; then
	echo "Installing Nginx";
	sudo apt-get update
	sudo apt-get install -y nginx
else
	echo 'Nginx is already installed.'
fi

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "<html><body><h1>Hello ALX!</h1></body></html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

cp /etc/nginx/sites-available/default{,.bak}

cat << 'EOF' > /etc/nginx/sites-available/default
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
	}

	location /hbnb_static {
		alias /data/web_static/current;
	}
}
EOF

sudo service nginx start
