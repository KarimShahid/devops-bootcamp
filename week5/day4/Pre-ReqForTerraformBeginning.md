# Terraform Beginning

## Declarative vs Imperative

### Imperative Approach

In an **imperative** approach, you explicitly tell the system **how** to do something, step by step.

**Characteristics:**

- Focuses on *commands and procedures*
- Order of execution matters
- You manage the steps manually

**Example (Imperative):**

```bash
apt update

apt install -y nginx

systemctl start nginx
```

Here, you are instructing the system exactly *how* to install and start NGINX.

**Pros:**

- Easy to understand for small tasks
- Good for ad-hoc changes

**Cons:**

- Hard to maintain at scale
- Easy to introduce inconsistencies
- No built-in way to verify final state

---

### Declarative Approach

In a **declarative** approach, you define **what the final state should be**, and the tool figures out *how* to achieve it.

**Characteristics:**

- Focuses on *desired state*
- Idempotent (safe to run multiple times)
- Tool decides execution order

**Example (Declarative – Terraform):**

```bash
resource "aws_instance" "web" {

ami           = "ami-0abcd1234"

instance_type = "t2.micro"

}
```

You don’t say *how* to create the EC2 instance—only that it *should exist*.

**Pros:**

- Easier to scale
- Consistent environments
- Better automation and reliability

**Cons:**

- Initial learning curve

---

## Drift Detection and State Management

### What Is Drift?

**Drift** occurs when the actual infrastructure differs from what is defined in your IaC code.

**Example:**

- Terraform defines an EC2 instance as `t2.micro`
- Someone manually changes it to `t3.micro` in the AWS Console

Now your infrastructure has **drifted** from the desired state.

---

### Drift Detection

IaC tools detect drift by **comparing the desired state (code)** with the **actual state (real infrastructure)**.

**Examples:**

- Terraform: `terraform plan`
- CloudFormation: Drift Detection feature

**Why Drift Detection Matters:**

- Prevents configuration inconsistencies
- Improves security and compliance
- Enables predictable deployments

---

### State Management

State management is how IaC tools keep track of **what resources exist and how they are configured**.

**Examples:**

- Terraform state file (`terraform.tfstate`)
- CloudFormation stack state (managed by AWS)

**Why State Is Important:**

- Enables change detection
- Prevents duplicate resource creation
- Allows safe updates and deletions

**Best Practice:**

- Store state securely (e.g., S3 + DynamoDB locking for Terraform)
- Never edit state files manually

---

## Four Types of Infrastructure as Code

### 1. Configuration Management

**Purpose:**
Manage and maintain the configuration of **existing servers**.

**What It Does:**

- Install software
- Apply patches
- Enforce consistent configuration across servers

**Key Goal:**
Ensure that all environments (dev, staging, prod) are **consistently configured**.

**Example:**

- Making sure all servers:
    - Have the same OS patches
    - Have NGINX installed
    - Use the same config files

**Tool Example:**

- **Ansible**

---

### 2. Server Templating

**Purpose:**
Create **reusable templates** that define how a server or application environment should look.

**What It Does:**

- Builds immutable images
- Makes spinning up new servers fast and predictable

**Key Idea:**
Instead of modifying existing servers, you **replace them** with new ones built from templates.

**Example:**

- Docker images
- VM images (AMI, Azure Image)

**Tool Example:**

- **Docker**

**Docker Example:**

```docker
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
```

Strengths:

- Highly consistent environments
- Fast deployments
- Works well with CI/CD pipelines

---

### 3. Orchestration

**Purpose:**
Manage the **interactions and relationships** between multiple components of an infrastructure.

**What It Does:**

- Handles scaling
- Manages networking between services
- Ensures high availability

**Used For:**
Complex environments with many interconnected services.

**Example Scenario:**

- Web frontend
- Backend API
- Database
- Load balancer

All need to communicate reliably.

**Tool Example:**

- **Kubernetes**

**Strengths:**

- Automatic scaling
- Self-healing
- Manages containerized workloads at scale

---

### 4. Provisioning

**Purpose:**
Perform the **initial setup** of infrastructure resources.

**What It Does:**

- Create servers
- Create networks
- Create storage

**Examples:**

- EC2 instances
- VPCs
- S3 buckets

**Tool Examples:**

- Terraform
- AWS CloudFormation
- Azure Resource Manager (ARM)

**Strengths:**

- Infrastructure defined as code
- Repeatable and auditable
- Works well with version control

---

## Major IaC Tools by Cloud Provider

### AWS

- **AWS CloudFormation (CFT)**
- Native AWS IaC service
- Uses YAML or JSON

### Azure

- **Azure Resource Manager (ARM)**
- Native Azure IaC service
- Uses JSON (and Bicep as a newer option)

### Google Cloud Platform

- **Google Cloud Deployment Manager**
- Uses YAML and Jinja templates

---

## Terraform Overview

- **Cloud-agnostic** (works with AWS, Azure, GCP, and more)
- **Open-source**, maintained by HashiCorp
- Huge provider ecosystem

### Terraform Language

- Uses **HCL (HashiCorp Configuration Language)** 🤯
- Designed to be human-readable and expressive

**Example:**

provider "aws" {

region = "us-east-1"

}

**Why Terraform Is Popular:**

- One tool for multiple clouds
- Strong community support
- Excellent state management

---

## Data Formats Used in IaC

Most IaC tools use:

- **YAML**
- **JSON**

Terraform is unique because it uses:

- **HCL** (more readable and expressive than JSON)