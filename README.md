# helloworld-cloudevent-function

## Libraries

- [functions-framework](https://github.com/GoogleCloudPlatform/functions-framework-python)
- [cloudevents](https://github.com/cloudevents/sdk-python)
- [pytest](https://github.com/pytest-dev/pytest)
- [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio)
- [structlog](https://github.com/hynek/structlog)

## Bootsrap

```bash
./install
```

## Run locally

Spin up server locally, listen on port 8080

```bash
docker compose up --build
```

Send a mock cloudevent

```bash
./venv/bin/pytest -v -s --tb=short invoke_test.py
```

## Build and push

Create builder

```bash
docker buildx create --use --platform=linux/arm64,linux/amd64 --name multi-platform-builder
```

Build and push

```bash
docker buildx build --platform linux/arm64,linux/amd64 -t "helloworld-python" --build-arg PYTHON_VERSION=3.12 .
```
