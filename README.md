# docker-practive-with-python
This repo gives you understanding with python(pandas) and docker basics.

## Requirements

- Docker Desktop (or Docker Engine) installed and running on your machine.
- Git (optional, for source control and pushing to GitHub).
- Python packages listed in `requirements.txt` (this project uses `pandas`).

## Setup & How to run

1. Open PowerShell and change to the project folder:

```powershell
cd "D:\projects\Docker"
```

2. Build the Docker image (runs the Python script inside the image):

```powershell
docker build -t pandas-runner -f DockerFile .
```

3. Create a host output folder (so generated CSV is saved on your host)

4. Run the container and mount the host folder to the container output path `/data`:

```powershell
docker run --rm -e OUTPUT_DIR=/data -v "D:\projects\Docker\output:/data" pandas-runner
```

## Notes

- The `DockerFile` sets a default `OUTPUT_DIR=/data` and declares `/data` as a `VOLUME`. You can override it at runtime using `-e OUTPUT_DIR=...` and mounting a host folder to the same container path with `-v host:container`.
- If you mount the entire repo to `/app` (instead of `/data`), set `-e OUTPUT_DIR=/app` so the output appears in the repo folder on the host.
- Pin package versions in `requirements.txt` for reproducible builds (for example `pandas==2.1.0`).
- Add a `.dockerignore` to avoid copying large files (e.g., `output/`, `.venv/`, `.git`) into the image.
