# Webmin

[https://webmin.com/download/](https://webmin.com/download/)

Webmin is a web-based control panel for system administrators to manage Unix-like servers, such as Linux and FreeBSD.

It provides a graphical, browser-based interface for tasks that are typically performed using the command line, such as creating user accounts, configuring services like Apache and BIND, managing software packages, and monitoring system performance. 

This makes server management easier, especially for users who are not familiar with all 
the command-line syntax.

```bash
sudo apt update

sudo apt upgrade
```

```bash
curl -o webmin-setup-repo.sh https://raw.githubusercontent.com/webmin/webmin/master/webmin-setup-repo.sh

sudo sh webmin-setup-repo.sh
```

![Screenshot 2025-12-01 at 12.39.50 PM.png](images/Screenshot_2025-12-01_at_12.39.50_PM.png)

```bash
sudo apt-get install webmin --install-recommends
```

```bash
systemctl status webmin.service
```

![Screenshot 2025-12-01 at 12.42.31 PM.png](images/Screenshot_2025-12-01_at_12.42.31_PM.png)

Use the ip and port 10000

192.168.64.3:10000

use the ubuntu username and password with root privs

![Screenshot 2025-12-01 at 12.43.35 PM.png](images/Screenshot_2025-12-01_at_12.43.35_PM.png)

![Screenshot 2025-12-01 at 12.44.58 PM.png](images/Screenshot_2025-12-01_at_12.44.58_PM.png)