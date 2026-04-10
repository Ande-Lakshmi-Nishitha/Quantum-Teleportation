from qiskit_aer.noise import amplitude_damping_error

from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error


def create_noise_model(p, noise_type="depolarizing"):
    noise_model = NoiseModel()

    if noise_type == "depolarizing":
        error_1 = depolarizing_error(p, 1)
        error_2 = depolarizing_error(p, 2)

    elif noise_type == "amplitude":
        error_1 = amplitude_damping_error(p)
        error_2 = amplitude_damping_error(p).tensor(amplitude_damping_error(p))

    else:
        raise ValueError("Unknown noise type")

    # Applying noise to gates used in circuit
    noise_model.add_all_qubit_quantum_error(error_1, ['h', 'ry', 'rz'])
    noise_model.add_all_qubit_quantum_error(error_2, ['cx'])

    return noise_model