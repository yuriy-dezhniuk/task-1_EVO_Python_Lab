class TurnStepError(Exception):
    """Raised when the turn value is not divisible by turn step (45)"""
    pass


class TurnLimitError(Exception):
    """Raised when the turn value is outside of turn limit (-1080, 1080)"""
    pass


def direction(facing, turn):
    directions = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    turn_limit = (-1080, 1080)
    turn_step = 45
    try:
        if turn % turn_step != 0:
            raise TurnStepError
        elif turn < turn_limit[0] or turn > turn_limit[1]:
            raise TurnLimitError
        if turn >= 360:
            turn %= 360
        elif turn <= -360:
            turn %= -360
        facing_index = directions.index(facing)
        turn_step_counts = turn / turn_step
        index = int(facing_index + turn_step_counts)
        new_facing_index = index if index < len(directions) else index % len(directions)
        return directions[new_facing_index]
    except ValueError:
        print('Incorrect facing value. Please, use one of this values:', ', '.join(directions))
    except TurnStepError:
        print('Turn value should be divisible by', turn_step)
    except TurnLimitError:
        print(f'Turn value should be within the range from {turn_limit[0]} to {turn_limit[1]}')
