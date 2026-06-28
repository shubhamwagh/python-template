# mypackage

> One-line description of what this project does.

## Overview

Short paragraph: the problem, the approach, and the high-level architecture.

```
src/mypackage/   # package source (src-layout)
  core.py        # core logic
  cli.py         # command-line entry point
tests/           # pytest suite
```

## Requirements

- [uv](https://docs.astral.sh/uv/) (package + Python version manager)
- Python 3.12–3.13 (auto-installed by uv via `.python-version`)

## Quick start

```bash
# 1. Install deps + pre-commit hooks
make install

# 2. Run the CLI
uv run mypackage 2 3      # -> 5
```

## Development

```bash
make lint      # ruff check
make format    # ruff format + autofix
make test      # pytest + coverage
make hooks     # run all pre-commit hooks
make clean     # remove caches/artifacts
```

Pre-commit runs ruff lint + format on every commit (`make install` sets it up).

## Conventions

- **Package manager:** `uv` (lockfile `uv.lock` is committed).
- **Build backend:** `hatchling`, src-layout.
- **Lint/format:** `ruff` — line-length 79, 2-space indent, double quotes,
  single-line imports, google docstrings. Config lives in `pyproject.toml`.
- **Tests:** `pytest` under `tests/`, coverage on `mypackage`.
- **CI:** GitHub Actions (`.github/workflows/ci.yml`) — lint, format check, test.

## Build the Docker image

```bash
docker build -t mypackage .
docker run --rm mypackage 2 3
```

## Using this template

1. Copy the folder, rename it.
2. Rename `src/mypackage` and update every `mypackage` reference in
   `pyproject.toml`, `Makefile`, `Dockerfile`, `.github/workflows/ci.yml`,
   and `tests/`.
3. `uv lock` to generate `uv.lock`, then `make install`.
4. Replace this README.
