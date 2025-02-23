# write a makefile that compiles the main.py to cnm, and then copy it to /usr/bin

.PHONY: all install

all: cnm

cnm: main.py
	@echo "Compiling main.py to cnm"
	cp ./main.py ./cnm.py
	pyinstaller --onefile cnm.py

install: ./dist/cnm
	sudo cp ./dist/cnm /usr/bin/cnm

clean:
	@echo "Cleaning up"
	rm -rf ./dist
	rm -rf ./build
	rm -rf ./cnm.py
	rm -rf ./cnm.spec

