SHELL = /bin/sh

USERS = foo bar bim baz
DOWNLOADS = downloads

all: setup

.PHONY: setup
setup: 
	for u in $USERS; do \
	    mkdir downloads; \
	    ./setup.py; \
	    mv downloads /home/$$u; \
	done
	    
