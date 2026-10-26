# codeastro-mbw

My self-study work using the materials from the
[Code/Astro workshop](https://semaphorep.github.io/codeastro/), which are
published at [semaphoreP/codeastro](https://github.com/semaphoreP/codeastro).
I did not attend the workshop and am not affiliated with it. This is a personal
learning repository, not a polished package.

> **NOTE**: 
> AI (Claude Code) is used in this project for Git management and documentation writing to accelerate the work. All functional code is written by hand.

## What's here

- `Dockerfile`: a Debian 13 image with Miniconda, for a reproducible environment
  to work through the course materials in. Build it with `make docker-build`. It defaults to `aarch64`
  (for Intel/AMD, use
  `make docker-build MINICONDA_ARCH_NAME=x86_64 OS_ARCH_NAME=amd64`);
  see [docs/NOTES.md](docs/NOTES.md) for the build args that target other
  platforms.
- `course-materials/`: the unmodified workshop materials, one subdirectory per
  day (e.g. [`Day1/README.md`](course-materials/Day1/README.md)).
- `course-work/`: my own work done against the course materials, one
  subdirectory per day.
- `docs/`: installation notes and a [TODO](docs/TODO.md) list.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and the
[Code of Conduct](CODE_OF_CONDUCT.md).

## License

[BSD 3-Clause](LICENSE)
