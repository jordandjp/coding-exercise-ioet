test:
	python3 -m unittest discover -s tests
	python3 -m doctest docs/daytime.doctest
	python3 -m doctest docs/timeslot.doctest