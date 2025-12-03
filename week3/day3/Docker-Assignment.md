# Docker Assignment: NGINX Container with Persistent Data

<aside>
📌

## TASK

- Pull a NGINX or httpd container.
- Browse the default page at [http://localhost](http://localhost/).
- Modify the default content.
- Stop and start the container and check if the changes persist.
- Remove the container and spin it up again to verify persistence.
- If content does not persist, explore ways to make it persistent.

</aside>

## Prerequisites

- Docker must be installed.
- Docker Hub account is required.

---

## 1. Pull NGINX Image

```bash
docker pull nginx:trixie-perl
```

![Screenshot 2025-12-03 at 6.07.59 PM.png](images/Screenshot_2025-12-03_at_6.07.59_PM.png)
![Screenshot 2025-12-03 at 6.09.52 PM.png](images/Screenshot_2025-12-03_at_6.09.52_PM.png)

Check downloaded images:

```bash
docker images
```

![Screenshot 2025-12-03 at 6.10.20 PM.png](images/Screenshot_2025-12-03_at_6.10.20_PM.png)

---

## 2. Create and Run Container

```bash
docker run --name my-nginx -p 80:80 -d nginx:trixie-perl
```

- `--name my-nginx` → assigns a name to the container
- `-p 80:80` → maps container port 80 to host port 80
- `-d` → runs container in detached mode
- `nginx:trixie-perl` → specifies the image and tag

![Screenshot 2025-12-03 at 6.15.44 PM.png](images/Screenshot_2025-12-03_at_6.15.44_PM.png)
![Screenshot 2025-12-03 at 6.17.39 PM.png](images/Screenshot_2025-12-03_at_6.17.39_PM.png)

---

## 3. Modify Default Content

Open a shell in the container:

```bash
docker exec -it my-nginx bash
```

![Screenshot 2025-12-03 at 6.51.58 PM.png](images/Screenshot_2025-12-03_at_6.51.58_PM.png)

Default NGINX page path:

```
/usr/share/nginx/html/index.html
```

Edit this file to modify the default page.

---

## 4. Stop and Start Container

```bash
docker stop my-nginx
docker start my-nginx
```

![Screenshot 2025-12-03 at 6.56.44 PM.png](images/Screenshot_2025-12-03_at_6.56.44_PM.png)
![Screenshot 2025-12-03 at 6.55.10 PM.png](images/Screenshot_2025-12-03_at_6.55.10_PM.png)

Without a volume, changes do not persist.

---

## 5. Remove Container and Create Again

```bash
docker rm -f my-nginx
docker ps
```

![Screenshot 2025-12-03 at 7.09.38 PM.png](images/Screenshot_2025-12-03_at_7.09.38_PM.png)
![Screenshot 2025-12-03 at 7.10.09 PM.png](images/Screenshot_2025-12-03_at_7.10.09_PM.png)

Run new container:

```bash
docker run --name my-nginx -p 80:80 -d nginx:trixie-perl
docker ps
```

![Screenshot 2025-12-03 at 7.11.05 PM.png](images/Screenshot_2025-12-03_at_7.11.05_PM.png)
![Screenshot 2025-12-03 at 7.10.53 PM.png](images/Screenshot_2025-12-03_at_7.10.53_PM.png)

Default content is restored.

![Screenshot 2025-12-03 at 7.11.50 PM.png](images/Screenshot_2025-12-03_at_7.11.50_PM.png)
![Screenshot 2025-12-03 at 7.13.06 PM.png](images/Screenshot_2025-12-03_at_7.13.06_PM.png)

---

## 6. Make Data Persistent Using Docker Volume

### Create Volume

```bash
docker volume create nginx-data
```

![Screenshot 2025-12-03 at 7.31.57 PM.png](images/Screenshot_2025-12-03_at_7.31.57_PM.png)

### Run Container with Volume

```bash
docker run -d -p 80:80 --name my-nginx -v nginx-data:/usr/share/nginx/html nginx:trixie-perl
```

- `-v` → mounts storage into the container
- `nginx-data` → name of the volume
- `/usr/share/nginx/html` → container path for web content

> Any changes made here are stored in `nginx-data` and persist across container removal.

---

## 7. Edit index.html in Volume

```bash
docker exec -it my-nginx bash
cd /usr/share/nginx/html
echo "I've written this message with a permanent pen!" > index.html
exit
```

![Screenshot 2025-12-03 at 8.12.19 PM.png](images/Screenshot_2025-12-03_at_8.12.19_PM.png)
![Screenshot 2025-12-03 at 8.13.27 PM.png](images/Screenshot_2025-12-03_at_8.13.27_PM.png)

---

## 8. Stop, Remove, and Run Again

```bash
docker stop my-nginx
docker rm -f my-nginx
docker run -d -p 80:80 --name my-nginx -v nginx-data:/usr/share/nginx/html nginx:trixie-perl
```

![Screenshot 2025-12-03 at 8.17.17 PM.png](images/Screenshot_2025-12-03_at_8.17.17_PM.png)
![Screenshot 2025-12-03 at 8.17.32 PM.png](images/Screenshot_2025-12-03_at_8.17.32_PM.png)

Your changes persist because they are stored in the Docker volume.

---

## ✅ Key Takeaways

- Mounting a volume overrides the container's folder.
- Named volumes copy default container content when first created.
- Changes inside the mounted volume persist even if the container is removed.
- The same volume can be reused for new containers to maintain content.

