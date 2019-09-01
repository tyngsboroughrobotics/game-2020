from botball.core import *
from .src import *

if __name__ == "__main__":
    procedure_run = choose_game_procedure(
        demobot=demobot_procedure.procedure,
        create=create_procedure.procedure
    )

    procedure_run()
