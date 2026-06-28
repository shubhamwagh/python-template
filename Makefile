.PHONY: install lint format test clean hooks

install:  ## Sync deps + install pre-commit hooks
	uv sync --group dev
	uv run pre-commit install

hooks:  ## Run all pre-commit hooks on all files
	uv run pre-commit run --all-files

lint:  ## Lint with ruff
	uv run ruff check .

format:  ## Auto-format + fix imports
	uv run ruff format .
	uv run ruff check --fix .

test:  ## Run tests with coverage
	uv run pytest --cov=mypackage

clean:  ## Remove caches + build artifacts
	rm -rf .ruff_cache .pytest_cache test_results dist build .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
