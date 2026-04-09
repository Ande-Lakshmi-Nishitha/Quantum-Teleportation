from qiskit_aer.noise import NoiseModel, depolarizing_error

def create_noise_model(p=0.01):
    noise_model = NoiseModel()

    error_1q = depolarizing_error(p, 1)
    error_2q = depolarizing_error(p, 2)

    noise_model.add_all_qubit_quantum_error(error_1q, ['u', 'h', 'x'])
    noise_model.add_all_qubit_quantum_error(error_2q, ['cx'])

    return noise_model