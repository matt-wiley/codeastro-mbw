# Contributing

This is a personal repository holding my self-study work with the
[Code/Astro workshop](https://semaphorep.github.io/codeastro/) materials. It isn't
actively seeking contributions, but issues and suggestions are welcome. Pull
requests may not be merged.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
Anything you contribute is accepted under the project's
[BSD 3-Clause License](LICENSE).

## Issues and Suggestions

- Search existing issues before opening a new one.
- Say what you expected, what happened, and how to reproduce it.
- See [SECURITY.md](SECURITY.md) for the project's security notes.

## Pull Requests

If you'd like to send a change, opening an issue first to ask is the best way
to avoid wasted effort. Keep each pull request to one change and describe what
it does and how you checked it.

## Building the Docker Image

The `Dockerfile` builds a Debian 13 image with Miniconda. It defaults to
`Linux` and `aarch64`. Override the build args for other targets:

```sh
docker build --build-arg ARCH=x86_64 -t codeastro-mbw:latest-amd64 .
```

`make docker-build` does the same. It takes the Miniconda `ARCH` build arg from
`MINICONDA_ARCH_NAME` (default `aarch64`) and tags the image
`codeastro-mbw:latest-$(OS_ARCH_NAME)` (`OS_ARCH_NAME` defaults to `arm64`).
For Intel/AMD, run
`make docker-build MINICONDA_ARCH_NAME=x86_64 OS_ARCH_NAME=amd64`.
More background is in [docs/NOTES.md](docs/NOTES.md), and planned work is in
[docs/TODO.md](docs/TODO.md).

## AI Use

AI (Claude Code) is used in this project for Git management and documentation
writing. All functional code is written by hand. If you used AI tools in a
contribution, please mention it in the pull request.
