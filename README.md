# Simulazione Pendolo 

Semplice simulazione di un pendolo classico tramite la libreria Sympy, Numpy e Scipy. Tramite matplotlib ho generato anche l'immagine presente.
Cercherò di implementare anche altre varianti del pendolo.

L'idea di base è quella di utilizzare il principio variazionale di minima azione, ovvero
$$\mathcal{S} = \int_{A}^B \mathcal{L}(q, \dot{q}, t)dt$$
dev'essere tale da assumere il valore minimo possibile fra due istanti di tempo. Questo si traduce, di fatto, nella necessità di minimizzare il funzionale $\mathcal{S}$, imponendo le condizione di Eulero-Lagrange:
$$\frac{\partial \mathcal{L}}{\partial q_i} - \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{q}_i} = 0$$
dove $q_i$ indica la $i$-esima coordinata generalizzata usata per descrivere la posizione del nostro corpo. Nel caso del pendolo, per esempio, invece di utilizzare le coordinate cartesiane (che di fatto sono ridondandi anche se le utilizzeremo per rappresentare l'animazione del pendolo), possiamo utilizzare le coordinate polari dove la posizione del corpo è indicata da $(l(t), \theta(t))$ ovvero dalla distanza $l(t)$ dall'origine $O$ e l'angolo che forma con l'asse $x$. Naturalmente $(x, y) \mapsto^{\phi} (q_1, q_2)$ con $\phi$ funzione biunivoca, ovvero il passaggio fra coordinate cartesiane e le coordinate generalizzate deve avvenire tramite una funzione $\phi: \mathbb{R}^2 \to \mathbb{R}^2$ che sia invertibile.
Nel caso del pendolo semplice queste equazioni, siccome $l$ fissato, si riduce a studiare il sistema ad un solo grado di libertà, dunque:
$$\frac{\partial \mathcal{L}}{\partial \theta} - \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{\theta}} = 0$$
nel caso invece di $l(t)$ (ovvero $l(t) \neq l_0 \, \forall t$) con il filo che si comporta come un oscillatore armonico ideale allora bisogna studiare il seguente sistema di equazioni differenziali:
```math
\begin{equation}\begin{cases} \frac{\partial \mathcal{L}}{\partial \theta} - \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{\theta}} = 0 \\ \frac{\partial \mathcal{L}}{\partial l} - \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{l}} = 0 \\ \end{cases}\end{equation}
```
