import numpy as np
import json
from qiskit_aer import Aer

from circuits.teleportation import create_teleportation_circuit
from circuits.state_prep import prepare_state
from noise.noise_models import create_noise_model
from analysis.fidelity import compute_fidelity


def run():
    backend = Aer.get_backend("aer_simulator")

    noise_levels = [0, 0.01, 0.05, 0.1, 0.2]
    noise_types = ["depolarizing", "amplitude"]

    all_results = {}

    for noise_type in noise_types:
        print(f"\nRunning for noise type: {noise_type}")

        results = []

        for p in noise_levels:
            noise_model = create_noise_model(p, noise_type)
            fidelities = []

            for _ in range(30):
                qc = create_teleportation_circuit()
                prepare_state(qc, 0, "random")

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

            print(f"{noise_type} | Noise: {p}, Fidelity: {avg_fidelity:.4f}")

        all_results[noise_type] = results

    # Save results to JSON
    with open("results.json", "w") as f:
        json.dump(all_results, f, indent=4)

    print("Results saved to results.json")

    return all_results