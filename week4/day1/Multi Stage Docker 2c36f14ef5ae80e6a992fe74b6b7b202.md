# Multi Stage Docker

Basic Project Structure

![Screenshot 2025-12-08 at 8.36.29 PM.png](images/Screenshot_2025-12-08_at_8.36.29_PM.png)

build.js

![Screenshot 2025-12-08 at 8.36.48 PM.png](images/Screenshot_2025-12-08_at_8.36.48_PM.png)

src/template.html

![Screenshot 2025-12-08 at 8.37.09 PM.png](images/Screenshot_2025-12-08_at_8.37.09_PM.png)

package.json

![Screenshot 2025-12-08 at 8.37.21 PM.png](images/Screenshot_2025-12-08_at_8.37.21_PM.png)

Summary:

- This project is a **Node.js static site generator**.
- `build.js` reads a template, replaces placeholders dynamically, and outputs `dist/index.html`.
- The generated HTML can be served as a static file, possibly as part of a **multi-stage Docker build** to produce a lightweight production image.

Create Dockerfile

```bash
FROM node:20-alpine as builder

# ARG APP_VERSION=1.0.0.1
# ENV APP_VERSION=$APP_VERSION

WORKDIR /app

# Copy only package.json first
COPY package*.json ./

# Install deps as root (default)
RUN npm install

# Copy rest of the code
COPY . .

# make sure that dist dir is present
RUN mkdir -p dist

# Run the build script to generate index.html
RUN npm run build

#--------- stage 2 ------------

FROM nginx:stable-alpine

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
```

Edit the .env file

![Screenshot 2025-12-08 at 9.45.42 PM.png](images/c997f3ac-74f7-497b-a615-89e878d4a259.png)

Create the image

```bash
docker build -t my-web:1.0.0.1 .
```

![Screenshot 2025-12-08 at 9.41.41 PM.png](images/Screenshot_2025-12-08_at_9.41.41_PM.png)

Spinning the container

```bash
docker run -p 80:80 -d --name my-web-container my-web:1.0.0.1

```

![Screenshot 2025-12-08 at 9.43.02 PM.png](images/Screenshot_2025-12-08_at_9.43.02_PM.png)

![Screenshot 2025-12-08 at 9.43.24 PM.png](images/Screenshot_2025-12-08_at_9.43.24_PM.png)

Edit the .env file

Since we have edited the .env → its used during the build time so we have to build new image

![Screenshot 2025-12-08 at 9.45.42 PM.png](images/Screenshot_2025-12-08_at_9.45.42_PM.png)

Create new image

![Screenshot 2025-12-08 at 9.46.46 PM.png](images/Screenshot_2025-12-08_at_9.46.46_PM.png)

Spin new container

![Screenshot 2025-12-08 at 9.47.52 PM.png](images/Screenshot_2025-12-08_at_9.47.52_PM.png)

![Screenshot 2025-12-08 at 9.48.04 PM.png](images/Screenshot_2025-12-08_at_9.48.04_PM.png)