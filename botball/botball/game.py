from .helpers import Timer


class Game(object):
    '''
    "Games" are abstractions over the code controlling the robot in order to
    execute the strategy. Games have a name and a list of "steps" that allow you
    to break up the implementation of your strategy into multiple pieces and
    reuse code. It's recommended to use steps and games instead of just writing
    your code at the top level, so it's easier to debug.

    The easiest way to create a `Game` is to use the `game_from_module` function,
    which automatically converts all functions beginning with `step_` in the
    current file to `Step` objects:

        # In 'demobot.py':

        def step_move_forward():
            ...

        def step_grab_block():
            ...

        # In another file:

        import demobot
        game = game_from_module(demobot)

        game.name == 'demobot'
        game.steps == [
            Step(name='move forward', function=demobot.step_move_forward),
            Step(name='grab block', function=demobot.step_grab_block),
        ]

    To run a game, call the `run()` method, which executes all steps and logs
    the total duration of the game, allowing you to ensure your code runs under
    the time limit.
    '''

    def __init__(self, name, steps):
        '''
        Create a new game with the specified name and list of steps.
        '''

        self.name = name
        self.steps = steps

    def run(self):
        '''
        Execute all the steps in the game in order, and log the total duration.
        '''

        print(f'Running game "{self.name}" ({len(self.steps)} steps)\n')

        timer = Timer()

        for step in self.steps:
            step.run()
            print()

        print(f'Finished game "{self.name}" in {timer.time_elapsed} seconds')


class Step(object):
    '''
    "Steps" are abstractions over a specific action the robot must execute in
    your strategy. It's recommended to split up your strategy into as many steps
    as possible to make it easy to read and debug.

    Steps are used with `Game` objects to run your code, but they can also be
    called individually with the `run()` method.
    '''

    def __init__(self, name, function):
        '''
        Create a new step with the specified name and function, which will be
        called when the step runs.
        '''

        self.name = name
        self.function = function

    def run(self):
        '''
        Execute the step and log the total duration.
        '''

        print(f'    Running step "{self.name}"')

        timer = Timer()

        self.function()

        print(f'    Finished step "{self.name}" in {timer.time_elapsed} seconds')


def choose_game(robot_name, games):
    '''
    Given a list of games, choose the game whose name matches `robot_name`.
    Throws an exception if there is no such game. This is used to easily choose
    the correct game from the current `RobotConfiguration`, so no code
    modifications are required to run different games on different robots.
    '''

    matching_game = None

    for game in games:
        if game.name == robot_name:
            matching_game = game

    assert matching_game is not None, \
        f'No game found for robot name {robot_name}'

    return matching_game


def game_from_module(name, module):
    '''
    Creates a `Game` object whose whose steps are the functions in the module
    beginning with `step_`.

    Example:

        # In 'demobot.py':

        def step_move_forward():
            ...

        def step_grab_block():
            ...

        # In another file:

        import demobot
        game = game_from_module('demobot', demobot)

        game.name == 'demobot'
        game.steps == [
            Step(name='move forward', function=demobot.step_move_forward),
            Step(name='grab block', function=demobot.step_grab_block),
        ]

    This function assumes that the step functions are declared in the order they
    should be executed. If you want any additional configuration, just manually
    create `Step` and `Game` objects.
    '''

    from inspect import getmembers, isfunction

    # Obtain the functions in module beginning with 'step_', in source code order
    fns = dict(getmembers(module, isfunction))
    step_fns = sorted(fns.values(), key=lambda fn: fn.__code__.co_firstlineno)
    step_fns = [fn for fn in step_fns if fn.__name__.startswith('step_')]

    # Convert a 'step_' function name to an English step name by removing the
    # prefix and other underscores
    def step_name_from(fn_name):
        step_name = fn_name.replace('step_', '', 1)
        step_name = step_name.replace('_', ' ')
        return step_name

    # Convert the functions to Step objects
    steps = [Step(step_name_from(fn.__name__), fn) for fn in step_fns]

    # Create a Game from the steps
    game = Game(name, steps)

    return game
