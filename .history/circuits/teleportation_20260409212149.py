from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

def create_teleportation_circuit():
    q = QuantumRegister(3)      #3 qubits
    c = ClassicalRegister(2)    #to account for 4 possible measurement for q0 and q1
    qc = QuantumCircuit(q, c)

    qc.h(q[1])
    qc.cx(q[1], q[2])   #Bell state between q1 and q2, maximally entangled

    return qc