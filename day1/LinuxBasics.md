# Linux Basics

1. Dir

```powershell
pwd
```

![Screenshot 2025-06-11 at 7.57.34 AM.png](Linux%20Basics/Screenshot_2025-06-11_at_7.57.34_AM.png)

1. List in detail with hidden files

```powershell
ls -la
```

![Screenshot 2025-06-11 at 7.58.41 AM.png](Linux%20Basics/Screenshot_2025-06-11_at_7.58.41_AM.png)

- -la shows long list and hidden files
- - means file
- d means dir
- rwx - read, write and execute
- rwxrwxrws - owner, group and others permission (7,7,7)

1. Case Sensitive

![Screenshot 2025-06-11 at 8.02.05 AM.png](Linux%20Basics/Screenshot_2025-06-11_at_8.02.05_AM.png)

1. Manual

```powershell
man ls
```

![Screenshot 2025-06-11 at 8.03.48 AM.png](Linux%20Basics/Screenshot_2025-06-11_at_8.03.48_AM.png)

1. Change dir

```powershell
cd 
```

![Screenshot 2025-06-11 at 8.07.38 AM.png](Linux%20Basics/Screenshot_2025-06-11_at_8.07.38_AM.png)

1. Make dir

```powershell
mkdir linuxLab
```

![Screenshot 2025-06-11 at 8.08.24 AM.png](Linux%20Basics/Screenshot_2025-06-11_at_8.08.24_AM.png)

1. Remove dir

```powershell
rmdir linuxLab
rm -r linuxlab
```

1. Creating file

```powershell
touch f1.txt
```

1. Creating multiple files

```powershell
for i in {1..100}; do
  echo "This is file number $i" > "file_$i.txt"
done
```

looping so that it creates 100 files from 1 to 100

echo will print the line in each file

1. Removing all the files

```powershell
echo file_{1..100}.txt
rm file_{1..100}.txt
```

echo shows the files to be deleted

rm will remove all the files

1. Reading file

```powershell
cat f1.txt
```

1. Writing into file

```powershell
nano f1.txt
vi f1.txt
vim f1.txt
echo "Some text" >> f1.txt
```

![Screenshot 2025-06-11 at 8.12.42 AM.png](Linux%20Basics/Screenshot_2025-06-11_at_8.12.42_AM.png)

Writing with vi

![Screenshot 2025-06-11 at 8.14.33 AM.png](Linux%20Basics/Screenshot_2025-06-11_at_8.14.33_AM.png)

press the key i for inserting into the file

press esc key then :wq to write and quit.

Using echo

![Screenshot 2025-06-11 at 8.19.57 AM.png](Linux%20Basics/Screenshot_2025-06-11_at_8.19.57_AM.png)

“>>” mean append to the f1.txt

“>" means overwrite in the f1.txt

1. moving file

```powershell
mv f1.txt ../demoDir/
```

f1.txt is moving from its dir to another dir called demoDir

1. Moving all txt file

```powershell
mv *.txt ../demoDir/
```

moving all .txt file extensions to demoDir

1. Finding the path of the command

```powershell
which pwd
```

1. Adding User

```powershell
sudo adduser std1
```

![Screenshot 2025-06-11 at 8.38.01 AM.png](Linux%20Basics/Screenshot_2025-06-11_at_8.38.01_AM.png)

1. Switching user

```powershell
su - std1
su -i
```

![Screenshot 2025-06-11 at 8.38.49 AM.png](Linux%20Basics/Screenshot_2025-06-11_at_8.38.49_AM.png)

su -i will start a root login shell.

1. Changing permissions

Read → 4

Write → 2

Execute → 1

```powershell
chmod [options] [filename]

chmod 777 file.txt
chmod u+w file.txt
chmod u=r file.txt
chmod u-r+wx file.txt
```

![Screenshot 2025-06-12 at 7.47.19 AM.png](Linux%20Basics/Screenshot_2025-06-12_at_7.47.19_AM.png)

u+x → user is given execute permission

![Screenshot 2025-06-12 at 7.49.25 AM.png](Linux%20Basics/Screenshot_2025-06-12_at_7.49.25_AM.png)

u-x → removes the permission

![Screenshot 2025-06-12 at 7.55.24 AM.png](Linux%20Basics/Screenshot_2025-06-12_at_7.55.24_AM.png)

u-r+wx  → read permission is removed, write and execute is given

1. Changing ownership

```powershell
chown [new_owner]:[new_group] file_or_directory
```

1. finding files

```powershell
find [path] -name [filename]
```

![Screenshot 2025-06-12 at 8.02.48 AM.png](Linux%20Basics/Screenshot_2025-06-12_at_8.02.48_AM.png)

finding files ending with .txt

![Screenshot 2025-06-12 at 8.13.25 AM.png](Linux%20Basics/Screenshot_2025-06-12_at_8.13.25_AM.png)

finding files of size > 2kb

1. Grep

```powershell
grep [expression] file.txt

grep "Lorem" file.txt
grep -i "LOREM" file.txt
```

![Screenshot 2025-06-12 at 8.10.21 AM.png](Linux%20Basics/Screenshot_2025-06-12_at_8.10.21_AM.png)

Case sensitive search.

![Screenshot 2025-06-12 at 8.12.09 AM.png](Linux%20Basics/Screenshot_2025-06-12_at_8.12.09_AM.png)

-i ignores case sensitivity

1. zip and unzip

```powershell
gzip file.txt
gunzip file.txt
```

![Screenshot 2025-06-12 at 8.24.57 AM.png](Linux%20Basics/Screenshot_2025-06-12_at_8.24.57_AM.png)

1. Ping in background and kill it

![Screenshot 2025-06-12 at 8.51.24 AM.png](Linux%20Basics/Screenshot_2025-06-12_at_8.51.24_AM.png)

/dev/null will store the ping packets.

We can use the terminal freely.

1. System Memory

```powershell
free -m
```

![Screenshot 2025-06-13 at 7.53.59 AM.png](Linux%20Basics/Screenshot_2025-06-13_at_7.53.59_AM.png)

1. Checking auth logs

```powershell
cat /var/log/auth.log

sudo grep -a "Failed password" /var/log/auth.log
```

![Screenshot 2025-06-13 at 8.31.45 AM.png](Linux%20Basics/Screenshot_2025-06-13_at_8.31.45_AM.png)

Terminal Hacks

![Screenshot 2025-06-15 at 9.41.38 AM.png](Linux%20Basics/Screenshot_2025-06-15_at_9.41.38_AM.png)

![Screenshot 2025-06-15 at 9.42.19 AM.png](Linux%20Basics/Screenshot_2025-06-15_at_9.42.19_AM.png)

![Screenshot 2025-06-15 at 9.42.36 AM.png](Linux%20Basics/Screenshot_2025-06-15_at_9.42.36_AM.png)

![Screenshot 2025-06-15 at 9.43.22 AM.png](Linux%20Basics/35555d60-c209-4b18-99df-d7587f78fdc8.png)

Zoom in = cmd + [+]

Zoom out = cmd + [-]