
MAIN_FILE = src/main.py

RUN = python

install:
	pip install -r requirements.txt

run:
	$(RUN) $(MAIN_FILE)


