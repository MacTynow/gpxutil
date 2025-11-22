.PHONY: test build clean install

all: build

clean:
	rm -rf *.gpx

test:
	uv run pytest

build:
	uv build

install:
	pipx install dist/gpxutil-*.whl