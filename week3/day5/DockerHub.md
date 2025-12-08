# Docker Hub

Create account → match with Docker Desktop

Login

Create repo

![Screenshot 2025-12-05 at 8.35.25 AM.png](images/Screenshot_2025-12-05_at_8.35.25_AM.png)

Login

```bash
docker login
```

Creating Docker Hub Repo

```bash
docker tag <local_image_name> <Username>/<repo_name>:<tag>

docker tag httpd karimshahid/karim-adex-devops
```

![Screenshot 2025-12-05 at 8.59.36 AM.png](images/Screenshot_2025-12-05_at_8.59.36_AM.png)

Push to DockerHub

```bash
docker push <username>/<Repo_name>:<tag>

docker push karimshahid/karim-adex-devops
```

![Screenshot 2025-12-05 at 9.01.43 AM.png](images/Screenshot_2025-12-05_at_9.01.43_AM.png)

Pulling someones image

Since im running ARM64 and the image is AMD64, we need to change the platform with pulling it.

```bash
docker pull --platform linux/amd64 yshakya/adex-devops
```

Running container

```bash
docker run --platform linux/amd64 -p 81:80 -d yshakya/adex-devops
```

![Screenshot 2025-12-05 at 9.19.24 AM.png](images/Screenshot_2025-12-05_at_9.19.24_AM.png)

Best practise

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t <you>/<image>:latest --push .
docker compose up
```