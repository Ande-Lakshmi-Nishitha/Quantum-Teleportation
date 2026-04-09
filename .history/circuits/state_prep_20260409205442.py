from qiskit import QuantumCircuit
import numpy as np

def prepare_state(qc, qubit, state="random"):
    if state == "zero":
        pass  # default |0>

    elif state == "one":
        qc.x(qubit)

    elif state == "plus":
        qc.h(qubit)

    elif state == "random":
        theta = np.random.uniform(0, np.pi)
        phi = np.random.uniform(0, 2*np.pi)
        qc.u(theta, phi, 0, qubit)

    return qc