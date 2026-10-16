# Security Policy

This is a personal repository of self-study work and isn't intended for
production use. There are no versioned releases, and only the latest state of
`main` is supported.

## Known Issues

The `Dockerfile` builds on `debian:13`, which currently carries a known zlib
vulnerability with no fixed version available
([CVE-2026-85091](https://scout.docker.com/vulnerabilities/id/CVE-2026-85091?s=debian&n=zlib&ns=debian&t=deb&osn=debian&osv=13&vr=%3E0)).
This is tracked in `docs/NOTES.md` and will be revisited when a fix is released.
