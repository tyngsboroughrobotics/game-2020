HOSTNAME=root@pepper.local
SSH=ssh -t ${HOSTNAME}
PROJECT_ROOT=/home/root/Documents/KISS/Default\ User/botball-game
PROJECT_ROOT_SCP="/home/root/Documents/KISS/Default\\ User/botball-game"
BOTBALL_SITE_PACKAGE="/usr/lib/python2.7/site-packages/botball"
EXECUTABLE=_build/bin/botball_user_program

ADD_ENVVAR_BEGIN=${SSH} "echo 'export
ADD_ENVVAR_END=' >> ~/.bashrc"

init:
	git submodule init

update-botball:
	git submodule update --remote botball

ssh:
	@${SSH} 2> /dev/null

configure-as-demobot:
	${ADD_ENVVAR_BEGIN} BOTBALL_USE_DEMOBOT=true ${ADD_ENVVAR_END}

configure-as-create:
	${ADD_ENVVAR_BEGIN} BOTBALL_USE_CREATE=true ${ADD_ENVVAR_END}

configure-debug-enable:
	${ADD_ENVVAR_BEGIN} BOTBALL_USE_DEBUG=true ${ADD_ENVVAR_END}

configure-debug-disable:
	${ADD_ENVVAR_BEGIN} BOTBALL_USE_DEBUG=false ${ADD_ENVVAR_END}

clean:
	@rm -rf _build/
	@rm -rf botball/_py2_build/

build:
	@make clean
	@mkdir -p _build/bin/

	# Build Botball for Python
	@cd botball; make build-for-py2; cd ..
	@mv botball/_py2_build/* _build/_botball_build/

	# Build Game
	@py-backwards -i src/ -o _build/src/ -t 2.7
	@cp __main__.py _build/

	# Create executable
	touch ${EXECUTABLE}
	echo "#!/bin/bash\n/usr/bin/python ${PROJECT_ROOT}/__main__.py" > ${EXECUTABLE}
	chmod +x ${EXECUTABLE}

install:
	@# Remove any old files
	@${SSH} "rm -rf ${PROJECT_ROOT}; mkdir -p ${PROJECT_ROOT}"

	@# Copy build folder
	@scp -C -r _build/* botball-game.project.json ${HOSTNAME}:${PROJECT_ROOT_SCP}

	@# Install Botball package on Wallaby
	@${SSH} "rm -rf ${BOTBALL_SITE_PACKAGE}; mv ${PROJECT_ROOT}/_botball_build ${BOTBALL_SITE_PACKAGE}"

run:
	@${SSH} "echo; ${PROJECT_ROOT}/bin/botball_user_program"

deploy:
	@echo "[botball-dev] Building project"
	@make build &> /dev/null

	@echo "[botball-dev] Installing to robot"
	@make install &> /dev/null

	@echo "[botball-dev] Running program"
	@make run
