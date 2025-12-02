# Assignment day 2: Linux

# TASK 1

![Screenshot 2025-11-18 at 9.42.59 AM.png](Assignment%20day%202%20Linux/Screenshot_2025-11-18_at_9.42.59_AM.png)

Create the directory structure

Navigate to ~**/devops-lab/projects/app1** and create a file called README.md

![Screenshot 2025-11-18 at 9.44.22 AM.png](Assignment%20day%202%20Linux/Screenshot_2025-11-18_at_9.44.22_AM.png)

Copy [README.md](http://README.md) to app2/ dir

![Screenshot 2025-11-18 at 9.45.33 AM.png](Assignment%20day%202%20Linux/Screenshot_2025-11-18_at_9.45.33_AM.png)

List all files in ~**/devops-lab/** recursively ****showing hidden files

![Screenshot 2025-11-18 at 9.49.46 AM.png](Assignment%20day%202%20Linux/Screenshot_2025-11-18_at_9.49.46_AM.png)

# TASK 2

![Screenshot 2025-11-18 at 9.50.04 AM.png](Assignment%20day%202%20Linux/Screenshot_2025-11-18_at_9.50.04_AM.png)

update your package index

![Screenshot 2025-11-18 at 9.54.47 AM.png](Assignment%20day%202%20Linux/Screenshot_2025-11-18_at_9.54.47_AM.png)

Install htop

![Screenshot 2025-11-18 at 10.12.08 AM.png](Assignment%20day%202%20Linux/Screenshot_2025-11-18_at_10.12.08_AM.png)

Check if nginx is installed. If not install

![Screenshot 2025-11-18 at 10.12.29 AM.png](Assignment%20day%202%20Linux/Screenshot_2025-11-18_at_10.12.29_AM.png)

List all currently installed packages and save output to ~/devops-lab/packages.txt

![Screenshot 2025-11-18 at 10.11.13 AM.png](Assignment%20day%202%20Linux/Screenshot_2025-11-18_at_10.11.13_AM.png)

# TASK 3

![image.png](Assignment%20day%202%20Linux/image.png)

1. Deployment frequency 

Deployment frequency measures how often a team successfully releases code to production.

$$
Deployment Frequency (per day) = \frac{\text{Total Deployments in a Month}}{\text{Total Number of Working Days}}
$$

Total Deployments in a Month = 40

Total Number of Working Days = 20

**Deployment Frequency = 40/20 = 2 deployments per day**

2. Lead time for changes

How long it takes from code commit to code running in production.

**Average 3 hours**

3. Change failure rate (%)

Percentage of deployments causing a failure in production.

$$
CFR = \frac{\text{Number of Failed Deployments}}{\text{Total Number of Deployments}} \times 100
$$

Number of Failed Deployments = 6

Total Number of Deployments = 40

**CFR = (6/40) * 100 ⇒ 15%**

4. Mean Time to Recovery

Time it takes to recover from a failure.

$$
MTTR = \frac{\text{Total Repair Time}}{\text{Total Number of Repairs}}
$$

Total Repair Time = 90+45+120+240+30+240 = 765 mins

Total Number of Repairs = 6

**MTTR = 765/6 ⇒ 127.5 mins**

5. Classify the team on DORA metrics

**DORA (DevOps Research and Assessment) metrics:**

- Deployment Frequency = 2/day → Elite (multiple per day)
- Lead Time = 3 hours → Elite (<1 day)
- CFR = 15% → Elite (0–15%)
- MTTR = 127.5 mins ≈ 2 hours 7 mins → High (<1 day)

Since 3/4 metrics are Elite and 1 metric is High, the team can be classified as High-performing (almost Elite, but MTTR slightly higher prevents full Elite status).