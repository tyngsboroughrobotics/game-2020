.DEFAULT_GOAL := deploy

SSH=ssh -t root@pepper.local
PROJECT_ROOT=/home/root/Documents/KISS/Default\ User/ths-botball-2019

init:
	git submodule init

update-botball:
	git submodule update --remote botball

build:
	# Remove any old files
	rm -rf _build/
	rm -rf botball/_py2_build/

	mkdir _build/

	# Build Botball for Python
	cd botball; make build-for-py2; cd ..
	mv botball/_py2_build/ _build/botball/

	# Build Game
	py-backwards -i src/ -o _build/src/ -t 2.7
	cp __main__.py _build/

install:
	# Remove any old files
	${SSH} "rm -rf ${PROJECT_ROOT}"

run:
	echo "TODO: Run file on wallaby (eg. botball_user_program)"

deploy:
	make build
	make install
	make run
