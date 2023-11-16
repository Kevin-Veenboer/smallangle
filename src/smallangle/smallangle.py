# smallangle/smallanlge.py

"""
This module allows the user to calculate values of tangent and sine between 0 and 2 pi and test sine and tangent approximations

This module contains the following functions:

-`sin(number)` - gives the value of sine for a number of steps between 0 and 2 pi\n
-`tan(number)` - gives the value of tangent for a number of steps between 0 and 2 pi\n
-`approx(error, type_flag)` - tests the maximum value for some sine/tangent approximations\n
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
@click.option(
    "-t",
    "--tangent/--no-tangent",
    help="selects tangent small-angle approximation instead of sine",
)
@click.option(
    "-c",
    "--compare/--no-compare",
    help="selects sine-tangent equality instead of sine small-angle approximation",
)
def approx(error, tangent, compare):
    """Function that gives the maximum value at which the small-angle/equality approximation holds

    Args:
        error (float): the required accuracy for which the approximation has to hold
        tangent (bool): flag for selecting the tangent small-angle approximation
        compare (bool): flag for selecting the sine-tangent equality approximation
    """

    # Only one approximation can be selected at a time, if both -t and -c are given to approx, then only tangent will run
    # Code for the tangent small angle approximation
    if tangent:
        for number in np.arange(0, 2 * pi, 0.001):
            # check the difference, if it is greater than the required accuracy we give the maximum value
            if abs(number - np.tan(number)) > float(error):
                print(
                    f"For an accuracy of {error}, the small-angle approximation holds\nup to x = {round(number,3)}"
                )
                return

        print(
            f"The given accuracy of {error} is so large that the tangent small-angle approximation holds\nfor all values between 0 and 2 pi"
        )

    # Code for the sine-tangent equality approximation
    elif compare:
        for number in np.arange(0, 2 * pi, 0.001):
            # check the difference, if it is greater than the required accuracy we give the maximum value
            if abs(np.sin(number) - np.tan(number)) > float(error):
                print(
                    f"For an accuracy of {error}, the sine-tangent equality approximation holds\nup to x = {round(number,3)}"
                )
                return

        print(
            f"The given accuracy of {error} is so large that the equality approximation holds\nfor all values between 0 and 2 pi"
        )

    # Code for the sine small angle approximation
    else:
        for number in np.arange(0, 2 * pi, 0.001):
            # check the difference, if it is greater than the required accuracy we give the maximum value
            if abs(number - np.sin(number)) > float(error):
                print(
                    f"For an accuracy of {error}, the small-angle approximation holds\nup to x = {round(number,3)}"
                )
                return
        print(
            f"The given accuracy of {error} is so large that the sine small-angle approximation holds\nfor all values between 0 and 2 pi"
        )


if __name__ == "__main__":
    cmd_group()
