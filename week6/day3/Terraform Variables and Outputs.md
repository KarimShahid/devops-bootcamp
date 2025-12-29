# Terraform: Variables and Outputs

Terraform is declarative → Describe what you want, not how to do it

- Variables → lets you parameterize your infrastructure.
- Variables can change depending on environment or user input

Outputs → Exposes the results after it creates resources.

- Info you want to see or use next

> input (vars) → Terraform → Outputs (results)
> 

## Variables

can be reused across your infrastructure

```hcl
variable "region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}
```

Usage

```hcl
provider "aws" {
  region = var.region
}
```

### Common types of Variables

- String
- Number
- Bool
- List

```hcl
variable "az"{
	type = list(string)
}
```

terraform.tfvars:

```hcl
az = [
  "us-east-1a",
  "us-east-1b",
  "us-east-1c"
]
```

CLI

<aside>
📌

terraform apply -var='availability_zones=["us-east-1a","us-east-1b"]’

</aside>

- Map

```hcl
variable "tags"{
	type = map(string)
}
```

terraform.tfvars:

```hcl
tags = {
  Environment = "dev"
  Owner       = "team-a"
  Project     = "terraform-demo"
}

```

CLI

<aside>
📌

terraform apply -var='tags={Environment="dev",Owner="team-a"}'

</aside>

### Priority Order

Terraform gets value of vars from lowest to highest

- default value
- terraform.tfvars
- *.auto.tfvars
- -var command line flag
- -var-file

### Input validations

- tf validates input before it runs
- prevents bad input early

```hcl
variable "environment" {
	type = string
	
	validation {
	    		condition     = contains(["dev", "staging", "prod"], var.environment)
	    		error_message = "Environment must be dev, staging, or prod."
	  	}
}

```

## Outputs

Outputs are values which terraform prints after **apply**

- stored in state

```hcl
output "instance_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.web.public_ip
}
```

### Importance:

- Human Visibility (ease of access)
- Cross-module communication → modules need outouts to tak to each other
- Automation

### Behaviour:

1. calculated after resources are created.
2. Stored in terraform state
3. Recomputed on every apply
4. sensitive outputs can be masked

```hcl
output "db_password"{
	value = var.db_password
	sensitive = true
}
```

Hidden from cli output but still stored in state