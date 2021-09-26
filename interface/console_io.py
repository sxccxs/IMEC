import sympy as sp
from sympy import Symbol, Basic
from typing import Optional, Union
from utils.converter import Converter
from utils.utils import Utils


Number = Union[int, float, sp.Float, sp.Integer]


class ConsoleIO:
    def __init__(self, prefix_in: str = "<-", prefix_out: str = "->"):
        self.prefix_in = prefix_in
        self.prefix_out = prefix_out

    def print(self, value: str):
        print(f"{self.prefix_out} {value}")

    def input(self, value: str) -> str:
        return input(f"{self.prefix_in} {value}")

    def print_name_value_with_10_power(self, name: str, value: Number, power_of_10: int = 0):
        """
        Outputs given values to console in format {name = value  * 10 ^ power_of_10}.
        The value will be multiplied by 10 ^ power_of_10.
        """
        self.print(f"{name} = {value * 10 ** power_of_10} * 10 ^ ({-power_of_10})")

    def print_name_value(self, name: str, value):
        """Outputs given values to console in format {name = value}."""
        self.print(f"{name} = {value}")

    def read_answer_for_yes_no(self, question: str) -> bool:
        """Asks user the given question and returns True if answer is yes else no."""
        inp = self.input(question)
        return inp.lower() == "yes"

    def read_and_print_float_length(self, default: int) -> int:
        """
        Asks user to enter amount of digits after comma in float values.
        if answer is valid then outputs the float length value to the console.
        Else asks user to enter a valid one.
        """
        while True:
            inp = self.input(
                f"Enter amount of digits after comma or left blank for default {default}: "
            )
            if inp == "":
                self.print(f"Float length is set to {default}")
                return default
            elif inp.isdigit() and (x := int(inp)) > 0:
                self.print(f"Float length is set to {x}")
                return x
            else:
                self.print("Provided value is not valid")

    def read_and_print_tnp(self) -> float:
        """
        Asks user to enter tnp coefficient.
        if answer is valid then outputs tnp value to the console.
        Else asks user to enter a valid one.
        """
        while True:
            inp = self.input(f"Enter tnp: ")
            if Utils.is_valid_float(inp):
                x = float(inp)
                self.print(f"tnp is set to {x}")
                return x
            else:
                self.print("Provided value is not valid")

    def read_formula(self) -> str:
        """Asks user to enter a formula and returns it."""
        formula = self.input("Enter formula after '=' sign: ")
        return formula

    def read_avg_values_for_variables(self, vars: list[Symbol]) -> dict[Symbol, str]:
        """
        Asks user to enter average values for every variable in {vars}.
        Then return dict of values.
        Calls self._read_avg_value_for_variable for every variable.
        """
        avg_values: dict[Symbol, str] = {}
        for var in vars:
            avg_value = self._read_avg_value_for_variable(var)
            if avg_value is not None:
                avg_values[var] = avg_value
        return avg_values

    def _read_avg_value_for_variable(self, var_name: Symbol) -> Optional[str]:
        """
        Asks user to enter an average value for given symbol.
        If value is not valid, asks user to enter a valid one.
        """
        while True:
            avg_val = self.input(
                f"Enter average value for {var_name} or leave blank if it needs to be calculated: "
            )
            if not avg_val:
                return None
            elif Utils.is_valid_float(avg_val):
                return avg_val
            else:
                self.print("Provided value is invalid.")

    def read_measurements_for_variables(self, vars: list[Symbol]) -> dict[Symbol, list[str]]:
        """
        Asks user to enter measurements values for every variable in {vars}.
        Then return dict of values.
        Calls self._read_measurements_for_variable for every variable.
        """
        measurements: dict[Symbol, list[str]] = {}
        for var in vars:
            measurs = self._read_measurements_for_variable(var)
            if measurs is not None:
                measurements[var] = measurs
        return measurements

    def _read_measurements_for_variable(self, var_name: Symbol) -> list[str]:
        """
        Asks user to enter an measurements values for given symbol.
        If values are not valid, asks user to enter a valid ones.
        """
        while True:
            measurements = self.input(
                f"Enter measurements values for {var_name} separated by spaces: "
            ).split()
            if all([Utils.is_valid_float(i) for i in measurements]):
                # If all measurements are valid float
                return measurements
            else:
                self.print("Provided values are invalid.")

    def read_error_for_variables(self, vars: list[Symbol]) -> dict[Symbol, str]:
        """
        Asks user to enter measurements error value for every variable in {vars}.
        Then return dict of values.
        Calls self._read_error_for_variable for every variable.
        """
        errors: dict[Symbol, str] = {}
        for var in vars:
            error_val = self._read_error_for_variable(var)
            if error_val is not None:
                errors[var] = error_val
        return errors

    def _read_error_for_variable(self, var_name: str) -> Optional[str]:
        """
        Asks user to enter an measurements error value for given symbol.
        If value is not valid, asks user to enter a valid one.
        """
        while True:
            error_val = self.input(
                f"Enter error value for {var_name} or leave blank if it needs to be calculated: "
            )
            if not error_val:
                return None
            elif Utils.is_valid_float(error_val):
                return error_val
            else:
                self.print("Provided value is invalid.")
