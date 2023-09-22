import matplotlib.pyplot as plt
import numpy as np

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
Y_TICKS_L = [0.5, 1, 2, 5, 10, 20, 50, 100]
X_TICKS_L = [2, 5, 10, 20, 50, 100]


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

    plt.plot(q_alb_values, q_igg_values, color="black", linewidth=2)
    plt.plot(q_alb_values, s_igg_values, color="black", linewidth=1)

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
        user_input = input("Enter QIgG value (or 'stop' to exit): ")
        if user_input.lower() == "stop":
            raise SystemExit(0)
        try:
            Qigg = float(user_input) * CONVERSION_FACTOR
            break  # Exit the loop if QIgG is valid
        except ValueError:
            print("Please enter a valid numerical value for QIgG.")

    while True:
        user_input = input("Enter QAlb value: ")
        if user_input.lower() == "stop":
            raise SystemExit(0)
        try:
            Qalbumin = float(user_input) * CONVERSION_FACTOR
            break  # Exit the loop if QAlb is valid
        except ValueError:
            print("Please enter a valid numerical value for QAlb.")

    return Qigg, Qalbumin


def main_plot_setup(Qigg, Qalbumin):
    """
    Set up the main plot with labels, ticks, and legends.

    Args:
        Qigg (float): QIgG value.
        Qalbumin (float): QAlb value.
    """
    plt.figure(figsize=(6, 8))

    plt.semilogx(
        [Qalbumin, Qalbumin],
        [0, Qigg],
        color="b",
        linestyle="solid",
        label=f"QAlb = {int(Qalbumin*1000)}" + " x $\mathregular{10^{-3}}$",
    )
    plt.semilogy(
        [0, Qalbumin],
        [Qigg, Qigg],
        color="g",
        linestyle="solid",
        label=f"QIgG = {int(Qigg*1000)}" + " x $\mathregular{10^{-3}}$",
    )

    plt.xlim(X_MIN, X_MAX)
    plt.ylim(Y_MIN, Y_MAX)

    plt.xticks(X_TICKS, X_TICKS_L)
    plt.yticks(Y_TICKS, Y_TICKS_L)

    plt.scatter(Qalbumin, Qigg, color="r")
    plt.title("Reibergram")
    plt.ylabel("QIgG $(\mathregular{x10^{-3}}$) (mg/dL)")
    plt.xlabel("QAlb $(\mathregular{x10^{-3}}$)(mg/dL)")
    plt.grid(False)
    plt.legend()


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

    plt.legend()
    plt.savefig(f"{barcode}.png")


if __name__ == "__main__":
    while True:
        try:
            Qigg, Qalbumin = get_input()
            plot_reibergram(Qigg, Qalbumin)
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break
