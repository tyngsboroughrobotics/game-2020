from botball import *

if __name__ == '__main__':
    from game import demobot, create

    game = choose_game(RobotConfiguration.robot_name(), [
        game_from_module('demobot', demobot),
        game_from_module('create', create),
    ])

    game.run()
