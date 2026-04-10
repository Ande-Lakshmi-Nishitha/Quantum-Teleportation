from qiskit_aer.noise import NoiseModel, depolarizing_error


def create_noise_model(p):
    noise_model = NoiseModel()

    error_1 = depolarizing_error(p, 1)
    error_2 = depolarizing_error(p, 2)

    # Apply to actual gates used
    noise_model.add_all_qubit_quantum_error(error_1, ['h', 'ry', 'rz'])
    noise_model.add_all_qubit_quantum_error(error_2, ['cx'])

    return noise_model