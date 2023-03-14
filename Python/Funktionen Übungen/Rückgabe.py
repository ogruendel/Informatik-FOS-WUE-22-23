def make_greeting(name):
    return 'Hi ' + name + '!'


def compute(x, y):
    total = x + y
    if total > 10:
        total = 10
    return total


def allow_access(person):
    if person == "Dr Evil":
        answer = True
    else:
        answer = False
    return answer
