import numpy as np
from qiskit_aer import Aer

from circuits.teleportation import create_teleportation_circuit
from noise.noise_models import create_noise_model
from analysis.fidelity import compute_fidelity


def run():
    backend = Aer.get_backend("aer_simulator")

    noise_levels = [0, 0.01, 0.05, 0.1, 0.2]
    results = []

    for p in noise_levels:
        noise_model = create_noise_model(p)
        fidelities = []

        for _ in range(30):
            qc = create_teleportation_circuit()
            prepare_state(qc, 0, random)

            # -------- IDEAL --------
            ideal_qc = qc.copy()
            ideal_qc.save_statevector()
            ideal_result = backend.run(ideal_qc).result()
            ideal_sv = ideal_result.get_statevector()

            # -------- NOISY --------
            noisy_qc = qc.copy()
            noisy_qc.save_statevector()
            noisy_result = backend.run(noisy_qc, noise_model=noise_model).result()
            noisy_sv = noisy_result.get_statevector()

            fidelity = compute_fidelity(ideal_sv, noisy_sv)
            fidelities.append(fidelity)

        avg_fidelity = np.mean(fidelities)
        results.append((p, avg_fidelity))

        print(f"Noise: {p}, Avg Fidelity: {avg_fidelity:.4f}")

    return results