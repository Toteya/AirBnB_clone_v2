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
FILE="/etc/nginx/nginx.conf"
if ! test -f "$FILE.bak"; then
	cp "$FILE" "$FILE.bak"
fi

CONFIG_TEXT="user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	##
	# Basic Settings
	##
	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;
	# server_tokens off;
	
	server {
		location /hbnb_static/ {
			alias /data/web_static/current/hbnb_static/;
		}
	}

	# server_names_hash_bucket_size 64;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# SSL Settings
	##
	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dro    pping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;
	
	##
	# Logging Settings
	##
	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	##
	# Gzip Settings
	##
	gzip on;

	# gzip_vary on;
	# gzip_proxied any;
	# gzip_comp_level 6;
	# gzip_buffers 16 8k;
	# gzip_http_version 1.1;
	# gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
	##
	# Virtual Host Configs
	##
	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}
"
echo "$CONFIG_TEXT" > "$FILE"
nginx -s reload
service nginx restart
