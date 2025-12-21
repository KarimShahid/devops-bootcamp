# TerraForm ❗

## Architecture:

- Terraform CLI → runs on your local machine or CI
- terraform core → Engine that parses .tf files and compares desired vs actual state
- Providers → plugins that talk to APIs (AWS, K8s, Github)
- Terraform State → Local (.tfstate) and Remote (like S3 on the cloud)

### Terraform CLI:

- runs on Developers machine or CI/CD Runners ( runners → jata run huncha process)
- Core Commands:
    
    Reads the .tf files and sets up providers, backend, modules
    
    ```hcl
    terraform init
    ```
    

shows what terraform will change

```hcl
terraform plan
```

executes the plan and changes the real infra

```hcl
terrform apply
```

destroys resources tracked in state

```hcl
terraform destory
```

---

Create a dir for Terraform, and inside the dir;

Create terra/ main.tf

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

```

```hcl
terrform init
```

![Screenshot 2025-12-19 at 9.26.47 AM.png](images/Screenshot_2025-12-19_at_9.26.47_AM.png)

<aside>
📌

Just creates the dependencies like npm init

</aside>

```hcl
terraform plan
```

![Screenshot 2025-12-19 at 9.32.23 AM.png](images/Screenshot_2025-12-19_at_9.32.23_AM.png)

> Terraform is just for resource deployment.
> 

edit the [main.tf](http://main.tf) file

include resources

![Screenshot 2025-12-19 at 9.34.53 AM.png](images/Screenshot_2025-12-19_at_9.34.53_AM.png)

```hcl
terrform plan -out=shahids3
```

What does `terraform plan -out=s3bucketwow` actually do?

It **saves the execution plan to a file**, so you can apply **exactly what was planned**, with **no surprises**.

![Screenshot 2025-12-19 at 9.39.27 AM.png](images/Screenshot_2025-12-19_at_9.39.27_AM.png)

terraform apply

![Screenshot 2025-12-19 at 9.47.48 AM.png](images/Screenshot_2025-12-19_at_9.47.48_AM.png)

.tfstate 

- plan: compares .tfstate to your code and actual cloud resources tor see what must chnage
- apply: updates .tfsatete after successfully mkaing chnmages
- destroy: destroys the created resources.

```hcl
terraform destroy
```

![Screenshot 2025-12-19 at 10.08.02 AM.png](images/Screenshot_2025-12-19_at_10.08.02_AM.png)

Add another S3 resource

![Screenshot 2025-12-21 at 6.24.09 PM.png](images/Screenshot_2025-12-21_at_6.24.09_PM.png)

Creating a plan for new S3 bucket 

```hcl
terraform plan
```

![Screenshot 2025-12-21 at 6.25.40 PM.png](images/Screenshot_2025-12-21_at_6.25.40_PM.png)

Pushing the changes to the remote 

This will update the terraform.tfstate

```hcl
terraform apply
```

The older bucket will be refreshed.

![Screenshot 2025-12-21 at 7.43.55 PM.png](images/Screenshot_2025-12-21_at_7.43.55_PM.png)

The newer will be created.

![Screenshot 2025-12-21 at 7.44.37 PM.png](images/Screenshot_2025-12-21_at_7.44.37_PM.png)

Output

![Screenshot 2025-12-21 at 7.52.29 PM.png](images/Screenshot_2025-12-21_at_7.52.29_PM.png)