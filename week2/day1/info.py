#!/usr/bin/env python3

import os
import subprocess
import datetime
import socket
import platform

# ===== Colors =====
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
NC = "\033[0m"

# Clear screen
os.system("clear")

system = platform.system()

# ===== SERVER INFO =====
print(f"{CYAN}=== SERVER INFO ==={NC}")
print(f"{GREEN}Server Name: {NC}{socket.gethostname()}")

# Uptime (macOS doesn't support uptime -p)
if system == "Darwin":   # macOS
    uptime = subprocess.getoutput("uptime | sed 's/.*up/up/'")
else:
    uptime = subprocess.getoutput("uptime -p")

print(f"{GREEN}Uptime: {NC}{uptime}\n")

# ===== USER & DATE =====
print(f"{CYAN}=== USER & DATE ==={NC}")
current_user = subprocess.getoutput("whoami")
print(f"{YELLOW}Current User: {NC}{current_user}")

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{YELLOW}Date: {NC}{now}\n")

# ===== SYSTEM USAGE =====
print(f"{CYAN}=== SYSTEM USAGE ==={NC}")

# Disk Usage (works on both)
print(f"{MAGENTA}Disk Usage:{NC}")
print(subprocess.getoutput("df -h | awk 'NR==1 || /^\\/dev\\// {print}'"))
print()

# Memory Usage
print(f"{MAGENTA}Memory Usage:{NC}")

if system == "Darwin":  # macOS
    print(subprocess.getoutput("vm_stat"))
else:                   # Linux
    print(subprocess.getoutput("free -h"))

print()

# CPU Usage
print(f"{MAGENTA}CPU Usage:{NC}")

if system == "Darwin":
    # macOS top command is very different → get CPU like this
    cpu = subprocess.getoutput(
        "ps -A -o %cpu | awk '{s+=$1} END {print s}'"
    )
else:
    cpu = subprocess.getoutput(
        "top -bn1 | grep 'Cpu(s)' | awk '{print $2 + $4}'"
    )

print(f"CPU Load: {cpu}%\n")

# ===== NETWORK =====
print(f"{CYAN}=== NETWORK ==={NC}")
external_ip = subprocess.getoutput("curl -s ifconfig.me")
print(f"{GREEN}External IP: {NC}{external_ip}\n")

# ===== LAST 3 LOGIN ATTEMPTS =====
print(f"{CYAN}=== LAST 3 LOGIN ATTEMPTS ==={NC}")

if system == "Darwin":
    print(subprocess.getoutput("last | head -n 3"))
else:
    print(subprocess.getoutput("last -n 3"))

print()
