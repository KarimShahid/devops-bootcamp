# Day 3 - 19 Nov 2025

# Task1

Creating users

![Screenshot 2025-11-19 at 9.50.25 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_9.50.25_AM.png)

Checking if they are created

![Screenshot 2025-11-19 at 9.51.10 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_9.51.10_AM.png)

Creating groups

![Screenshot 2025-11-19 at 9.53.03 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_9.53.03_AM.png)

Checking the groups

![Screenshot 2025-11-19 at 9.53.36 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_9.53.36_AM.png)

![Screenshot 2025-11-19 at 9.53.49 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_9.53.49_AM.png)

Adding users to groups

![Screenshot 2025-11-19 at 10.00.42 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.00.42_AM.png)

Checking if users are added in the groups

![Screenshot 2025-11-19 at 10.01.04 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.01.04_AM.png)

![Screenshot 2025-11-19 at 10.00.17 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.00.17_AM.png)

# Task2

![Screenshot 2025-11-19 at 10.10.57 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.10.57_AM.png)

Creating /var/www/project

![Screenshot 2025-11-19 at 10.02.43 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.02.43_AM.png)

Creating dir inside the /var/www/project

![Screenshot 2025-11-19 at 10.14.21 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.14.21_AM.png)

![Screenshot 2025-11-19 at 10.15.32 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.15.32_AM.png)

Setting groups for the new dirs

![Screenshot 2025-11-19 at 10.17.31 AM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.17.31_AM.png)

Setting permissions for each dir

### **source/**

- Only `devteam` can read/write, others no access:

Not 760 because the group wouldn't be able to enter (cd) into the folder nor list its files. if you want to open and read files, you must have execute permission also.

![Screenshot 2025-11-19 at 6.19.41 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_6.19.41_PM.png)

### **scripts/**

- Only `deploy` can execute scripts:

`chmod 750`  is required because to execute a script, you must have read permission on it. Only compiled binaries can be executed without read permission.

![Screenshot 2025-11-19 at 6.21.37 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_6.21.37_PM.png)

### **shared/**

- All `devteam` members can read/write
- New files inherit the group `devteam`:

![Screenshot 2025-11-19 at 6.33.43 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_6.33.43_PM.png)

<aside>
🔥

**Sticky bit?**

- The **sticky bit** is a special permission that you can set on **directories** (and rarely, on files).
- Its main purpose is **to control file deletion** in a shared directory.

**Rule:**

> When a directory has the sticky bit set, users can only delete or rename files that they own, even if the directory is writable by others.
> 

Without the sticky bit, anyone with write permission on the directory can delete or rename anyone else’s files.

</aside>

### **logs/**

- All `devteam` members can append (write), but not delete others’ files → **set sticky bit**:

![Screenshot 2025-11-19 at 6.40.19 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_6.40.19_PM.png)

Verifying

![Screenshot 2025-11-19 at 6.43.27 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_6.43.27_PM.png)

# Task3

![Screenshot 2025-11-19 at 6.47.03 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_6.47.03_PM.png)

1.

![image.png](Day%203%20-%2019%20Nov%202025/image.png)

- The directory `/var/www/project/source/` is **owned by `root`** and **group-owned by `devteam`**.
- Permissions are set to `rwxrws---`, which means:
    - Owner (root) → read, write, execute
    - Group (devteam) → read, write, execute → allows devteam members to **enter (`cd`) and modify files**
    - Others → no access
- The **`s` in the group execute position indicates the SGID bit is set**.
- **SGID ensures that any new files or subdirectories created inside `/source/` automatically inherit the `devteam` group**, maintaining consistent group ownership.
- Because others have no permissions, **only devteam members can access and modify the directory contents**.
- This setup ensures **controlled collaboration for the development team** while keeping files grouped properly.

2.

Everyone in devteam can append to logs

No one can delete or modify others’ log files → **use sticky bit**

![Screenshot 2025-11-19 at 8.48.27 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_8.48.27_PM.png)

- The directory `/var/www/project/logs/` is **owned by `root`** and **group-owned by `devteam`**.
- Permissions are set to `rwxrwx--T`, which means:
    - Owner (root) → read, write, execute
    - Group (devteam) → read, write, execute → allows devteam members to **append files** and enter the directory
    - Others → no access
- The **capital `T` at the end indicates the sticky bit is set**.
- **Sticky bit prevents users from deleting or renaming files they do not own**, even if they have write permissions on the directory.
- As a result, **everyone in devteam can append/write to logs**, but **cannot delete or modify files created by other members**.
- This setup allows safe collaborative logging while preserving each user’s files.

3.

![Screenshot 2025-11-19 at 9.14.57 PM.png](Day%203%20-%2019%20Nov%202025/3d81d34d-d9d4-4dd9-b8d5-6a2cab941ed8.png)

- Created an empty file deploy.sh in /var/www/project/scripts using sudo touch.
- Added a simple bash script into deploy.sh that echoes "Deployment script running...".
- Correctly set initial permissions to 700 so only the owner could read, write, and execute.
- Changed the owner of the script to deploy and the group to deployers.
- Set the **SUID bit with chmod 4700** so the script runs with the privileges of the deploy user.
- Listed the file to verify permissions, owner, group, and SUID were correctly applied.

4.

![Screenshot 2025-11-19 at 9.19.09 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_9.19.09_PM.png)

- The directory `/var/www/project/shared/` is **group-owned by `devteam`**.
- Permissions are set so that **all devteam members have read, write, and execute access** on the directory.
- Execute permission on the directory allows users to **enter (`cd`) the directory**.
- The **SGID bit is set** on the directory, indicated by `s` in the group execute slot.
- Because of SGID, any **new files or subdirectories created inside inherit the group `devteam` automatically**.
- Other users (not in `devteam`) have **no access**.

# Task4

![Screenshot 2025-11-19 at 6.43.53 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_6.43.53_PM.png)

Creating umask 002 for devteam

![Screenshot 2025-11-19 at 7.39.54 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_7.39.54_PM.png)

![Screenshot 2025-11-19 at 7.38.53 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_7.38.53_PM.png)

![Screenshot 2025-11-19 at 7.40.32 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_7.40.32_PM.png)

![Screenshot 2025-11-19 at 8.16.56 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_8.16.56_PM.png)

1. Created a new script `/etc/profile.d/devteam-umask.sh` using `sudo nano`.
2. Inside the script, added a **conditional statement** that checks if the logged-in user belongs to the `devteam` group using `groups $USER | grep -q '\bdevteam\b'`.
3. If the user is in `devteam`, the script sets their **default umask to 002**, so new files are group-writable.
4. Saved the script and exited the editor.
5. Made the script **executable**, so it runs automatically when users log in.

As a result, **any devteam member logging in will automatically have a default umask of 002**, without affecting other users.

# Task5

![Screenshot 2025-11-19 at 6.44.18 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_6.44.18_PM.png)

1.

![Screenshot 2025-11-19 at 9.36.43 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_9.36.43_PM.png)

2.

![Screenshot 2025-11-19 at 9.39.46 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_9.39.46_PM.png)

3.

![Screenshot 2025-11-19 at 10.15.05 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.15.05_PM.png)

# Task6

![Screenshot 2025-11-19 at 6.45.46 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_6.45.46_PM.png)

Screenshots

![Screenshot 2025-11-19 at 10.19.41 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.19.41_PM.png)

![Screenshot 2025-11-19 at 10.20.54 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.20.54_PM.png)

![Screenshot 2025-11-19 at 10.22.36 PM.png](Day%203%20-%2019%20Nov%202025/Screenshot_2025-11-19_at_10.22.36_PM.png)

### Why SUID, SGID, and Sticky Bit?

**SUID [4] (Set User ID) on `deploy.sh`:**

- Ensures the script runs with the owner’s privileges (user `deploy`).
- Useful for CI/CD or automated processes that need consistent permissions.
- Misuse of SUID, especially with root, can pose a security risk if the script is not carefully written or validated.

**SGID [2] (Set Group ID) on `source/` and `shared/`:**

- Forces all newly created files and directories to inherit the `devteam` group.
- Simplifies collaboration, as all team members automatically share group ownership and permissions.

**Sticky Bit [1] on `logs/`:**

- Prevents users from deleting or renaming files owned by others in the directory.
- Protects log files from accidental or unauthorized removal, while still allowing developers to create and append their own logs.

### Security Implications

**Least Privilege:**

- Only `devteam` members have access to `source/` and `shared/`; other users are blocked.
- `deploy.sh` is executable only by the `deploy` user, minimizing exposure of critical deployment scripts.

**SUID Risks:**

- If `deploy.sh` contains insecure commands or allows arbitrary execution, an attacker could exploit the elevated privileges.
- SUID scripts should be simple, carefully audited, and avoid unsafe user input.

**SGID & Group Sharing:**

- Ensures all new files in `source/` and `shared/` inherit the `devteam` group, simplifying collaboration.
- Any `devteam` member can modify group files; for finer control, ACLs can restrict individual users.

**Sticky Logs:**

- Prevents users from deleting or renaming files owned by others, preserving audit trails and log integrity.
- Users can still modify their own logs, so critical logs may require additional protection (e.g., root-owned or append-only).