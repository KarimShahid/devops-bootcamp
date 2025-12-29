# Terraform: Code Correction, Validation & Drift Management

This document explains how Terraform helps maintain clean Infrastructure as Code (IaC) and how it detects and manages infrastructure drift.  
It is suitable for learning, revision, and GitHub documentation.

---

## 1. Code Correction in Terraform

Terraform provides built-in commands to ensure your configuration is clean, readable, and valid before deployment.

### 1.1 Formatting (`terraform fmt`)

Formats Terraform configuration files according to standard style conventions.

```hcl
terraform fmt
```

**What it does:**
- Fixes indentation and spacing
- Aligns arguments consistently
- Improves readability and maintainability

You can also format recursively:

```hcl
terraform fmt -recursive
```

---

### 1.2 Validation (`terraform validate`)

Validates the Terraform configuration files without accessing remote services.

```hcl
terraform validate
```

**What it checks:**
- Syntax correctness
- Required arguments are present
- References to variables, resources, and providers are valid

> Note: Validation does NOT check real infrastructure.

---

## 2. Terraform State Overview

Terraform uses a **state file** (`terraform.tfstate`) to track real infrastructure.

**Purpose of state:**
- Maps Terraform resources to real-world resources
- Stores metadata and dependencies
- Enables Terraform to calculate changes safely

---

## 3. What is Drift?

**Infrastructure Drift** occurs when real infrastructure changes outside Terraform after it has been applied.

In this situation:
- Terraform state ≠ Real infrastructure
- Terraform code no longer represents reality

---

## 4. Common Causes of Drift

- Manual changes via AWS Console
- Manual changes using AWS CLI or SDKs
- Other IaC tools (CloudFormation, CDK, Pulumi)
- Auto Scaling or managed AWS services modifying resources
- Hotfixes applied directly in production

---

## 5. Why Drift is Dangerous

- Unexpected production behavior
- Broken deployments
- Terraform apply may fail or overwrite changes
- Loss of Infrastructure as Code reliability

---

## 6. Drift Detection in Terraform

Terraform detects drift by comparing:

| Component | Description |
|---------|-------------|
| Desired State | Terraform configuration files |
| Current State | Real infrastructure in the cloud |

### 6.1 Using `terraform plan`

```hcl
terraform plan
```

**What it does:**
- Refreshes state
- Detects drift
- Shows planned changes to fix drift

---

### 6.2 Detect Drift Only (`-refresh-only`)

To check drift without planning any modifications:

```hcl
terraform plan -refresh-only
```

**Use case:**
- Auditing infrastructure
- CI/CD drift detection
- Safe inspection without risk

---

## 7. Fixing Drift

There are two common approaches:

### Option 1: Update Terraform Code (Recommended)

- Modify `.tf` files to match the real infrastructure
- Run:

```hcl
terraform apply
```

### Option 2: Revert Infrastructure to Code

- Let Terraform overwrite manual changes:

```hcl
terraform apply
```

> Best practice: Avoid manual changes in production.

---

## 8. Best Practices to Prevent Drift

- Use Terraform as the **single source of truth**
- Restrict console access in production
- Use IAM roles with least privilege
- Enable CI/CD pipelines for Terraform
- Use `terraform plan` in pull requests
- Lock state using remote backends (S3 + DynamoDB)

---

## 9. Related Terraform Commands

```hcl
terraform init        # Initialize providers and backend
terraform plan        # Preview changes
terraform apply       # Apply changes
terraform destroy     # Destroy infrastructure
terraform state list  # Inspect state
```

---

## 10. Summary

- `terraform fmt` ensures clean code
- `terraform validate` ensures correctness
- Drift happens when infra changes outside Terraform
- `terraform plan` detects drift
- `terraform plan -refresh-only` safely audits drift
- Prevent drift using strong IaC discipline

---

**Author:** Karim  
**Purpose:** Terraform Learning & DevOps Practice  
