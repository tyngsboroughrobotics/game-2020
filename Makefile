# - Configuration

.DEFAULT_GOAL := copy_and_run

IP_ADDRESS=pi@raspberrypi.local
SSH_PASSWORD="wallaby"

PROJECT_DIR=/home/root/Documents/KISS/Default\ User/botball-game
CONFIG_DIR=/etc/ths-botball-conf

SSHPASS=sshpass -p ${SSH_PASSWORD}

# - Transferring project files

copy_to_robot:
	${SSHPASS} rsync -a --delete -x -v \
		--exclude='/.git' --filter="dir-merge,- .gitignore" \
		--rsync-path="sudo rsync" \
		. ${IP_ADDRESS}:"${PROJECT_DIR}/"

delete_on_robot:
	${SSHPASS} ssh ${IP_ADDRESS} \
		"sudo rm -rf ${PROJECT_DIR}"

# - Running project on robot

run_on_robot:
	${SSHPASS} ssh ${IP_ADDRESS} \
		"${PROJECT_DIR}/bin/botball_user_program"

copy_and_run:
	make copy_to_robot
	make run_on_robot

# - Configuring robot settings

configure_robot_name:
	${SSHPASS} ssh ${IP_ADDRESS} \
		"sudo bash -c \"mkdir -p ${CONFIG_DIR}; touch ${CONFIG_DIR}/robot_type; echo '$(name)' > ${CONFIG_DIR}/robot_type\""

configure_debug_enabled:
	${SSHPASS} ssh ${IP_ADDRESS} \
		"sudo bash -c \"mkdir -p ${CONFIG_DIR}; touch ${CONFIG_DIR}/debug_enabled\""

configure_debug_disabled:
	${SSHPASS} ssh ${IP_ADDRESS} \
		"sudo rm ${CONFIG_DIR}/debug_enabled"
