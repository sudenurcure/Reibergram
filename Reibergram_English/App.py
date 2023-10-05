import matplotlib.pyplot as plt
import numpy as np

# Hansotto Reiber
# Reiber, H. (1994). Flow rate of cerebrospinal fluid (CSF) —
# A concept common to normal blood-CSF barrier function and to dysfunction in neurological diseases.
# Journal of the Neurological Sciences, 122(2), 189–203. doi:10.1016/0022-510x(94)90298-4
# Sude Nur Cüre, English Version


# Limiting Functions
def high(x):
    q_igg_value = 0.93 * (np.sqrt(x**2 + 6e-6)) - 1.7e-3
    return q_igg_value


def low(x):
    s_igg_value = 0.33 * (np.sqrt(x**2 + 2e-6)) - 0.3e-3
    return s_igg_value


# Constants
CONVERSION_FACTOR = 1e-3
QALB_MIN = 0
QALB_MAX = 130e-3
X_MIN = 1.5e-3
X_MAX = 130e-3
Y_MIN = 0.3e-3
Y_MAX = 130e-3
Y_TICKS = [0.5e-3, 1e-3, 2e-3, 5e-3, 10e-3, 20e-3, 50e-3, 100e-3]
X_TICKS = [2e-3, 5e-3, 10e-3, 20e-3, 50e-3, 100e-3]
Y_TICKS_L = [".5", 1, 2, 5, 10, 20, 50, "$\mathregular{100_{x10^{-3}}}$"]
X_TICKS_L = [2, 5, 10, "$\mathregular{20_{x10^{-3}}}$", 50, 100]
q_alb_values = np.linspace(QALB_MIN, QALB_MAX, 1000)
q_igg_values = 0.93 * (np.sqrt(q_alb_values**2 + 6e-6)) - 1.7e-3
s_igg_values = 0.33 * (np.sqrt(q_alb_values**2 + 2e-6)) - 0.3e-3

twenty_igg_values = q_igg_values / 0.8
fourty_igg_values = q_igg_values / 0.6
sixty_igg_values = q_igg_values / 0.4
eighty_igg_values = q_igg_values / 0.2

vertical_lines_x = [5e-3, 6.5e-3, 8e-3]
vertical_ymax = [
    high(vertical_lines_x[0]),
    high(vertical_lines_x[1]),
    high(vertical_lines_x[2]),
]
vertical_ymin = [2.3e-3, 3.2e-3, 2.4e-3]
top_limit = [twenty_igg_values, fourty_igg_values, sixty_igg_values, eighty_igg_values]
upper_liners = ["20", "40", "60", "80%"]

# Functions


def text_at_position(upper, label):
    plt.text(
        np.interp(100e-3, upper, q_alb_values),
        100e-3,
        label,
        ha="right",
        va="bottom",
        color="black",
    )


def define_lines():
    """
    Calculate QAlb, QIgG, and SIgG values.

    Returns:
        q_alb_values (numpy.ndarray): Array of QAlb values.
        q_igg_values (numpy.ndarray): Array of QIgG values.
        s_igg_values (numpy.ndarray): Array of SIgG values.
    """

    plt.plot(q_alb_values, q_igg_values, color="black", linewidth=2)
    plt.plot(q_alb_values, s_igg_values, color="black", linewidth=1)

    for values in top_limit:
        plt.plot(q_alb_values, values, color="black", linewidth=1, linestyle="--")

    for p, n in zip(top_limit, upper_liners):
        text_at_position(p, n)

    # X grid
    gridline_x_positions = [x for x in plt.xticks()[0] if x >= 8e-3] + [
        x for x in plt.xticks(minor=True)[0] if x >= 8e-3
    ]
    ymin = [low(x) for x in gridline_x_positions]
    ymax = [high(x) for x in gridline_x_positions]

    for x, y1, y2 in zip(gridline_x_positions, ymin, ymax):
        plt.plot([x, x], [y1, y2], color="black", linewidth=0.5, linestyle="-")

    # Y grid
    gridline_y_positions = [
        y for y in plt.yticks()[0] if y >= low(8e-3) and y < high(130e-3)
    ] + [y for y in plt.yticks(minor=True)[0] if y >= low(8e-3) and y < high(130e-3)]

    for y in gridline_y_positions:
        xinterp_max = np.interp(y, s_igg_values, q_alb_values)
        xinterp_min = np.interp(y, q_igg_values, q_alb_values)
        if xinterp_min < 8e-3:
            xinterp_min = 8e-3
        plt.hlines(
            y,
            xmin=xinterp_min,
            xmax=xinterp_max,
            color="black",
            linewidth=0.5,
            linestyle="-",
        )


def draw_vertical_lines():
    """
    Draw vertical lines on the plot.

    Vertical lines are defined by the constants VERTICAL_LINES_X, YMIN, and YMAX.
    """

    for x, y1, y2 in zip(vertical_lines_x, vertical_ymin, vertical_ymax):
        plt.plot([x, x], [y1, y2], color="black", linewidth=2, linestyle="-")


def get_input():
    """
    Get user input for QIgG and QAlb values.

    Returns:
        Qigg (float): QIgG value.
        Qalbumin (float): QAlb value.
    """
    while True:
        user_input = input("Enter a QIgG value or 'exit': ")
        if user_input.lower() == "exit":
            raise SystemExit(0)
        try:
            Qigg = float(user_input) * CONVERSION_FACTOR
            break  # Exit the loop if QIgG is valid
        except ValueError:
            print("Please enter a valid QIgG value.")

    while True:
        user_input = input("Enter a QAlb value or 'exit': ")
        if user_input.lower() == "exit":
            raise SystemExit(0)
        try:
            Qalbumin = float(user_input) * CONVERSION_FACTOR
            break  # Exit the loop if QAlb is valid
        except ValueError:
            print("Please enter a valid QAlb value.")

    return Qigg, Qalbumin


def main_plot_setup(Qigg, Qalbumin):
    """
    Set up the main plot with labels, ticks, and legends.

    Args:
        Qigg (float): QIgG value.
        Qalbumin (float): QAlb value.
    """
    plt.figure(figsize=(6, 6))

    plt.semilogx(
        [Qalbumin, Qalbumin],
        [0, Qigg],
        color="b",
        linestyle="solid",
    )
    plt.semilogy(
        [0, Qalbumin],
        [Qigg, Qigg],
        color="g",
        linestyle="solid",
    )

    plt.xlim(X_MIN, X_MAX)
    plt.ylim(Y_MIN, Y_MAX)

    plt.xticks(X_TICKS, X_TICKS_L)
    plt.yticks(Y_TICKS, Y_TICKS_L)

    plt.minorticks_on()
    plt.xticks(np.append(plt.xticks()[0], [15e-3, 1.5e-3]))
    plt.yticks(np.append(plt.yticks()[0], [15e-3, 1.5e-3]))

    plt.tick_params(
        axis="x",
        which="both",
        length=8,
        width=1.5,
        direction="in",
        pad=-8,
    )
    plt.tick_params(axis="y", which="both", length=8, width=1.5, direction="in", pad=-9)

    for tick in plt.gca().yaxis.get_majorticklabels():
        tick.set_horizontalalignment("left")
    for tick in plt.gca().xaxis.get_majorticklabels():
        tick.set_verticalalignment("bottom")

    plt.text(
        3e-3,
        60e-3,
        "QIgG",
        ha="center",
        va="center",
        fontsize=15,
        color="black",
        alpha=1,
        weight="bold",
    )
    plt.text(
        60e-3,
        0.65e-3,
        "QAlb",
        ha="center",
        va="center",
        fontsize=15,
        color="black",
        alpha=1,
        weight="bold",
    )

    plt.scatter(Qalbumin, Qigg, color="r")
    plt.grid(False)


def plot_reibergram(Qigg, Qalbumin, barcode="App"):
    """
    Plot the Reibergram including vertical lines and shaded region.

    Args:
        Qigg (float): QIgG value.
        Qalbumin (float): QAlb value.
    """
    main_plot_setup(Qigg, Qalbumin)
    define_lines()
    draw_vertical_lines()

    plt.savefig(f"{barcode}.png", bbox_inches="tight")


if __name__ == "__main__":
    while True:
        try:
            Qigg, Qalbumin = get_input()
            plot_reibergram(Qigg, Qalbumin)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
