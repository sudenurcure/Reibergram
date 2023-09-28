import matplotlib.pyplot as plt
import numpy as np

# Hansotto Reiber
# Reiber, H. (1994). Flow rate of cerebrospinal fluid (CSF) —
# A concept common to normal blood-CSF barrier function and to dysfunction in neurological diseases.
# Journal of the Neurological Sciences, 122(2), 189–203. doi:10.1016/0022-510x(94)90298-4
# Sude Nur Cüre

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


def define_lines():
    """
    Calculate QAlb, QIgG, and SIgG values.

    Returns:
        q_alb_values (numpy.ndarray): Array of QAlb values.
        q_igg_values (numpy.ndarray): Array of QIgG values.
        s_igg_values (numpy.ndarray): Array of SIgG values.
    """
    q_alb_values = np.linspace(QALB_MIN, QALB_MAX, 1000)
    q_igg_values = 0.93 * (np.sqrt(q_alb_values**2 + 6e-6)) - 1.7e-3
    s_igg_values = 0.33 * (np.sqrt(q_alb_values**2 + 2e-6)) - 0.3e-3

    twenty_igg_values = q_igg_values / 0.8
    fourty_igg_values = q_igg_values / 0.6
    sixty_igg_values = q_igg_values / 0.4
    eighty_igg_values = q_igg_values / 0.2

    plt.plot(q_alb_values, q_igg_values, color="black", linewidth=2)
    plt.plot(q_alb_values, s_igg_values, color="black", linewidth=1)

    plt.plot(
        q_alb_values, twenty_igg_values, color="black", linewidth=1, linestyle="--"
    )
    plt.plot(
        q_alb_values, fourty_igg_values, color="black", linewidth=1, linestyle="--"
    )
    plt.plot(q_alb_values, sixty_igg_values, color="black", linewidth=1, linestyle="--")

    plt.plot(
        q_alb_values, eighty_igg_values, color="black", linewidth=1, linestyle="--"
    )

    # Label for twenty_igg_values line
    plt.text(
        87e-3,
        100e-3,
        "20",
        ha="right",
        va="bottom",
        color="black",
    )

    # Label for fourty_igg_values line
    plt.text(
        66e-3,
        100e-3,
        "40",
        ha="right",
        va="bottom",
        color="black",
    )

    # Label for sixty_igg_values line
    plt.text(
        44e-3,
        100e-3,
        "60",
        ha="right",
        va="bottom",
        color="black",
    )

    # Label for eighty_igg_values line
    plt.text(
        23e-3,
        100e-3,
        "80%",
        ha="right",
        va="bottom",
        color="black",
    )

    plt.fill_between(
        q_alb_values,
        q_igg_values,
        s_igg_values,
        where=(q_alb_values >= 8e-3),
        facecolor="none",
        edgecolor="black",
        alpha=1,
        hatch="\|",
    )
    return 0


def draw_vertical_lines():
    """
    Draw vertical lines on the plot.

    Vertical lines are defined by the constants VERTICAL_LINES_X, YMIN, and YMAX.
    """
    vertical_lines_x = [5e-3, 6.5e-3, 8e-3]
    ymin = [2.3e-3, 3.2e-3, 2.4e-3]
    ymax = [3.4e-3, 4.7e-3, 6e-3]

    for x, y1, y2 in zip(vertical_lines_x, ymin, ymax):
        plt.plot([x, x], [y1, y2], color="black", linewidth=2, linestyle="-")


def get_input():
    """
    Get user input for QIgG and QAlb values.

    Returns:
        Qigg (float): QIgG value.
        Qalbumin (float): QAlb value.
    """
    while True:
        user_input = input("QIgG değeri giriniz. (ya da çıkmak için 'bitir'): ")
        if user_input.lower() == "bitir":
            raise SystemExit(0)
        try:
            Qigg = float(user_input) * CONVERSION_FACTOR
            break  # Exit the loop if QIgG is valid
        except ValueError:
            print("Lütfen geçerli bir QIgG değeri giriniz.")

    while True:
        user_input = input("QAlb değeri giriniz. (ya da çıkmak için 'bitir'): ")
        if user_input.lower() == "bitir":
            raise SystemExit(0)
        try:
            Qalbumin = float(user_input) * CONVERSION_FACTOR
            break  # Exit the loop if QAlb is valid
        except ValueError:
            print("Lütfen geçerli bir QAlb değeri giriniz.")

    return Qigg, Qalbumin


def main_plot_setup(Qigg, Qalbumin):
    """
    Set up the main plot with labels, ticks, and legends.

    Args:
        Qigg (float): QIgG value.
        Qalbumin (float): QAlb value.
    """
    plt.figure(figsize=(6, 7))

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
            print("\nUygulama kapatılıyor.")
            break
