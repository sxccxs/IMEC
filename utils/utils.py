from sympy import Basic, Symbol


class Utils:
    @staticmethod
    def is_valid_float(value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def get_variables_from_expression(expression: Basic) -> list[Symbol]:
        """Returns list of symbols for given sympy expression."""
        return sorted(list(expression.free_symbols), key=lambda x: x.name)
