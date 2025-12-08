# Docker Basics

Make sure docker is installed.

```bash
docker system ps
```

![Screenshot 2025-12-04 at 8.27.44 AM.png](images/Screenshot_2025-12-04_at_8.27.44_AM.png)

Check the available images

![Screenshot 2025-12-04 at 8.30.31 AM.png](images/Screenshot_2025-12-04_at_8.30.31_AM.png)

Remove images

```bash
docker rmi <image_name>
```

Pull image

```bash
docker pull nginx
```

This will pull the nginx with latest tag.

Docker run

```bash
docker run --name not-nginx -p 81:80 -d httpd
```

since httpd:latest is not available locally, it will pull from the remote repo.

![Screenshot 2025-12-04 at 8.44.30 AM.png](images/Screenshot_2025-12-04_at_8.44.30_AM.png)

![Screenshot 2025-12-04 at 8.46.10 AM.png](images/Screenshot_2025-12-04_at_8.46.10_AM.png)

Changing the default index.html

/usr/local/apache2/htdocs/index.html  is the default root dir for Apache

edit that file to see the changes.

```bash
echo "Hello World" > index.html

docker cp index.html not-nginx:/usr/local/apache2/htdocs/index.html
```

Container name: `not-nginx` 

File location inside container: `/usr/local/apache2/htdocs/index.html` 

![Screenshot 2025-12-04 at 8.54.39 AM.png](images/Screenshot_2025-12-04_at_8.54.39_AM.png)

OR we can also use

```bash
docker exec -it <container_name> bash

docker exec -it not-nginx bash

# We will be logged in as root inside the container's file system.
# We can just go to /htdocs/index.html
# do echo "hello world!" > index.html
```

## How to make persistent content?

→ Volume mount binding

make a dir → cd into the dir → create index.html → run the code below

the ./ means current dir

```bash
docker run --name not-nginx -p 81:80 -d -v "./index.html:/usr/local/apache2/htdocs/index.html" httpd
```

![Screenshot 2025-12-04 at 9.19.59 AM.png](images/Screenshot_2025-12-04_at_9.19.59_AM.png)

→ docker-compose.yml (the best way)

make sure that you are inside the same dir where index.html is present

```bash
services:
  not-nginx:
    image: httpd
    container_name: not-nginx
    ports:
      -"81:80"
    volumes:
      -./index.html:/usr/local/apache2/htdocs/index.html
```

Starting the container

```bash
docker compose up -d
```

![Screenshot 2025-12-04 at 9.33.06 AM.png](images/Screenshot_2025-12-04_at_9.33.06_AM.png)

Stopping the container and removing it

```bash
docker compose down
```

![Screenshot 2025-12-04 at 9.48.39 AM.png](images/Screenshot_2025-12-04_at_9.48.39_AM.png)

Lets build docker image

Create Dockerfile

```docker
FROM nginx:latest

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 81
```

Building the image using Dockerfile

```bash
docker build -t nginx:again . 
```

![Screenshot 2025-12-04 at 10.08.28 AM.png](images/Screenshot_2025-12-04_at_10.08.28_AM.png)

Run the image

```bash
docker run --name not-nginx -p 80:80 -d nginx:again
```

![Screenshot 2025-12-04 at 10.13.32 AM.png](images/Screenshot_2025-12-04_at_10.13.32_AM.png)