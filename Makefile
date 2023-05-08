
manage_py := python app/manage.py

run:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

testdata:
	$(manage_py) test_data

worker:
	cd app && celery -A settings worker -l info -c 4 --pool threads

beat:
	cd app && celery -A settings beat -l info

pytest:
	pytest ./app/tests --cov=app --cov-report html && coverage report --fail-under=70.7754