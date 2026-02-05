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
