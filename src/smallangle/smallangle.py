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
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


@cmd_group.command()
@click.argument("error")
def approx(error):
    for number in np.arange(0, 2 * pi, 0.001):
        delta = abs(number - np.sin(number))
        if delta > float(error):
            print(
                f"For an accuracy of {error}, the small-angle approximation holds\nup to x = {number}"
            )
            return
    print(
        f"The given accuracy of {error} is so large that the small-angle approximation holds\nfor all values between 0 and 2 pi"
    )


if __name__ == "__main__":
    cmd_group()
