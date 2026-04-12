from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

def create_teleportation_circuit(theta, phi):
    qc = QuantumCircuit(3)

    qc.ry(theta, 0)
    qc.rz(phi, 0)

    qc.h(1)
    qc.cx(1, 2)

    qc.cx(0, 1)
    qc.h(0)

    qc.cx(1, 2)
    qc.cz(0, 2)

    return qc