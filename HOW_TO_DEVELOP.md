## Before you begin

### Required

- [docker & docker-compose](https://www.docker.com)

## Before development

### (optional) Create the ENV file for Docker

Create the `.env` file like bellow.

on Linux

```
UID=1000
GID=100
```

## Run

```shellsession
python -m mazgi_sandbox_4d36b809 mazgi_sandbox_4d36b809/
```

## Test

```shellsession
python -m pytest mazgi_sandbox_4d36b809/tests/
```

## Install / uninstall

```shellsession
pip uninstall --yes mazgi-sandbox-4d36b809
pip install --no-cache-dir .
mazgi-sandbox-4d36b809
```

## Build pip

```shellsession
python setup.py sdist bdist_wheel
python -m twine upload --verbose --repository-url https://upload.pypi.org/legacy/ dist/*
```
