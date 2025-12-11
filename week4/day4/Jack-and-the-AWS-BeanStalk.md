# Jack and the AWS BeanStalk

Open ElasticBean Stalk in AWS console

→ Create Application

![Screenshot 2025-12-11 at 5.51.32 PM.png](images/Screenshot_2025-12-11_at_5.51.32_PM.png)

Configure the environment

→ Add app name

→ Add domain name

![Screenshot 2025-12-11 at 5.52.29 PM.png](images/Screenshot_2025-12-11_at_5.52.29_PM.png)

Choose the platform

Add the code

→ Make sure that app is zipped

![Screenshot 2025-12-11 at 6.36.27 PM.png](images/Screenshot_2025-12-11_at_6.36.27_PM.png)

Single instance cause its free tier

![Screenshot 2025-12-11 at 5.58.21 PM.png](images/Screenshot_2025-12-11_at_5.58.21_PM.png)

Select roles

and Key pair (optional)

![Screenshot 2025-12-11 at 6.04.02 PM.png](images/Screenshot_2025-12-11_at_6.04.02_PM.png)

Select the default VPC or create your own

Select the required subnets

Leaving The db section empty

![Screenshot 2025-12-11 at 6.05.08 PM.png](images/Screenshot_2025-12-11_at_6.05.08_PM.png)

Root Volume → General Purpose SSD

SG → default sg

Leave everything as default

![Screenshot 2025-12-11 at 6.30.30 PM.png](images/Screenshot_2025-12-11_at_6.30.30_PM.png)

Small Changes.

![Screenshot 2025-12-11 at 6.17.39 PM.png](images/Screenshot_2025-12-11_at_6.17.39_PM.png)

![Screenshot 2025-12-11 at 6.17.50 PM.png](images/Screenshot_2025-12-11_at_6.17.50_PM.png)

It works!

![Screenshot 2025-12-11 at 9.29.04 PM.png](images/Screenshot_2025-12-11_at_9.29.04_PM.png)

## Changing the version

Edited the index.html to show “*Version:2.0.0.0”*

![Screenshot 2025-12-11 at 9.35.00 PM.png](images/Screenshot_2025-12-11_at_9.35.00_PM.png)

Compress and deploy again

![Screenshot 2025-12-11 at 6.48.15 PM.png](images/Screenshot_2025-12-11_at_6.48.15_PM.png)

![Screenshot 2025-12-11 at 9.35.18 PM.png](images/Screenshot_2025-12-11_at_9.35.18_PM.png)

To Rollback to previous versions

Elastic Beanstalk → Applications → my-bean-web → Application versions

![Screenshot 2025-12-11 at 7.02.36 PM.png](images/Screenshot_2025-12-11_at_7.02.36_PM.png)

Select the version to rollback to and click on deploy

![Screenshot 2025-12-11 at 7.04.11 PM.png](images/Screenshot_2025-12-11_at_7.04.11_PM.png)

The version goes back to the first one.

![Screenshot 2025-12-11 at 9.27.33 PM.png](images/Screenshot_2025-12-11_at_9.27.33_PM.png)