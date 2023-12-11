# Working with docker images

This README file describes basics of working with custom images:
how to write a `Dockerfile`, how to build and publish to the Docker Hub.

## Specify image
See `Dockerfile` in this directory to understand how Docker images are built.

## Build an image

To build an image use command:

    docker build -t org-name/image-name:tag-name .

It is a good convention to additionally label a newly built image with the
`latest` tag:

    docker tag org-name/image-name:tag-name org-name/image-name:latest

## Publish an image to Docker Hub

First, login to the Docker Hub from the terminal:

     docker login

where your login and password to the Hub will be asked.

Then push both the newly built image with the `tag-name` and the `latest` tag
also:

    docker push org-name/image-name:tag-name
    docker push org-name/image-name:latest
