# Weekend Task3

Write `harden.sh` that applies basic security best practices:

- Disables root login via SSH
- Changes SSH port
- Installs and configures fail2ban
- Disables unused services
- Sets up basic firewall rules (ufw or firewalld)
- Creates a report of what was changed

```bash
nano harden.sh
```

```bash
#!/bin/bash

# =====================================================
# Harden.sh - Basic Server Hardening Script
# Applies SSH hardening, fail2ban, firewall rules, and disables unused services
# Generates a report of changes
# =====================================================

if [ $EUID -ne 0 ]; then
    echo "Please run as root: sudo $0"
    exit 1
fi

REPORT="harden_report_$(date).txt"
echo "Server Hardening Report - $(date)" > "$REPORT"
echo "=====================================" >> "$REPORT"

# Function to log changes
log_change() {
    echo "$1" | tee -a "$REPORT"
}

#1 Check if the line is exactly "#PermitRootLogin no"
if grep -q "^PermitRootLogin no" /etc/ssh/sshd_config; then
    log_change "Root login is already disabled."
else
    sed -i 's/^#*PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
    log_change "Disabled root login via SSH."
fi

#2
sed -i 's/^#*Port.*/Port 2222/' /etc/ssh/sshd_config
log_change "SSH port changed to 2222."
systemctl restart ssh
log_change "SSH service restarted."

 #3. Install and configure fail2ban
apt update >/dev/null 2>&1  && apt install -y fail2ban >/dev/null 2>&1
log_change "Installed fail2ban."

cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

# Configure basic SSH jail
cat > /etc/fail2ban/jail.local <<EOL
[sshd]
enabled = true
port = 2222
filter = sshd
logpath = /var/log/auth.log
maxretry = 5
bantime = 3600
EOL
systemctl restart fail2ban
log_change "Configured fail2ban for SSH and restarted service."

#4. 
# Only disable these well-known unnecessary services 
UNUSED_SERVICES=( avahi-daemon cups bluetooth rpcbind snapd postfix nginx apache2 ) 
for svc in "${UNUSED_SERVICES[@]}"; do 
if systemctl is-enabled --quiet "$svc" 2>/dev/null; then 
systemctl disable --now "$svc" 2>/dev/null 
log_change "Disabled unnecessary service: $svc" 
fi 
done

# 5. Set up basic firewall rules (ufw)
apt install -y ufw >/dev/null 2>&1
ufw default deny incoming
ufw default allow outgoing
ufw allow 2222/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw --force enable
ufw reload
systemctl restart ssh
log_change "Configured UFW firewall with basic rules and enabled it."

6.
echo "" >> "$REPORT"
echo "HARDENING COMPLETE. Review changes above." >> "$REPORT"
echo "Report saved to: $REPORT"
echo ""
echo "====================================="
cat "$REPORT"

```

Fail2Ban is an open-source intrusion prevention software that scans server log files for malicious patterns, such as repeated failed login attempts, and automatically blocks the offending IP addresses by updating firewall rules.

How it works

- **Monitors logs**: Fail2Ban reads log files (like `/var/log/auth.log`) and uses regular expressions to find patterns of repeated failures or other malicious behaviors.
- **Bans IPs**: When a predefined number of failures (e.g., 5) from a single IP address occurs within a set time (e.g., 10 minutes), it executes an action,
most commonly updating firewall rules (like `iptables`) to block that IP from accessing the server.
- **Unbans IPs**: The ban is temporary, with the duration configurable. After the ban
time expires, the IP is unblocked, allowing legitimate users to
reconnect.
- **Customizable**: Fail2Ban is highly configurable, allowing administrators to set the
number of retries, ban times, and which logs and services to monitor. It can also be configured to perform other actions, like sending an email
to the administrator

In Linux, an "unused service" is a background process (daemon) or system unit that is running or enabled to start automatically but does not provide a function needed for the system's current role or the user's requirements

![Screenshot 2025-11-23 at 5.18.50 PM.png](images/fcfd1d98-2b3d-40c9-b3a1-0d598515d01b.png)

![Screenshot 2025-11-23 at 5.19.05 PM.png](images/Screenshot_2025-11-23_at_5.19.05_PM.png)

We can do Number 4 like this also, but some services might cause problems if disabled. 

```bash

# 4. Disable unused services (inactive and enabled services)
log_change "Checking for unused services to disable..."
systemctl list-unit-files --type=service | grep enabled | awk '{print $1}' \
| while read services; do
    if ! systemctl is-active --quiet "$services" 2>/dev/null; then
        systemctl disable "$services"
        log_change "Disabled unused service: $services"
    fi
done

```