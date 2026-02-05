# uv-test

A test project for [uv](https://docs.astral.sh/uv/), demonstrating dependency management and project setup with Python 3.13.

## Setup

```bash
uv sync
```

## Usage

```bash
uv run main.py
uv run main.py --url https://httpbin.org/json
```

## Development

```bash
uv run ruff check        # lint
uv run ruff format       # format
uv run pytest            # run tests
```

## Dependencies

- [arrow](https://arrow.readthedocs.io/) — date/time handling
- [click](https://click.palletsprojects.com/) — CLI framework
- [httpx](https://www.python-httpx.org/) — HTTP client
- [pydantic](https://docs.pydantic.dev/) — data validation
- [rich](https://rich.readthedocs.io/) — terminal formatting

## How This Project Was Built

This project was built step by step using [Claude Code](https://claude.ai/code) to demonstrate uv-based Python development.

**Project setup:**
- Initialized the repo with project files and a `CLAUDE.md` for AI-assisted development
- Created a GitHub repo and set `main` as the default branch

**Dependencies were added one at a time:**
- **httpx** — HTTP client for fetching JSON from an API
- **arrow** — human-friendly date/time formatting
- **rich** — colored and pretty-printed terminal output
- **click** — CLI framework with a `--url` option
- **pydantic** — data validation with typed models for the API response
- **pytest** (dev) — testing framework
- **ruff** (dev) — linter and formatter

**Code evolution:**
- `main.py` grew from a simple `print("Hello")` to a CLI app that fetches JSON, validates it with pydantic models, and displays formatted output
- Added 9 tests covering the pydantic models (valid data, defaults, validation errors)
- Set up GitHub Actions CI with lint and test jobs
