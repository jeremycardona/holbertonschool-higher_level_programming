   # Use the official Alpine image as the base image
   FROM alpine:latest

   # Install Curl
   RUN apk add --no-cache curl

   # Add the config file
   COPY config.txt /config.txt
   # Set the command to be run when the container starts
   CMD ["echo", "Hello, World!"]