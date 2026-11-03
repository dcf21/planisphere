## Make your own cardboard model planisphere

This repository contains Python scripts that can be used to produce a cardboard cut-and-glue kit to make your own model planisphere.

### Introduction

A planisphere is a simple hand-held device which shows a map of which stars are visible in the night sky at any particular time. By rotating a wheel, it shows how stars move across the sky through the night, and how different constellations are visible at different times of year.

See <https://in-the-sky.org/planisphere/index.php> for more information, including detailed assembly instructions.

### Getting started

To make planisphere models for all latitudes, at five degree intervals, run the shell script `main_planisphere.sh`.

### Running in Docker

The scripts need Python 3 with the `cairocffi` and `numpy` packages, and LaTeX
to assemble the final PDF documents. Rather than installing these yourself, you
can run the scripts inside a Docker container, using the `Dockerfile` and
`docker-compose.yml` in this repository. The container uses Python 3.14 on
Debian.

To build the Docker image, and then make the planisphere models inside a
container, run:

```
docker compose build
docker compose run --rm python
```

This runs `main_planisphere.sh --theme default` inside the container, and
removes the container when it finishes. Making models for every latitude takes
several minutes. The repository directory is shared with the container, so the
output appears in the `output` directory, replacing any previous output.

The container runs as root, so the files it creates will be owned by root. To
create them as your own user instead, run:

```
docker compose run --rm --user "$(id -u):$(id -g)" -e HOME=/tmp python
```

### Caveat

Planispheres do not work well when used close to the equator. The scripts in this repository do not allow you to create planispheres for latitudes between 15&deg;N and 15&deg;S, as the celestial pole is too close to the horizon.

## Author

This code was developed by Dominic Ford <https://dcford.org.uk>. It is distributed under the Gnu General Public License V3.

