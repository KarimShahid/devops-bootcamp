# Weekend Task2

Your teammate always asks “What is the IP of this server?” so please create a bash script as

[myip.sh] myip.sh which shows only the private and public IP in a pretty way.

Create a bash script

```bash
nano myip.sh
```

```bash
#!/bin/bash

# Colors
RED="\e[31m"
GREEN="\e[32m"
CYAN="\e[36m"
NC="\e[0m" # No color

# Clear screen
clear

echo -e "${CYAN}=== SERVER IP INFORMATION ===${NC}"

# Private IP (from hostname or ip command)
PRIVATE_IP=$(hostname -I | awk '{print $1}')
echo -e "${GREEN}Private IP: ${NC}${PRIVATE_IP}"

# Public IP (from external service)
PUBLIC_IP=$(curl ifconfig.me)   
echo -e "${RED}Public IP: ${NC}${PUBLIC_IP}"

echo
```

Make [myip.sh] myip.sh executable

```bash
chmod +x myip.sh
```

![Screenshot 2025-11-23 at 1.30.54 PM.png](images/Screenshot_2025-11-23_at_1.30.54_PM.png)