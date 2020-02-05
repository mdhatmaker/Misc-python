# Makefile for opuslib.
#
# Author:: Никита Кузнецов <self@svartalf.info>
# Copyright:: Copyright (c) 2012, SvartalF
# License:: BSD 3-Clause License
#


.DEFAULT_GOAL := all

BUNDLE_EXEC ?= bundle exec

all: install_requirements develop

develop:
	python setup.py develop

install:
	python setup.py install

install_requirements:
	pip install --upgrade -r requirements.txt

uninstall:
	pip uninstall -y opuslib

clean:
	rm -rf *.egg* build dist *.py[oc] */*.py[co] cover doctest_pypi.cfg \
		nosetests.xml pylint.log *.egg output.xml flake8.log tests.log \
		test-result.xml htmlcov fab.log *.deb

publish:
	python setup.py register sdist upload

nosetests:
	python setup.py nosetests

pep8:
	flake8

flake8: install_requirements
	flake8 --ignore=E402,E731 --max-complexity 12 --exit-zero opuslib/*.py opuslib/api/*.py tests/*.py

lint: install_requirements
	pylint --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" \
	-r n opuslib/*.py opuslib/api/*.py tests/*.py || exit 0

test: lint flake8 nosetests

deploy_thor:
	$(BUNDLE_EXEC) scmversion bump auto --default patch
