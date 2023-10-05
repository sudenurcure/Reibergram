import matplotlib.pyplot as plt
import numpy as np

"""
Changing elements:
* high and low

* Plot drawing is inactivated for given coordinates.
"""


def high(x):
    # q_IgM_value = 0.67 * (np.sqrt(x**2 + 120e-6)) - 7.1e-3 #IgM
    q_IgA_value = 0.77 * (np.sqrt(x**2 + 23e-6)) - 3.1e-3
    return q_IgA_value


def low(x):  # takes list returns list
    # s_IgM_value = 0.04 * (np.sqrt(x**2 + 442e-6)) - 0.82e-3 #IgM
    s_IgA_value = 0.17 * (np.sqrt(x**2 + 74e-6)) - 1.3e-3
    return s_IgA_value


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
q_IgA_values = high(q_alb_values)
s_IgA_values = low(q_alb_values)

twenty_IgA_values = q_IgA_values / 0.8
fourty_IgA_values = q_IgA_values / 0.6
sixty_IgA_values = q_IgA_values / 0.4
eighty_IgA_values = q_IgA_values / 0.2

vertical_lines_x = [5e-3, 6.5e-3, 8e-3]
vertical_ymax = [
    high(vertical_lines_x[0]),
    high(vertical_lines_x[1]),
    high(vertical_lines_x[2]),
]
vertical_ymin = [
    2.3 * vertical_ymax[0] / 4.2,
    2.3 * vertical_ymax[1] / 4.3,
    low(vertical_lines_x[2]),
]

top_limit = [twenty_IgA_values, fourty_IgA_values, sixty_IgA_values, eighty_IgA_values]
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
    Calculate QAlb, QIgA, and SIgA values.

    Returns:
        q_alb_values (numpy.ndarray): Array of QAlb values.
        q_IgA_values (numpy.ndarray): Array of QIgA values.
        s_IgA_values (numpy.ndarray): Array of SIgA values.
    """

    plt.plot(q_alb_values, q_IgA_values, color="black", linewidth=2)
    plt.plot(q_alb_values, s_IgA_values, color="black", linewidth=1)

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
        xinterp_max = np.interp(y, s_IgA_values, q_alb_values)
        xinterp_min = np.interp(y, q_IgA_values, q_alb_values)
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
    return 0


def draw_vertical_lines():
    """
    Draw vertical lines on the plot.

    Vertical lines are defined by the constants VERTICAL_LINES_X, YMIN, and YMAX.
    """

    for x, y1, y2 in zip(vertical_lines_x, vertical_ymin, vertical_ymax):
        plt.plot([x, x], [y1, y2], color="black", linewidth=2, linestyle="-")


def get_input():
    """
    Get user input for QIgA and QAlb values.

    Returns:
        QIgA (float): QIgA value.
        Qalbumin (float): QAlb value.
    """
    while True:
        user_input = input("QIgA değeri giriniz. (ya da çıkmak için 'bitir'): ")
        if user_input.lower() == "bitir":
            raise SystemExit(0)
        try:
            QIgA = float(user_input) * CONVERSION_FACTOR
            break  # Exit the loop if QIgA is valid
        except ValueError:
            print("Lütfen geçerli bir QIgA değeri giriniz.")

    while True:
        user_input = input("QAlb değeri giriniz. (ya da çıkmak için 'bitir'): ")
        if user_input.lower() == "bitir":
            raise SystemExit(0)
        try:
            Qalbumin = float(user_input) * CONVERSION_FACTOR
            break  # Exit the loop if QAlb is valid
        except ValueError:
            print("Lütfen geçerli bir QAlb değeri giriniz.")

    return QIgA, Qalbumin


def main_plot_setup(QIgA, Qalbumin):
    """
    Set up the main plot with labels, ticks, and legends.

    Args:
        QIgA (float): QIgA value.
        Qalbumin (float): QAlb value.
    """
    plt.figure(figsize=(6, 6))

    plt.semilogx([Qalbumin, Qalbumin], [0, QIgA], color="b", linestyle="solid", alpha=0)
    plt.semilogy([0, Qalbumin], [QIgA, QIgA], color="g", linestyle="solid", alpha=0)

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

    # Sude Nur Cüre
    plt.text(
        3e-3,
        60e-3,
        "QIgA",
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

    plt.grid(False)


def plot_reibergram(QIgA, Qalbumin, barcode="App"):
    """
    Plot the Reibergram including vertical lines and shaded region.

    Args:
        QIgA (float): QIgA value.
        Qalbumin (float): QAlb value.
    """
    main_plot_setup(QIgA, Qalbumin)
    define_lines()
    draw_vertical_lines()

    plt.savefig(f"{barcode}.png", bbox_inches="tight")


if __name__ == "__main__":
    while True:
        try:
            QIgA, Qalbumin = get_input()
            plot_reibergram(QIgA, Qalbumin)
        except KeyboardInterrupt:
            print("\nUygulama kapatılıyor.")
            break
