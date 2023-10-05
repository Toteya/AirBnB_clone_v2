#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static

# Install nginx on the machine
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
service nginx start

# Create resource directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create test/fake HTML file
echo 'Welcome to Web_static' > /data/web_static/releases/test/index.html

# Create a symbolic link to the '/data/web_static/releases/test/' folder
# Delete and recreate if it already exists
LINK='/data/web_static/current'
TARGET='/data/web_static/releases/test/'
if test "$LINK"; then
	rm "$LINK"
fi
ln -s "$TARGET" "$LINK"

# Change owner and group of the /data/ directory to 'ubuntu'
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to server the content of /data/web_static/current/
# to hbnb_static
FILE="/etc/nginx/sites-available/default"
if ! test -f "$FILE.bak"; then
	cp "$FILE" "$FILE.bak"
fi


CONFIG_TEXT="
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name nyandi.tech;

	add_header X-Served-By \$hostname;

	rewrite ^/redirect_me/$ http://nyandi.tech permanent;
	
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}

	error_page 404 /custom_404.html;
	location = /custom_404.html {
		root /usr/share/nginx/html;
		internal;
	}
}
"

echo "$CONFIG_TEXT" > "$FILE"
nginx -s reload
service nginx restart
