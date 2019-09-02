HOSTNAME=root@pepper.local
SSH=ssh -t ${HOSTNAME}
PROJECT_ROOT=/home/root/Documents/KISS/Default\ User/botball-game
PROJECT_ROOT_SCP="/home/root/Documents/KISS/Default\\ User/botball-game"
EXECUTABLE=_build/bin/botball_user_program
CONFIG_DIRECTORY=/etc/ths-botball-conf

init:
	git submodule init

update-botball:
	git submodule update --remote botball

ssh:
	@${SSH} 2> /dev/null

configure-as-demobot:
	${SSH} "mkdir -p ${CONFIG_DIRECTORY}; touch ${CONFIG_DIRECTORY}/demobot"

configure-as-create:
	${SSH} "mkdir -p ${CONFIG_DIRECTORY}; touch ${CONFIG_DIRECTORY}/create"

configure-debug-enable:
	${SSH} "mkdir -p ${CONFIG_DIRECTORY}; touch ${CONFIG_DIRECTORY}/debug"

configure-debug-disable:
	${SSH} "mkdir -p ${CONFIG_DIRECTORY}; rm -f ${CONFIG_DIRECTORY}/debug"

clean:
	@rm -rf _build/
	@rm -rf botball/_py2_build/

__build-file: # call using `make __build-file file=path/to/file`
	@python3 -m lib3to6 $(file) --in-place

build:
	@make clean
	@mkdir -p _build/src/
	@mkdir -p _build/bin/
	@mkdir -p _build/_botball_build/

	@# Build Botball for Python
	@cd botball; make build; cd ..
	@mv botball/_py2_build/* _build/_botball_build/

	@# Build Game
	@cp -r src/ _build/src/
	@find _build/src/ -name "*.py" -exec make __build-file file='{}' \; >/dev/null
	@cp __main__.py _build/__main__.py
	@make __build-file _build/__main__.py >/dev/null

	@# Create executable
	@touch ${EXECUTABLE}
	@echo "#!/bin/bash\n/usr/bin/python ${PROJECT_ROOT}/__main__.py" > ${EXECUTABLE}
	@chmod +x ${EXECUTABLE}

install:
	@# Remove any old files
	@${SSH} "rm -rf ${PROJECT_ROOT}; mkdir -p ${PROJECT_ROOT}"

	@# Copy build folder
	@scp -C -r _build/* botball-game.project.json ${HOSTNAME}:${PROJECT_ROOT_SCP}

run:
	@${SSH} "echo; ${PROJECT_ROOT}/bin/botball_user_program"

deploy:
	@echo "[botball-dev] Building project"
	@make build &> /dev/null

	@echo "[botball-dev] Installing to robot"
	@make install &> /dev/null

	@echo "[botball-dev] Running program"
	@make run
