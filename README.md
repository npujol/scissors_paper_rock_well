# scissors_paper_rock_well

A version of the game scissor-paper-rock, but now including a new word **well**.

## Install

### Requirements

1.[Docker](https://www.docker.com/) installed in your system.

### Steps to install the service

Step 1: Clone the project

```shell
git clone git@github.com:npujol/scissors_paper_rock_well.git
```

Step 2: Move to the project's folder

```shell
cd scissors_paper_rock_well/
```

## Test

The steps to run the tests are the followings:

Step 1: Build the local image

```shell
docker build . -t local_app
```

Step 2: Run the tests \[Optional\]

```shell
docker run app python -m pytest --verbose
```

## Development

The steps to development are the followings:

Step 1: Create the virtual environment
Step 2: Install poetry

```shell
pip install poetry

```

Step 3: Install the poetry dependencies

```shell
poetry install
```

## Production

The steps to use the service in production are the followings:

Step 1: Build the image for production, removing the development dependencies

```shell
docker build . -t production_app --build-arg CURRENT_ENV=production
```

Step 2: Run the service

```shell
docker run -d -p 8000:8000 production_app
```

You can visit http://localhost:8000/ to see the API documentation

## How to run the service on AWS

To the deploy and run the docker image on AWS ECS, you can follow the [Docker Documentation](https://docs.docker.com/cloud/ecs-integration/).

### Requirements

- [Docker containing the ECS functionality](https://docs.docker.com/cloud/ecs-integration/#install-the-docker-compose-cli-on-linux)
- An [AWS account](https://aws.amazon.com/resources/create-account/)
- [Manage IAM permissions](https://aws.amazon.com/iam/features/manage-permissions/) for your user
- Install the [AWS CLI tool](https://aws.amazon.com/cli/)

### Run an application on ECS

Step 1: Create AWS context

```shell

docker context create ecs myappcontext

```

Step 2: List your docker contexts and check if the new context is active

```shell

docker context ls

```

Step 3: Run the docker image

```shell

docker --context myappcontext run -p 80:80 production_app

```
