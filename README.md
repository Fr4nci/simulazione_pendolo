# Pendulumn simulations 

Simple simulation of a classic pendulumn using Sympy, Numpy e Scipy. Thanks to matplotlib I was able to generate the .gif you can see.
I'll try to implement other variants of the pendulumn.

The basic idea is to use the variation principle of least action, that is the following

$$\mathcal{S} = \int_{A}^B \mathcal{L}(q, \dot{q}, t)dt$$

and this quantity need to be the least possible considering a motion from an instant $t_A$ and $t_B$. This condition imply, as a matter of speaking, in finding a way to minimize the functional $\mathcal{S}$, by using the equation of Euler-Lagrange:

$$\frac{\partial \mathcal{L}}{\partial q_i} - \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{q}_i} = 0$$

where $q_i$ indicate the $i$-th generalised coordinate used to described the position of a body. In our case, for example, instead of using the cartesian coordinates (that are redondant even if I'll use them to represent the animation of the pendulum), we can use the polar coordinates where the position of a body  $(l(t), \theta(t))$ where $l(t)$ is the distance from the origin $O$ e $\theta(t)$ the angle that the body create with the $x$ axis. Naturally $(x, y) \xmapsto{\phi} (q_1, q_2)$ with $\phi$ a bijective function.
In the case of the classic pendulumn, where $l$ is fixed, our dinamycal system reduces to only a 1 degree of freedom system, so:

$$\frac{\partial \mathcal{L}}{\partial \theta} - \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{\theta}} = 0$$

in the case of $l(t)$ (that is $l(t) \neq l_0 \, \forall t$) with the wire acting as an ideal armonic oscillator, we have to study the following system of differential equations:
```math
\begin{equation}\begin{cases} \frac{\partial \mathcal{L}}{\partial \theta} - \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{\theta}} = 0 \\ \frac{\partial \mathcal{L}}{\partial l} - \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{l}} = 0 \\ \end{cases}\end{equation}
```
