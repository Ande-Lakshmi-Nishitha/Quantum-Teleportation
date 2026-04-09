from qiskit import QuantumCircuit
import numpy as np

def prepare_state(qc, qubit, state="random"):
    if state == "zero":
        pass        #passes default |0⟩  
    elif state == "one":
        qc.x(qubit) #inverts |0⟩ to |1⟩
    elif state == "plus":
        qc.h(qubit) #applies hadamard on |0⟩ to convert to |+⟩
    elif state == "random":
        theta = np.random.uniform(0, np.pi)
        phi = np.random.uniform(0, 2*np.pi)
        qc.u(theta, phi, 0, qubit)      #created a qubit with a random configuration
    
    return qc

    