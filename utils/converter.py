import sympy as sp
from sympy import Symbol, Basic, Float


class Converter:
    @staticmethod
    def formula_to_expression(formula: str) -> Basic:
        """
        Converts string formula to sympy expression.
        Uses sympy.sympify().
        """
        return sp.sympify(formula)

    @staticmethod
    def measurements_values_to_float(
        measurement_values: dict[Symbol, list[str]], float_length: int
    ) -> dict[Symbol, list[Float]]:
        """
        Converts all measurements values from given dict to sympy.Float .
        Makes a copy of given dict.
        """
        measurement_values = measurement_values.copy()
        for key, value in measurement_values.items():
            measurement_values[key] = [Float(i, float_length) for i in value]
        return measurement_values

    @staticmethod
    def dict_symbol_str_to_float(
        values: dict[Symbol, str], float_length: int
    ) -> dict[Symbol, Float]:
        """
        Converts all values from given dict to sympy.Float .
        Makes a copy of given dict.
        """
        values = values.copy()
        for key, value in values.items():
            values[key] = Float(value, float_length)
        return values
