# CI CD 🔁 Theory

## Continuous Integration 🤝

- Software dev practice
- Enables frequent merge of code changes.
- Integrating code changes from multiple dev into a central repo frequently.

### Cons

- Teams will need to write automated tests for each new feature, improvement or bug fix
- CI sever is needed.
- Devs will need to merge more frequently

### Pros

- Less bugs as Automated Tests capture regressions
- Efficient to build a release as integration issues have been resolved early.
- Parallel testing

## Continuous Delivery 💿

Extension of CI

- Auto deploy all code changes to a testing and/or production env after the build stage.
- Release to production more frequently
- Deploy → put in any server/ env. run anywhere.
- Release → put in the hands of the customer

### Cons

- Dependent on CI. So, a strong CI is needed.
- Deployments need to be fully automated.
- Automated testing required additional complex mechanisms like feature flags, A/B testing, Percentage Rollout etc.

### Pros

- Save time with instant release (one time effort).
- Frequent releases → More feedback from users.
- Less decision making → leads to faster iterations.

## Continuous Deployment

CI/CD has evolved to being more as CI/CD/CD

Needs more effort than CI/CD