check:
	python master.py > this_time.txt
	diff this_time.txt golden_master.txt

coverage:
	coverage run master.py >/dev/null
	coverage report
	coverage html

init:
	virtualenv -p /usr/bin/python virtualenv