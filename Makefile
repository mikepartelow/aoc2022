lint:
	flake8 --max-line-length 120 .
	pylint --recursive y .

fmt:
	black .

SUBDIRS := $(wildcard day*/.)
test: $(SUBDIRS)
$(SUBDIRS):
	cd $@ && python ./a.py

.PHONY: test $(SUBDIRS)