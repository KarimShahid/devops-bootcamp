# Docker Assignment

<aside>
📌

## TASK

Pull a NGINX or httpd container.

Browse the default page in [http://localhost](http://localhost/)

Alter the default content.

Stop and start the container again and check if the content persists.

Remove the container and spin it again and check the persistence again.

If content does not persist, try different ways to make it persistence.

</aside>



Pre-requisites

- Docker should be installed
- Should have account in docker hub

Pulling nginx image from Docker Hub

```docker
docker pull nginx:trixie-perl
```

![Screenshot 2025-12-03 at 6.07.59 PM.png](images/Screenshot_2025-12-03_at_6.07.59_PM.png)

![Screenshot 2025-12-03 at 6.09.52 PM.png](images/Screenshot_2025-12-03_at_6.09.52_PM.png)

To see the images created

```docker
docker images
```

![Screenshot 2025-12-03 at 6.10.20 PM.png](images/Screenshot_2025-12-03_at_6.10.20_PM.png)

Creating container and running the image

```docker
docker run --name my-nginx -p 80:80 -d nginx:trixie-perl
```

- `-name my-nginx` → container name
- `-p 80:80` → map container port 80 to host port 80
- `d` → run in detached mode
- `nginx:trixie-perl` → name of image (the tag has to be mentioned)

![Screenshot 2025-12-03 at 6.15.44 PM.png](images/Screenshot_2025-12-03_at_6.15.44_PM.png)

![Screenshot 2025-12-03 at 6.17.39 PM.png](images/Screenshot_2025-12-03_at_6.17.39_PM.png)

Alter the default content

Open a bash shell inside the nginx container

```docker
docker exec -it my-nginx bash
```

![Screenshot 2025-12-03 at 6.51.58 PM.png](images/Screenshot_2025-12-03_at_6.51.58_PM.png)

Nginx serves its default page from /usr/share/nginx/html/index.html

Editing this file will bring changes to the default page.

Stopping and starting nginx container

```docker
docker stop my-nginx

docker start my-nginx
```

![Screenshot 2025-12-03 at 6.56.44 PM.png](images/Screenshot_2025-12-03_at_6.56.44_PM.png)

![Screenshot 2025-12-03 at 6.55.10 PM.png](images/Screenshot_2025-12-03_at_6.55.10_PM.png)

Remove the container and spin it again

```docker
docker rm -f my-nginx

docker ps
```

![Screenshot 2025-12-03 at 7.09.38 PM.png](images/Screenshot_2025-12-03_at_7.09.38_PM.png)

![Screenshot 2025-12-03 at 7.10.09 PM.png](images/Screenshot_2025-12-03_at_7.10.09_PM.png)

```docker
docker run --name my-nginx -p 80:80 -d nginx:trixie-perl

docker ps
```

![Screenshot 2025-12-03 at 7.11.05 PM.png](images/Screenshot_2025-12-03_at_7.11.05_PM.png)

![Screenshot 2025-12-03 at 7.10.53 PM.png](images/Screenshot_2025-12-03_at_7.10.53_PM.png)

My content has changed

![Screenshot 2025-12-03 at 7.11.50 PM.png](images/Screenshot_2025-12-03_at_7.11.50_PM.png)

The /usr/share/nginx/html/index.html file has returned to default.

![Screenshot 2025-12-03 at 7.13.06 PM.png](images/Screenshot_2025-12-03_at_7.13.06_PM.png)

Create volume to make data persistent

```docker
docker volume create nginx-data
```

![Screenshot 2025-12-03 at 7.31.57 PM.png](images/Screenshot_2025-12-03_at_7.31.57_PM.png)

Mount the volume to the container

```bash
docker run -d -p 80:80 --name my-nginx -v nginx-data:/usr/share/nginx/html nginx:trixie-perl
```

**`v`** → Stands for **volume**.

- It tells Docker: “Mount some storage into the container.”

**`nginx-data`** → This is the **name of the volume**.

- It can be an **existing named volume**, or Docker will **create it automatically** if it doesn’t exist.

**`/usr/share/nginx/html`**→ This is the **path inside the container** where the volume will be mounted.

- For NGINX, this is the **default folder for web content** (the default `index.html` lives here).

Anything written to `/usr/share/nginx/html` inside the container is actually stored in the **volume `nginx-data`**.

<aside>
📌

This means:

- Changes **persist** even if the container is removed.
- You can reuse the same volume with a new container to keep the website content.
</aside>

Editing the index.html 

```bash
docker exec -it my-nginx bash
cd /usr/share/nginx/html
echo "Ive written this message with a permanent pen!" > index.html
exit
```

![Screenshot 2025-12-03 at 8.12.19 PM.png](images/Screenshot_2025-12-03_at_8.12.19_PM.png)

![Screenshot 2025-12-03 at 8.13.27 PM.png](images/Screenshot_2025-12-03_at_8.13.27_PM.png)

Stopping the container, removing it and again running it

```bash
docker stop my-nginx

docker rm -f my-nginx
```

![Screenshot 2025-12-03 at 8.16.06 PM.png](images/Screenshot_2025-12-03_at_8.16.06_PM.png)

No containers are found

![Screenshot 2025-12-03 at 8.16.40 PM.png](images/Screenshot_2025-12-03_at_8.16.40_PM.png)

Running a container

```bash
docker run -d -p 80:80 --name my-nginx -v nginx-data:/usr/share/nginx/html nginx:trixie-perl
```

![Screenshot 2025-12-03 at 8.17.17 PM.png](images/Screenshot_2025-12-03_at_8.17.17_PM.png)

The data has persisted.

![Screenshot 2025-12-03 at 8.17.32 PM.png](images/Screenshot_2025-12-03_at_8.17.32_PM.png)