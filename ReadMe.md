# Indirect Measurements Error Calculatore(IMEC)

IMEC is a console-based calculator, created for computing measurements errors and then indirect error.

- It can evaluate formula with average values(which can be calculated or specified)
- Calculate measurements error for every variable in formula
- Compute indirect error for the formula

## How are calculations done

- Calculation of average values is simply made using formula **\<x> = ∑xᵢ / n**
- Then computation of measurements error is done using formula **∆x = σ \* tnp** , where tnp is a coefficient, specified by user and sigma is calculated using formula **σ = (∑ (xᵢ - <x>)²) / (n \* (n-1))**
- Then to calculate an indirect error the formula **∆f = √∑(∂f/∂yᵢ \* ∆yᵢ)²** is used, where yᵢ is a measured variable and ∆yᵢ is its error.

## Usage

1. If you have python>=3.9 installed, then you can download git repo, install dependencies(using pip or poetry) and run with 'python main.py'
2. Anotherway to run the program is using and executable from build folder.

## Dependencies

- [Python] >= 3.9
- [Sympy] >= 1.8

## Dev Dependencies

- [Black] >= 21.9
- [Pylint] >= 2.11.1
- [Pyinstaller] >= 4.5.1

## License

[MIT]

[//]: #
[mit]: https://github.com/sxccxs/IMEC/blob/main/LICENSE
[python]: https://www.python.org/
[sympy]: https://www.sympy.org
[black]: https://github.com/psf/black
[pylint]: https://pylint.org/
[pyinstaller]: https://www.pyinstaller.org/
