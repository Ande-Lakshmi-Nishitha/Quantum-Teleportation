# Quantum Teleportation with Noise Simulation

## Overview
This project simulates **quantum teleportation** using Qiskit and analyzes how different noise models affect the reliability of quantum communication.

Quantum teleportation transfers the *state* of a qubit using entanglement and classical communication. In real systems, noise degrades this process — which we study here.

---

## Features
- Implementation of a **quantum teleportation circuit**
- Simulation under realistic noise models:
  - Depolarizing noise
  - Amplitude damping
- Random quantum state generation using θ and φ
- Fidelity calculation using **partial trace**
- Visualization of fidelity vs noise
- Results stored in structured JSON format

---

## Methodology

1. Generate a random quantum state:
- |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩

2. Perform quantum teleportation

3. Simulate:
- Ideal (no noise)
- Noisy system

4. Extract the teleported qubit using partial trace

5. Compute fidelity between ideal and noisy states

---

## Results

- Fidelity decreases as noise increases
- Different noise models impact teleportation differently:
- **Depolarizing noise** → gradual degradation
- **Amplitude damping** → stronger degradation due to energy loss

---

## Output

- `results_plot.png` → Fidelity vs Noise graph
- `results.json` → Experimental data

---

## Key Insight

Quantum communication is highly sensitive to environmental noise.  
Different physical error processes affect reliability differently, making error mitigation essential for real-world quantum systems.

---

## Tech Stack

- Python
- Qiskit
- Qiskit Aer
- NumPy
- Matplotlib

---

## How to Run

```bash
pip install qiskit qiskit-aer matplotlib numpy
python main.py