.PHONY: test

test:
	while inotifywait -e close_write *.py ; do python -m pytest test_wordstime.py ; done
