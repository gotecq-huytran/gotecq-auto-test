# Makefile

VENV_DIR := venv
ACTIVATE := source $(VENV_DIR)/bin/activate

.PHONY: test

active: 
	${ACTIVATE}
test:
	${ACTIVATE} && pytest -v test_suits/
