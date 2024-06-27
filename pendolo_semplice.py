import numpy as np
import sympy as sp
from sympy.utilities import lambdify
from sympy.solvers import solve
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation
from matplotlib.animation import PillowWriter
from IPython.display import HTML

import matplotlib
matplotlib.use('TkAgg')

# Definisco la classe pendolo dove gli passo tutta le variabili che devono caratterizzare l'istanza pendolo
class Pendolo:
    def __init__(self, t, theta0, v0):
        self.l = 1  # Lunghezza fissa del pendolo
        self.t = t # Inizializzo la variabile del tempo
        self.conds = [theta0, v0] # Definisco le condizioni iniziali

    def solve(self):
        m, g, t = sp.symbols(('m', 'g', 't')) # definisco i simboli che utilizzerò nei calcoli
        l = self.l 
        theta = sp.Function("theta")(t) # definisco la funzione theta
        dtheta = theta.diff(t) # definisco la derivata di theta rispetto al tempo
        ddtheta = dtheta.diff(t) # definisco la derivata seconda di theta rispetto al tempo

        x = l * sp.sin(theta) # passaggio alle coordinate cartesiane per animare il pendolo
        y = -l * sp.cos(theta)

        T = sp.Rational(1, 2) * m * (x.diff(t)**2 + y.diff(t)**2) # energia cinetica
        V = m * g * y # energia potenziale
        L = T - V # lagrangiana

        # equazione di lagrange di minimizzazione della lagrangiana
        dL_dtheta = L.diff(theta)
        dL_ddtheta_dt = L.diff(dtheta).diff(t)
        eq = sp.Eq(dL_ddtheta_dt - dL_dtheta, 0)

        # Risoluzione dell'equazione differenziale
        sol = solve(eq, ddtheta)
        if len(sol) == 0:
            raise ValueError("Nessuna soluzione trovata")
        ddtheta_sol = sol[0]

        dthetadt_num = sp.lambdify(dtheta, dtheta)
        dudt_num = sp.lambdify((g, theta), ddtheta_sol)
        
        x_num = sp.lambdify(theta, x)
        y_num = sp.lambdify(theta, y)
        
        del m, g, t
        
        g = 9.81
        l = self.l
        t = self.t
        conds = self.conds
        
        def dXdt(X, t, g, l):    
            theta_num, u_num = X
            return [dthetadt_num(u_num), dudt_num(g, theta_num)]
        
        sol = odeint(dXdt, t=t, y0=conds, args=(g, l))
        angle = sol.T[0]
        velocity = sol.T[1]
        
        return x_num(angle), y_num(angle)

# Parametri
t = np.linspace(0, 10, 500)
pend = Pendolo(t, np.pi/4, 0)
x, y = pend.solve()

# Animazione
fig, ax = plt.subplots()
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.5, 1.1)
line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data([0, x[frame]], [0, y[frame]])
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)

# Salvataggio animazione in una GIF
ani.save("D:/Dati Windows/Simulazione_pendolo_lagrangiana/moto_pendolo.gif", writer=PillowWriter(fps=30))

# Riga utile se si vuole mostrare sul Jupyter Notebook
HTML(ani.to_jshtml())