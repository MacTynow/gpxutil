.PHONY: test build clean cli

clean:
	rm -rf *.gpx

cli:
	uv run cli.py ./test_data/activity_1.gpx ./test_data/activity_2.gpx

api:
	uv run fastapi dev api.py

test:
	uv run pytest

build:
	uv build