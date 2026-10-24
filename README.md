# Project 07 — Dockerised Cloud API

A containerised Python FastAPI application for my cloud engineering portfolio.

## Features

- FastAPI homepage and health-check endpoints
- Docker containerisation
- Three automated pytest tests
- GitHub Actions continuous integration

## Run locally

Build:

    docker build -t jennyoma-cloud-api:v3 .

Run locally:

    docker run --rm -d --name jennyoma-api -p 127.0.0.1:8001:8000 jennyoma-cloud-api:v3

Visit http://localhost:8001

## Run tests

    docker run --rm --entrypoint python jennyoma-cloud-api:v3 -m pytest -q

## Planned AWS architecture

Docker → Amazon ECR → Amazon ECS with AWS Fargate

Terraform infrastructure will be added in a later stage.

## Security

- Local API published on localhost only
- No AWS credentials or secrets included
- No AWS infrastructure deployed yet
