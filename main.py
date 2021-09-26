from sympy import Float, Basic, Symbol
from interface.console_io import ConsoleIO
from calculations.calculator import Calculator
from utils.converter import Converter
from utils.utils import Utils

DEFAULT_FLOAT_LENGTH = 15


class Main:
    expression: Basic
    expression_result: Float
    expression_error: Float
    console: ConsoleIO
    calculator: Calculator
    converter: Converter
    variables: list[Symbol]
    avg_values: dict[Symbol, Float]
    measurements: dict[Symbol, list[Float]]
    errors: dict[Symbol, Float]

    def __init__(self):
        self.console = ConsoleIO()
        self.converter = Converter()
        float_length = self.console.read_and_print_float_length(DEFAULT_FLOAT_LENGTH)
        tnp = self.console.read_and_print_tnp()
        self.calculator = Calculator(float_length, tnp)

    def read_data(self):
        """Reads needed data from self.console ."""
        self._read_expression()
        self._set_variables()
        self._read_avg_values()
        self._read_measurements()
        self._read_errors()

    def calculate(self):
        """Calculates results."""
        self._calculate_avg_values()
        self._calculate_errors()
        self._calculate_expression_result()
        self._calculate_expression_error()

    def run(self):
        """Runs the program."""
        self.read_data()
        self.calculate()
        self.console.print_name_value_with_10_power(
            "formula result", self.expression_result, 5
        )
        for key, value in self.avg_values.items():
            self.console.print_name_value(f"avg value of {key}", value)
        for key, value in self.errors.items():
            self.console.print_name_value_with_10_power(f"error for {key}", value, 5)
        self.console.print_name_value_with_10_power("formula error", self.expression_error, 5)
        input()  # To pause compiled program after execution.

    def _calculate_expression_error(self):
        """Calculates the expression error using self.calculator ."""
        self.expression_error = self.calculator.calculate_result_error(
            self.expression, self.errors, self.avg_values, self.variables
        )

    def _calculate_expression_result(self):
        """Calculates the expression result using self.calculator ."""
        self.expression_result = self.calculator.calculate_formula(
            self.expression, self.avg_values
        )

    def _calculate_errors(self):
        """Calculates measurements errors for self.variables using self.calculator ."""
        for var in self.variables:
            if var not in self.errors:
                self.errors[var] = self.calculator.calculate_error_for_variable(
                    self.measurements[var], self.avg_values[var]
                )

    def _calculate_avg_values(self):
        """
        Calculates average values for self.variables,
           which haven't been provided, based on self.measurements.
        Uses self.calculator.
        """
        for var in self.variables:
            if var not in self.avg_values:
                self.avg_values[var] = self.calculator.calculate_avg(self.measurements[var])

    def _read_errors(self):
        """Reads measurements error from self.console ."""
        self.errors = self.converter.dict_symbol_str_to_float(
            self.console.read_error_for_variables(self.variables), self.calculator.float_length
        )

    def _read_avg_values(self):
        """Reads average values from self.console ."""
        self.avg_values = self.converter.dict_symbol_str_to_float(
            self.console.read_avg_values_for_variables(self.variables),
            self.calculator.float_length,
        )

    def _read_measurements(self):
        """Reads measurements from self.console ."""
        self.measurements = self.converter.measurements_values_to_float(
            self.console.read_measurements_for_variables(
                list(filter(lambda x: x not in self.avg_values, self.variables))
            ),
            self.calculator.float_length,
        )

    def _set_variables(self):
        """
        Sets self.variables to variables in self.expression.
        Uses Utils.get_variables_from_expression() .
        """
        if self.expression is not None:
            self.variables = Utils.get_variables_from_expression(self.expression)
        else:
            raise ValueError("self.variables does not exist.")

    def _read_expression(self):
        """
        Reads expression from self.console .
        Converts it to sympy expression using self.converter .
        Then asks the user if expression is correct.
        If not, repeats.
        """
        while True:
            self.expression = self.converter.formula_to_expression(self.console.read_formula())
            self.console.print_name_value("formula", self.expression)
            if self.console.read_answer_for_yes_no("Is formula valid [yes/no]: "):
                break


def main():
    app = Main()
    app.run()


if __name__ == "__main__":
    main()
