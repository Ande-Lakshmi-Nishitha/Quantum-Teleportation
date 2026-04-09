import numpy as np
from qiskit import Aer, transpile
from qiskit.quantum_info import Statevector
from circuits.teleportation import create_teleportation_circuit
from noise.noise_models import create_noise_model
from analysis.fidelity import compute_fidelity

def run():
    backend = Aer.get_backend('aer_simulator')
    noise_levels = [0,0.01,0.05,0.1,0.2]
    results=[]

    for p in noise_levels:
        noise_model=create_noise_model(p)
        fidelities=[]

        for _ in range(30):
            theta=np.random.uniform(0,np.pi)
            phi=np.random.uniform(0,2*np.pi)

            qc=create_teleportation_circuit(theta,phi)

            #ideal state with no noise
            ideal_sv =Statevector.from_instruction(qc)

            #simulation creation
            qc.save_statevector()
            tqc=transpile(qc,backend)

            #running with noise
            result = backend.run(tqc,noise_model=noise_model).result()
            noisy_sv =result.get_statevector()

            fidelity=compute_fidelity(ideal_sv,noisy_sv)
            fidelities.append(fidelity)

        avg_fidelity=np.mean(fidelities)
        results.append((p,avg_fidelity))

        print(f"Noise: {p}, Avg Fidelity: {avg_fidelity:.4f}")

    return results