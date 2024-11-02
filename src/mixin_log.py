class MixinLog:
    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})"

    def __init__(self, *args, **kwargs) -> None:
        print(repr(self))
