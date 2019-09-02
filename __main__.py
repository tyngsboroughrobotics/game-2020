import sys; sys.path.insert(0, "/home/root/Documents/KISS/Default User/botball-game/_botball_build")

from botball.core import choose_game_procedure
from src import demobot_procedure, create_procedure

if __name__ == "__main__":
    procedure_run = choose_game_procedure(
        demobot=demobot_procedure.procedure,
        create=create_procedure.procedure
    )

    # TODO: wait_for_light if debug enabled

    procedure_run()
