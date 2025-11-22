.PHONY: test build clean install

all: build

clean:
	rm -rf *.gpx

test:
	uv run pytest

build:
	uv build

install:
	pipx install dist/merge_gpx-0.1.0-py3-none-any.whl