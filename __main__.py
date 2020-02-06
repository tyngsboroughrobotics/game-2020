from game import demobot
from botball import *

if __name__ == "__main__":
    print("\n\n@@ Press Ctrl+C to stop the program. @@")

    choose_game_procedure(procedure_map={
        demobot.procedure.name: demobot.procedure,
    })()
