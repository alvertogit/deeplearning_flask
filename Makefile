.PHONY: install test

default: test

install:
	pip install virtualenv \
	&& virtualenv dlflask36 \
	&& bash -c "source dlflask36/bin/activate" \
	&& pip install --no-cache-dir -r requirements.txt

test:
	bash -c "source dlflask36/bin/activate" \
	&& cd tests \
	&& pytest test.py
