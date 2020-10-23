THIS_MAKEFILE = $(abspath $(firstword $(MAKEFILE_LIST)))
SRC_ROOT := $(shell dirname ${THIS_MAKEFILE})

test:
	python -m unittest
