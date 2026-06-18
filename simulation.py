import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameter
V1max = 5.0
Km1 = 2.0
Ki = 3.0
X = 10.0

k2 = 1.0
k3 = 0.8
k4 = 0.3

def model(t, y):
    A, B, P = y

    v1 = (V1max * X)/((Km1 + X)*(1 + P/Ki))
    v2 = k2*A
    v3 = k3*B
    v4 = k4*A

    dA = v1 - v2 - v4
    dB = v2 - v3
    dP = v3

    return [dA,dB,dP]

y0 = [0,0,0]

t_span = (0,50)

t_eval = np.linspace(0,50,500)

sol = solve_ivp(
    model,
    t_span,
    y0,
    t_eval=t_eval
)

plt.plot(sol.t,sol.y[0],label='A')
plt.plot(sol.t,sol.y[1],label='B')
plt.plot(sol.t,sol.y[2],label='P')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Metabolic Pathway Simulation')
plt.legend()

plt.savefig('simulation_result.png')
plt.show()
