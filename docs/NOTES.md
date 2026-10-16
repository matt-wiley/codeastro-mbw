# NOTES

## Installation -- Debian 13 via Docker

- There's a known CVE for debian 13 at the moment
  - NOTE: https://scout.docker.com/vulnerabilities/id/CVE-2026-85091?s=debian&n=zlib&ns=debian&t=deb&osn=debian&osv=13&vr=%3E0
  - No fix versions available as of writing, check again later

- Must install curl and ca-certificates from APT to download Miniconda isntaller script
  - Dockerfile runs update-ca-certificates to refresh the image and enable curl download

- This is being developed on Macbook Air M1 so it uses Aarch64
  -  There are OS and ARCH build args that can be passed to the Docker build to enable other targets (particularly other ARCH targets)

