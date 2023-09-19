import matplotlib.pyplot as plt
import numpy as np

def DefiningLines():
    # Create a range of Q(Alb) values (e.g., from 0 to Qalbumin)
    q_alb_values = np.linspace(0,130,1000)

    # Calculate corresponding Q(IgG) values using your equation
    q_igg_values = 0.77 * (np.sqrt(q_alb_values**2 + 23e-6)) - 3.1e-3 #Q lim

    m_igg_values = 0.65 * (np.sqrt(q_alb_values**2 + 8e-6)) - 1.4e-3 #Q med

    s_igg_values = 0.33 * (np.sqrt(q_alb_values**2 + 2e-6)) - 0.3e-3 #Q low
    
    return q_alb_values, q_igg_values, m_igg_values, s_igg_values

def DownwardLines(plt, q_igg_values, s_igg_values):
    vertical_lines_x = [5, 6.5, 8]
    ymax= [3.8, 5, 6.1]
    ymin = [1.7, 2.2, 2.7]

    for i in range(0,3):
        x = vertical_lines_x[i]
        y1= ymax[i]
        y2 = ymin[i]

        xlist = [x, x]
        ylist = [y1, y2]
        plt.plot(xlist,ylist, color = "black", linewidth = 2)

    return plt


# Input Qalbumin and Qigg values
def GetInput (): #--> out Qigg Q alb floats 
    Qigg = float(input("Enter Qigg value: "))
    Qalbumin = float(input("Enter Qalbumin value: "))
    return Qigg, Qalbumin

def Main_PlotSetup ():
    plt.figure(figsize=(6, 8)) 

    # Use logarithmic scale for both axes
    Qigg, Qalbumin = GetInput()
    plt.semilogx([Qalbumin, Qalbumin], [0, Qigg], color='b', linestyle='solid', label=f'Qalbumin = {Qalbumin}')
    plt.semilogy([0, Qalbumin], [Qigg, Qigg], color='g', linestyle='solid', label=f'Qigg = {Qigg}')

    # Define fixed axis limits
    x_min, x_max = 1, 130  # Adjusted for logarithmic scale
    y_min, y_max = 0.3, 130  # Adjusted for logarithmic scale

    # Define fixed tick locations including 50
    y_ticks = [0.5, 1, 2, 5, 10, 20, 50, 100]
    x_ticks = [2, 5, 10, 20, 50, 100]

    # Set axis limits
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    # Set custom ticks and labels
    plt.xticks(x_ticks, x_ticks)
    plt.yticks(y_ticks, y_ticks)

    # Display the intersection point
    plt.scatter(Qalbumin, Qigg, color='r', label='Intersection')
    #plt.semilogx([Qalbumin, Qalbumin], [0, Qigg], color='b', linestyle='solid', label=f'Qalbumin = {Qalbumin}')

    plt.title('Reibergram')
    plt.ylabel('QIgG')
    plt.xlabel('QAlb')
    plt.grid(True)

    plt.legend()
    return plt

def Main():

    plt = Main_PlotSetup()

    q_alb_values, q_igg_values, m_igg_values , s_igg_values = DefiningLines()
    plt = DownwardLines(plt, q_igg_values,s_igg_values)

    # Plot the Q(IgG) vs. Q(Alb) curve
    plt.plot(q_alb_values, q_igg_values, color='black', linewidth = 2)
    plt.plot(q_alb_values, m_igg_values, color='black', linewidth = 2)
    plt.plot(q_alb_values, s_igg_values, color='black', linewidth = 2)
     
    plt.show()
    return

Main()