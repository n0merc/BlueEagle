.PHONY: install run test clean

install:
	pip install -r requirements.txt

run:
	sudo python3 blue_eagle_spammer.py

test:
	python3 -m pytest tests/

clean:
	rm -rf __pycache__/
	rm -rf *.log
	find . -name "*.pyc" -delete

docker-build:
	docker build -t blue-eagle .

docker-run:
	docker run --privileged -it blue-eagle
