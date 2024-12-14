class Natural:
    def __init__(self, value) -> None:
        match value:
            case int():
                if value < 0:
                    raise ValueError('value must 0 or greater')
                self.__v = value
            case Natural():
                self.__v = value.__v
            case _:
                raise ValueError('incompatible type')

    def __str__(self) -> str:
        return str(self.__v)

    def __repr__(self) -> str:
        return f'Natural({self.__v})'

    def __lt__(self, other) -> bool:
        return self.__v < Natural(other).__v

    def __eq__(self, other) -> bool:
        return self.__v == Natural(other).__v

    def __le__(self, other) -> bool:
        return (self < other) or (self == other)

    def __ne__(self, other) -> bool:
        return not self == other

    def __gt__(self, other) -> bool:
        return not self <= other

    def __ge__(self, other) -> bool:
        return not self < other

    def __hash__(self) -> int:
        return hash(self.__v)

    def __bool__(self) -> bool:
        return bool(self.__v)
