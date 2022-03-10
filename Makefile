# EXAMPLE TO BE ADAPTED
.PHONY: setup_env
setup_env: clean
	virtualenv -p python3 venv
	. venv/bin/activate; pip install -e .[dev]

.PHONY: clean
clean:
	rm -rf venv
	rm -rf *.egg-info
	find . | grep -E "__pycache__|\.pyc|\.pyo$$|.pytest_cache|.mypy_cache" | xargs rm -rf

.PHONY: test
test:
	python -m isort pi_server
	python -m black pi_server
	python -m mypy pi_server
	python -u -m pytest -vv
