# smallangle/smallanlge.py

"""
This module allows the user to calculate values of tangent and sine between 0 and 2 pi and test sine and tangent approximations

This module contains the following functions:

-`sin(number)` - gives the value of sine for a number of steps between 0 and 2 pi
-`tan(number)` - gives the value of tangent for a number of steps between 0 and 2 pi
-`approx(error, type_flag)` - tests the maximum value for some sine/tangent approximations
"""

import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of steps between 0 and 2 pi to calculate sine",
    show_default=True,
)
def sin(number):
    """Function that shows values of sine between 0 and 2 pi

    Args:
        number (int): number of steps between 0 and 2 pi to calculate values of sine
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of steps between 0 and 2 pi to calculate tangent",
    show_default=True,
)
def tan(number):
    """Function that shows values of tangent between 0 and 2 pi

    Args:
        number (int): number of steps between 0 and 2 pi to calculate values of tangent
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


@cmd_group.command()
@click.argument("error")
def approx(error):
    """Function that gives the maximum value at which the small-angle approximation holds

    Args:
        error (float): the required accuracy for which the approximation has to hold
    """
    for number in np.arange(0, 2 * pi, 0.001):
        # check the difference, if it is greater than the required accuracy we give the maximum value
        if abs(number - np.sin(number)) > float(error):
            print(
                f"For an accuracy of {error}, the small-angle approximation holds\nup to x = {number}"
            )
            return
    print(
        f"The given accuracy of {error} is so large that the small-angle approximation holds\nfor all values between 0 and 2 pi"
    )


if __name__ == "__main__":
    cmd_group()
