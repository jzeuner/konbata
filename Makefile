# INSTALL

install-dependencies:
	pip install -r requirements.txt

# RUN

run-flake8:
	flake8 .

run-tests:
	python3 -m unittest Tests/test_basic.py

run-code-coverage:
	coverage run --source='.' -m unittest Tests/test_basic.py -b

run-display-code-coverage:
	coverage report -m
