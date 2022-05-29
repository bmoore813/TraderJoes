
.PHONY: venv
venv:
	python -m venv venv

.PHONY: activate
activate:
	source venv/bin/activate

.PHONY: deactivate
deactivate:
	deactivate

requirements.txt: requirements.in # update requirements.txt
	@echo '==> updating requirements.txt'
	@pip-compile --upgrade --output-file requirements.txt requirements.in

update:
	pip install -r requirements.txt