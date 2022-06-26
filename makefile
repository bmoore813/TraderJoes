
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
	make update


update-pip:
	pip install --upgrade pip

update: update-pip
	pip install -r requirements.txt

dashboard:
	streamlit run app/dashboards/real_time.py