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
	python -m isort app
	python -m black app
	python -m isort tests
	python -m black tests
	python -m mypy --config-file=./mypy.ini app
	python -m mypy --config-file=./mypy.ini tests
	python -u -m pytest tests -vv
