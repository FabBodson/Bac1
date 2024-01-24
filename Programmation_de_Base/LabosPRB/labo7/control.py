import turtle


SET_PEN_COLOR = 1
SET_FILL_COLOR = 2
ROTATE_LEFT = 3
ROTATE_RIGHT = 4
MOVE_FORWARD = 5
START_DRAW = 6
STOP_DRAW = 7
START_FILL = 8
STOP_FILL = 9
SET_POSITION = 10
SET_DIRECTION = 11


def __compile_color(color):
    assert type(color) == tuple, f'Une couleur doit être exprimée sous la forme d\'un tuple: (rouge, vert, bleu), et non d\'un [{type(color)}].'
    for item in color:
        assert 0.0 <= item <= 1.0, f'La valeur d\'une composante de couleur doit être comprise entre 0.0 et 1.0, et non [{item}].'
    return color


def __compile_angle(angle):
    assert type(angle) in (float, int), f'La valeur d\'un angle doit être exprimée en int ou float, et non [{angle}].'
    assert 0 <= angle <= 360, f'La valeur d\'un angle doit être comprise entre 0 et 360, et non [{angle}].'
    return angle


def __compile_set_color(command):
    assert len(command) == 2, f'La commande [{command[0]}] doit recevoir 1 argument: couleur (tuple[rouge, vert, bleu]).'
    color = __compile_color(command[1])
    return color,


def __compile_rotate(command):
    assert len(command) == 2, f'La commande [{command[0]}] doit recevoir 1 argument: angle (int ou float).'
    angle = __compile_angle(command[1])
    return angle,


def __compile_move_forward(command):
    assert len(command) == 2, f'La commande [{command[0]}] doit recevoir 1 argument: distance (int).'
    distance = command[1]
    assert type(distance) == int, f'La valeur d\'une distance doit être exprimée en int, et non en [{type(distance)}].'
    return distance,


def __compile_set_position(command):
    assert len(command) == 2, f'La commande [{command[0]}] doit recevoir 1 argument: position (tuple[int, int]).'
    position = command[1]
    assert len(position) == 2, 'La position doit être exprimée sous la forme d\'un tuple d\'entiers définissant les coordonnées (x, y).'
    assert type(position[0]) == int, f'La valeur d\'une coordonnée doit être exprimée en int, et non en [{type(position[0])}].'
    assert type(position[1]) == int, f'La valeur d\'une coordonnée doit être exprimée en int, et non en [{type(position[1])}].'
    return position


def __compile_set_direction(command):
    assert len(command) == 2, f'La commande [{command[0]}] doit recevoir 1 argument: angle (int ou float).'
    angle = __compile_angle(command[1])
    return angle,


def __compile_no_arguments(command):
    assert len(command) == 1, f'La commande [{command[0]}] n\'accepte aucun argument.'
    return []


def __build_action_dictionary():
    return {
        SET_PEN_COLOR: (__compile_set_color, turtle.pencolor),
        SET_FILL_COLOR: (__compile_set_color, turtle.fillcolor),
        ROTATE_LEFT: (__compile_rotate, turtle.left),
        ROTATE_RIGHT: (__compile_rotate, turtle.right),
        MOVE_FORWARD: (__compile_move_forward, turtle.forward),
        START_DRAW: (__compile_no_arguments, turtle.pendown),
        STOP_DRAW: (__compile_no_arguments, turtle.penup),
        START_FILL: (__compile_no_arguments, turtle.begin_fill),
        STOP_FILL: (__compile_no_arguments, turtle.end_fill),
        SET_POSITION: (__compile_set_position, turtle.setpos),
        SET_DIRECTION: (__compile_set_direction, turtle.setheading),
    }


def __compile_command(command, action_dictionary):
    assert len(command) > 0, f'Aucune commande spécifiée dans la commande [{command}].'
    command_name = command[0]
    assert command_name in action_dictionary, f'La commande [{command_name}] n\'existe pas.'
    argument_compiler, function = action_dictionary[command_name]
    arguments = argument_compiler(command)
    return function, arguments


def __compile(scenario, action_dictionary):
    return [__compile_command(command, action_dictionary) for command in scenario]


def play(scenario, speed='slow'):
    """
    Cette fonction va piloter la tortue en respectant les différentes commandes contenues dans le scénario.
    :param scenario: list, une liste contenant les actions à réaliser par la tortue
    :param speed: str, vitesse de déplacement de la tortue. Les modes sont: slowest, slow, normal, fast, fastest
    """

    turtle.shape("turtle")
    turtle.speed(speed)

    action_dictionary = __build_action_dictionary()
    actions = __compile(scenario, action_dictionary)
    for action in actions:
        function, arguments = action
        function(*arguments)
    turtle.done()
