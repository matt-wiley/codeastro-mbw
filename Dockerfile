## NOTE: https://scout.docker.com/vulnerabilities/id/CVE-2026-85091?s=debian&n=zlib&ns=debian&t=deb&osn=debian&osv=13&vr=%3E0
## - No fix versions available as of writing, check again later
FROM debian:13

ARG OS="Linux"
ARG ARCH="aarch64" 

ENV MINICONDA_INSTALLER="Miniconda3-latest-${OS}-${ARCH}.sh"
# Optimistically set the PATH where Miniconda will be installed.
ENV PATH=/root/miniconda3/bin:${PATH} 

USER root
WORKDIR "/docker-build-tmp"

# -----------------------------------------------------------------------------
#  Install OS-level packages
#
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        build-essential \
        vim \
        ca-certificates \
        && \
    update-ca-certificates

# -----------------------------------------------------------------------------
#  Install Miniconda
#
# Source: https://www.howtoforge.com/how-to-install-miniconda-on-debian-12/
#
# IMPORTANT:
#  - Running with '-b' flag to run in batch mode which disables manual intervention
#
RUN curl -fsSLO "https://repo.anaconda.com/miniconda/${MINICONDA_INSTALLER}" && \
    bash "./${MINICONDA_INSTALLER}" -b -p /root/miniconda3 && \
    rm "./${MINICONDA_INSTALLER}"


WORKDIR /
RUN rm -r "/docker-build-tmp"

# -----------------------------------------------------------------------------
#  Smoke Tests before we write the image
#  
#  Small checks as needed to verify: 
#   - tooling is accessible
#   - paths are correct
#   - configurations are correct
#  
#   NOTE: Tests below should return non-zero exit codes and cause the build fail.
# 
RUN conda --version