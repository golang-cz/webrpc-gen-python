all:
	@echo "please read Makefile source or README to see available commands"

clean:
	rm -rf __pycache__

requirements:
	pip install -r requirements.txt

generate:
	webrpc-gen -schema=service.ridl -target=../../ -server=flask -out=./server.py
	webrpc-gen -schema=service.ridl -target=../../ -client -out=./client.py -server

run-server:
	python app.py