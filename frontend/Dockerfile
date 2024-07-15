FROM nginx:latest

COPY index.html /usr/share/nginx/html/index.html
# COPY styles.css /usr/share/nginx/html/styles.css

# copy the custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf


EXPOSE 80
