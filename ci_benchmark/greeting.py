from termcolor import colored


class Greeting:
    def __init__(self, name: str) -> None:
        self._name = name

    def greet(self) -> str:
        return "Hello " + colored(self._name, "green")
