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

Setting port forwarding

![Screenshot 2025-12-02 at 1.06.37 PM.png](images/Screenshot_2025-12-02_at_1.06.37_PM.png)

Since Host Port for SSH is set at 2222, with [localhost](http://localhost) as host address, we have to do ssh this way

```yaml
ssh -p 2222 <username>:localhost
```

![Screenshot 2025-12-02 at 1.09.46 PM.png](images/Screenshot_2025-12-02_at_1.09.46_PM.png)

To connect to the webmin page, use [localhost:10000](http://localhost:10000) (as we have done port mapping)

Use the ubuntu username and password with root privs

![Screenshot 2025-12-02 at 1.13.08 PM.png](images/Screenshot_2025-12-02_at_1.13.08_PM.png)

![Screenshot 2025-12-02 at 1.12.30 PM.png](images/Screenshot_2025-12-02_at_1.12.30_PM.png)