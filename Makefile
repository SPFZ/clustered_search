update-requirements:
	pip freeze > requirements.txt

install-requirements:
	pip install -r requirements.txt

run:
	export FLASK_DEBUG=1
	python3 backend.py &
	python3 frontend.py &
	sleep 1
	echo "RUNNING!"

kill:
	-pkill -f "python3 backend.py"
	-pkill -f "python3 frontend.py"

rerun: kill run

pylint:
	find -name "*.py" -not -path "./.ENV/*" | xargs  .ENV/bin/pylint


.PHONY: update-requirements install-requirementsrun rerun kill pylint