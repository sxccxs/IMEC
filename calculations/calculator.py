import sympy as sp
from sympy import Float, Basic, Symbol


class Calculator:
    def __init__(self, float_length: int, tnp: float):
        self.float_length = float_length
        self.tnp = tnp

    def calculate_formula(self, expr: Basic, avg_values: dict[Symbol, Float]) -> Float:
        """Calculates expression with given values."""
        return expr.evalf(self.float_length, subs=avg_values)

    def calculate_avg(self, values: list[Float]) -> Float:
        """Calculates average value for given list of values."""
        return Float(sum(values) / len(values))

    def calculate_sigma(self, values: list[Float], avg_value: Float) -> Float:
        """
        Calculates sigma coefficient for calculation of measurement error.
        Fromula:
            σ = (∑ (xᵢ - <x>)²) / (n * (n-1))
        """
        n = len(values)
        return sp.sqrt(sum([(x - avg_value) ** 2 for x in values]) / (n * (n - 1)))

    def calculate_error_for_variable(
        self, measurements: list[Float], avg_value: Float
    ) -> Float:
        """
        Calculates measurements error for given values.
        Formula:
            ΔX = σ * tnp
        """
        return self.calculate_sigma(measurements, avg_value) * self.tnp

    def calculate_result_error(
        self,
        expr: Basic,
        errors: dict[Symbol, Float],
        avg_values: dict[Symbol, Float],
        vars: list[Symbol],
    ) -> Float:
        """
        Calculates indirect error for given formula and values.
        Formula:
            ∆f = √∑(∂f/∂yᵢ * ∆yᵢ)²
        """
        res_error = 0
        for var in vars:
            deriv = expr.diff(var).evalf(self.float_length, subs=avg_values)
            res_error += (deriv * errors[var]) ** 2
        res_error = sp.sqrt(res_error)
        return res_error
