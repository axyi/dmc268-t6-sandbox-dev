def greet(name: str) -> str:
    """Return a greeting for the #144 e2e."""
    return f"hello, {name}"


def farewell(name: str) -> str:
    return f"bye, {name}"


def shout(name: str) -> str:
    return greet(name).upper()


def whisper(name: str) -> str:
    return greet(name).lower()


def echo(name: str) -> str:
    return name
