import numpy as np
import sympy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter

# Definizione delle variabili simboliche
t = sp.Symbol('t')
theta = sp.Function('theta')(t)
l = sp.Function('l')(t)
m, g, k, l0 = sp.symbols('m g k l0')
dtheta = theta.diff(t)
ddtheta = dtheta.diff(t)
dl = l.diff(t)
ddl = dl.diff(t)

# Passaggio a coordinate cartesiane
x = l * sp.sin(theta)
y = -l * sp.cos(theta)

# Definizione Lagrangiana
T = sp.Rational(1, 2) * m * (x.diff(t)**2 + y.diff(t)**2)
V = m * g * y + sp.Rational(1, 2) * k * (l - l0)**2
L = T - V

# Equazioni di Eulero-Lagrange
lagrange_eq_theta = sp.Eq(L.diff(dtheta).diff(t) - L.diff(theta), 0)
lagrange_eq_l = sp.Eq(L.diff(dl).diff(t) - L.diff(l), 0)

# Risoluzione delle equazioni di Eulero-Lagrange
sol = sp.solve([lagrange_eq_theta, lagrange_eq_l], (ddtheta, ddl))
ddtheta_sol = sol[ddtheta]
ddl_sol = sol[ddl]

# Funzioni lambda per l'integrazione numerica
ddtheta_func = sp.lambdify((theta, l, dtheta, dl, m, g, k, l0), ddtheta_sol)
ddl_func = sp.lambdify((theta, l, dtheta, dl, m, g, k, l0), ddl_sol)

# Parametri
g_val = 9.81  # accelerazione gravitazionale, m/s^2
k_val = 15.0  # costante elastica della molla, N/m
m_val = 1.0   # massa, kg
l0_val = 1.0  # lunghezza naturale della molla, m

# Condizioni iniziali
theta0 = np.pi / 4  # angolo iniziale, rad
omega0 = 0.0        # velocità angolare iniziale, rad/s
l_initial = 1.0     # lunghezza iniziale della molla, m
dl0 = 0.0           # velocità iniziale di cambiamento di lunghezza, m/s

# Funzione per il sistema di equazioni differenziali
def pendulum_spring(y, t, m, g, k, l0):
    theta, omega, l, dl = y
    dydt = [
        omega,
        ddtheta_func(theta, l, omega, dl, m, g, k, l0),
        dl,
        ddl_func(theta, l, omega, dl, m, g, k, l0)
    ]
    return dydt

# Condizioni iniziali per odeint
y0 = [theta0, omega0, l_initial, dl0]

# Intervallo di tempo per la simulazione
t_vals = np.linspace(0, 10, 1000)  # da 0 a 10 secondi

# Soluzione del sistema di equazioni differenziali
sol = odeint(pendulum_spring, y0, t_vals, args=(m_val, g_val, k_val, l0_val))

# Estrazione dei risultati
theta_vals = sol[:, 0]
l_vals = sol[:, 2]

# Animazione del pendolo
def animate_pendulum(t_vals, theta_vals, l_vals):
    fig, ax = plt.subplots()
    ax.set_xlim((-2, 2))
    ax.set_ylim((-4, 2))

    line, = ax.plot([], [], 'o-', lw=2)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        x = l_vals[frame] * np.sin(theta_vals[frame])
        y = -l_vals[frame] * np.cos(theta_vals[frame])
        line.set_data([0, x], [0, y])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=range(len(t_vals)),
                                  init_func=init, blit=True)

    plt.show()
    ani.save("D:/Dati Windows/Simulazione_pendolo_lagrangiana/moto_pendolo_molla.gif", writer=PillowWriter(fps=30))
    return ani

# Esecuzione dell'animazione
ani = animate_pendulum(t_vals, theta_vals, l_vals)
