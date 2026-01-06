# Jenkins: Static Web App CICD

![image.png](images/image.png)

## Objectives

- Push code to **GitHub**
- **Jenkins** detects the push
- Jenkins copies files to **EC2 Server (ubuntu)**
- Files are served by **Nginx**

## Create a simple static site

![Screenshot 2026-01-05 at 6.42.44 PM.png](images/Screenshot_2026-01-05_at_6.42.44_PM.png)

## Push to github

![Screenshot 2026-01-05 at 6.43.04 PM.png](images/Screenshot_2026-01-05_at_6.43.04_PM.png)

## Create EC2 server

![Screenshot 2026-01-05 at 6.49.08 PM.png](images/Screenshot_2026-01-05_at_6.49.08_PM.png)

## Install nginx in the server

ssh in the server

```bash
sudo apt update
sudo apt install -y nginx
```

![Screenshot 2026-01-05 at 6.48.36 PM.png](images/Screenshot_2026-01-05_at_6.48.36_PM.png)

## Configuring EC2

### Editing the dir permission

```bash
chown -R ubuntu:ubuntu /var/www/html
```

![Screenshot 2026-01-05 at 7.05.12 PM.png](images/Screenshot_2026-01-05_at_7.05.12_PM.png)

### Git Clone

```bash
git clone https://github.com/KarimShahid/nba_memes_jenkins.git .
```

![Screenshot 2026-01-05 at 7.08.58 PM.png](images/Screenshot_2026-01-05_at_7.08.58_PM.png)

## Jenkins

### deploy.groovy

```groovy
pipeline {
    agent any

    parameters {
        string(
            name: 'SERVER_IP',
            defaultValue: '3.237.6.29',
            description: 'EC2 public IP'
        )
    }

    environment {
        SSH_KEY64 = credentials('SSH_KEY64')
    }

    stages {
        stage('Configure SSH') {
            steps {
                sh '''
                mkdir -p ~/.ssh
                chmod 700 ~/.ssh
                printf "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config  
                cat ~/.ssh/config   #to verify
                touch ~/.ssh/known_hosts
                chmod 600 ~/.ssh/known_hosts
                '''
            }
        }

        stage('Prepare SSH Key') {
            steps {
                sh """
                touch mykey.pem
                echo "$SSH_KEY64" | base64 -d > mykey.pem && chmod 400 mykey.pem
                ssh-keygen -R ${params.SERVER_IP} 
                """
            }
        }

        stage('Deploy') {
            steps {
                sh """
                ssh -i mykey.pem ubuntu@${SERVER_IP} 'cd /var/www/html && git pull origin main'
                """
            }
        }
    }

    post {
        always {
            sh 'rm -f mykey.pem'
        }
        success {
            echo "✅ Deployment completed successfully"
        }
        failure {
            echo "❌ Deployment failed"
        }
    }
}

```

### Create new item: nba_memes

select pipeline

![Screenshot 2026-01-05 at 7.25.18 PM.png](images/Screenshot_2026-01-05_at_7.25.18_PM.png)

### Parameterize

![Screenshot 2026-01-05 at 7.34.29 PM.png](images/Screenshot_2026-01-05_at_7.34.29_PM.png)

### Configuring Pipeline

Add git repo

![Screenshot 2026-01-05 at 7.26.21 PM.png](images/Screenshot_2026-01-05_at_7.26.21_PM.png)

Add branch name

Add Script path mentioned in the repo

![Screenshot 2026-01-05 at 7.26.33 PM.png](images/Screenshot_2026-01-05_at_7.26.33_PM.png)

### Create SSH_KEY64 credential

![Screenshot 2026-01-05 at 7.29.00 PM.png](images/Screenshot_2026-01-05_at_7.29.00_PM.png)

### Make changes to the file and push to git

![Screenshot 2026-01-05 at 7.38.14 PM.png](images/Screenshot_2026-01-05_at_7.38.14_PM.png)

### Run the workflow

![Screenshot 2026-01-05 at 7.35.53 PM.png](images/Screenshot_2026-01-05_at_7.35.53_PM.png)

## Output!

![Screenshot 2026-01-05 at 7.38.57 PM.png](images/Screenshot_2026-01-05_at_7.38.57_PM.png)