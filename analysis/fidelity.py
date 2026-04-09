from  qiskit.quantum_info import partial_trace, state_fidelity

def compute_fidelity(ideal_sv, noisy_sv):
    ideal_reduced =partial_trace(ideal_sv,[0,1])
    noisy_reduced = partial_trace(noisy_sv,[0,1])

    return state_fidelity(ideal_reduced,noisy_reduced)
