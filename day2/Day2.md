# Day 2 - 18 Nov 2025

## DevOps Culture

DevOps is a collaborative approach to software development and IT operations, emphasizing **Collaboration, Automation, and Continuous Integration (CI)**.

### Key Concepts:

- Collaboration: Practice of bringing development and operations teams together to work as one unified group throughout the entire software lifecycle. By integrating diverse skills and perspectives, this collaboration enhances efficiency and accelerates project timelines.
- Automation (Auto): Manual repetitive tasks like deployments and testing are automated to ensure speed and reliability.
- Continuous Integration (CI): Code changes are automatically tested and integrated into a shared repository frequently.

### Artifact

- They are by-products created during the software development lifecycle. These artifacts are usually created as a result of the Continuous Integration (CI) process and can be used in further stages of the software development lifecycle, such as testing, deployment, and release. 
For example, compiled code, container images, meeting notes, risk assessments, user guides, images, executables, and prototypes

---

## Key DevOps Metrics

Monitoring key metrics is crucial for measuring performance, reliability, and the quality of deployments.

| Metric | Definition | Importance / Benchmark |
| --- | --- | --- |
| **Deployment Frequency** | How often code reaches production | Higher frequency indicates faster delivery |
| **Lead Time for Changes** | Time from commit to production deployment | Shorter lead time shows efficient development process |
| **Mean Time to Recovery (MTTR)** | Time taken to recover from a failure | Focused on monitoring; impacts SLA and SLO |
| **Change Failure Rate** | % of deployments causing issues | 0–15% → Excellent, 16–30% → Good, 31%+ → Poor |
| **Measures (Code Quality)** | Assessment of code reliability and testing effectiveness | Shows if testing methods need improvement |

## DOC FORMAT for some kind of case study

- **Why is this case study needed?** (Stakeholder reason)
→ Explain in 2–3 lines why bosses/managers/customers care.
Example: “Company was losing money because of slow releases and bugs. This case study shows how DevOps fixed it.”
- **Intro**
→ Just a short hello: what company, what project, when it happened.
- **Problem Statement**
→ What was broken before?
→ Why were we doing this project? What pains did we want to solve?
(slow releases, too many bugs, servers down, high cost, etc.)
- **The Solution**
→ What exact DevOps things we did to fix those problems
(CI/CD, Docker, Kubernetes, automation, monitoring, etc.)
- **Architecture Diagram + Description**
→ Put the picture of new system + explain it in simple sentences.
- **Key Metrics**
→ Numbers that prove we became better
(deployment speed, uptime, how fast we fix bugs, etc.)
→ Always show “Before” vs “After”.
→ Remember DORA
- **TCO Analysis** (optional)
→ Total money spent before vs after.
→ Show how much money/company saved.
- **Conclusion**
→ One short paragraph: “We fixed it, results are awesome, everyone is happy.”

# Linux Filesystem Hierarchy

Linux generally follows the [Filesystem Hierarchy Standard (FHS)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html). This standard reference (developed in 1994) describes the common layout conventions used by most UNIX and UNIX variant systems. It consists of a single primary (or root) directory with multiple branching 
sub-directories.

![Screenshot 2025-11-18 at 7.44.33 PM.png](Day%202%20-%2018%20Nov%202025/Screenshot_2025-11-18_at_7.44.33_PM.png)

The `/bin` directory contains essential commands programs(binaries) needed by all users, including `cp`, `ls`, `ssh`, and `kill`. These commands are universally available across user types.

`/etc` - Short for "Editable Text Configuration”, This is the core system configuration directory. It contains configuration files for the operating system and installed applications, but it should not contain any executable binaries.

`/opt` - Third-party software and packages not part of the default system installation are stored here. It includes their configuration and data files.

- Contains add-on applications from individual vendors.
- Add-on applications should be installed under either /opt/ or /opt/ sub-directory.

`/var` - Variable data → Files that keep changing:
• /var/log → all system logs (very important!)
• /var/www → web server files
• /var/mail → emails
• /var/spool → print jobs

`/usr`  -  User programs and data. The biggest folder! Contains almost all software:
• /usr/bin → normal programs (thousands of commands)
• /usr/local → software you install manually
• /usr/share → documentation, icons, templates