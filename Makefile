install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint hello.py, test_hello.py

format:
	black *.py

test:
	python -m pytest -vv --cov=hello test_hello.py