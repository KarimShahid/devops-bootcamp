# Assignment: Bash Scripting

Tasks: Write a script that:

- Identifies the PID using the most CPU
- **Logs its PID, process name, and CPU usage to `cpu_report.txt`**

![Screenshot 2025-11-20 at 6.01.43 PM.png](images/Screenshot_2025-11-20_at_6.01.43_PM.png)

```docker
top -b -o +%CPU -n 1 | \
awk '
    NR==7 {
        for (i=1; i<=NF; i++) header[i]=$i
    }
    NR==8 {
        print header[1] " = " $1
        print header[2] " = " $2
        print header[9] " = " $9
    }
' > cpu_report.txt
```

![Screenshot 2025-11-20 at 6.01.52 PM.png](images/Screenshot_2025-11-20_at_6.01.52_PM.png)

- `top` → a Linux utility to show running processes.
- `b` → **batch mode**, non-interactive output (good for scripts).
- `o +%CPU` → sort the output **by CPU usage**, highest first.
- `n 1` → **take only 1 snapshot** and exit (do not refresh continuously).
- **`awk ' ... '`**→ AWK is a **text-processing tool**. It reads **input line by line**, splits each line into **fields** (columns) automatically, and allows actions based on patterns.

**Line: `NR==7 { for (i=1; i<=NF; i++) header[i]=$i }`**

- `NR` → “Number of Record” = **current line number**.
- `NR==7` → Only execute this block on **line 7**, which is the **header line** in top output
- `NF` → “Number of Fields” = how many columns in the line.
- `for (i=1; i<=NF; i++) header[i]=$i`
    - Loops over each column of the header.
    - Saves the column names in an array `header[]`:

**Line: `NR==8 { ... }`**

- `NR==8` → Only execute this block on **line 8**, which is the **top CPU-consuming process line**
- `$1, $2, $9` → Access **columns of the current line** (line 8)
- `header[x] " = " $x` → Combines **header name** with **value**, producing:

![Screenshot 2025-11-20 at 6.03.09 PM.png](images/Screenshot_2025-11-20_at_6.03.09_PM.png)