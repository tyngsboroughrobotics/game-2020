import sys; sys.path.insert(0, "/home/root/Documents/KISS/Default User/botball-game/_botball_build")

from botball.core.helpers.choose_game_procedure import RobotConfig

if __name__ == "__main__":
    config = RobotConfig()

    if config.robot_type == "demobot":
        from src.demobot_procedure import procedure
    else:
        from src.create_procedure import procedure

    procedure.run(
        debug=config.debug_enabled
    )
