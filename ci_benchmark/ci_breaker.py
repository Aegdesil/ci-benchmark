class CIBreaker:
    def __init__(self):
        pass

    @staticmethod
    def test():
        return 2 + ""

    def test_covered(self):
        return self.__class__.__name__
