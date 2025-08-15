# Makefile
ROOT_DIR = .
VENV_DIR := venv
ACTIVATE := source $(VENV_DIR)/bin/activate
TEST_DIR := __test__
SRC_DIR := src
.PHONY: test

active: 
	${ACTIVATE}
test:
	${ACTIVATE} && pytest -v -s ${ROOT_DIR}/${SRC_DIR}/${TEST_DIR}

