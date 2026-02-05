# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python project managed with [uv](https://docs.astral.sh/uv/) (not pip/poetry). Python 3.13+ is required.

## Commands

- **Install dependencies:** `uv sync`
- **Run the app:** `uv run main.py`
- **Add a dependency:** `uv add <package>`
- **Launch JupyterLab:** `uv run jupyter lab`

## Structure

- `main.py` — Application entry point
- `pyproject.toml` — Project metadata and dependencies (uv/PEP 621 format)
- `uv.lock` — Locked dependency versions (do not edit manually)
- `.python-version` — Pinned Python version (3.13)
