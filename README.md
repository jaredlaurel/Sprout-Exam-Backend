# Jared Laurel Sprout BE Exam

## Installation 📌

### Build Employee Service

Build and Run
```shell
make build
```

Logs
```shell
make logs
```

### DB Migration
```shell
cd db-migration
make migrate
```

Access:
```
http://localhost:8000/docs/
```

### Unit Test

Run:
```shell
sh employee-service/runtest.sh -v
```
<br /> 

If we are going to deploy this on production, what do you think is the next
improvement that you will prioritize next? This can be a feature, a tech debt, or
an architectural design.
```
I believe the next step for enhancement involves the creation and integration
of an Authorization Service. Given the importance of security in our APIs,
it is critical that we ensure their protection.

Given that our repository is structured as a monolithic one, establishing a
dedicated Authorization microservice represents the optimal approach to maintain
a well-structured and efficient codebase.

Here are a few ideas to consider for this improvement:

1. Implement JWT-based Authorization
2. OAuth2 Integration
3. API Key Management
```
