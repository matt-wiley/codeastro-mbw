

OS_ARCH_NAME ?= arm64
MINICONDA_ARCH_NAME ?= aarch64

docker-build:
	docker build --build-arg "ARCH=$(MINICONDA_ARCH_NAME)" -t "codeastro-mbw:latest-$(OS_ARCH_NAME)" .