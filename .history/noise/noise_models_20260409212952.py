from qiskit_aer.noise import NoiseModel, depolarizing_error

def create_noise_model(p=0.01):     #error probability is defined
    noise_model = NoiseModel()      #empty noise model

    error_1q = depolarizing_error(p, 1)     #single qubit error
    error_2q = depolarizing_error(p, 2)     #double qubit error

    noise_model.add_all_qubit_quantum_error(error_1q, ['u', 'h', 'x'])  #applies error after using specified gates
    noise_model.add_all_qubit_quantum_error(error_2q, ['cx'])
    
    return noise_model