.PHONY: all generate diff

all: generate diff

generate:
	cd hello-webrpc && make generate

diff:
	git diff --color --ignore-all-space --ignore-blank-lines --exit-code 