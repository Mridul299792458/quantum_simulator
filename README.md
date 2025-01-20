<<<<<<< HEAD
# Quantum Circuit Simulator

A Python package for simulating quantum circuits with support for various quantum gates, measurements, and visualizations. This simulator allows you to create and manipulate quantum circuits, apply quantum gates, and perform measurements on the resulting quantum states.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Features

### Quantum Gates
- **Single-Qubit Gates**
  - Hadamard Gate (H)
  - Pauli Gates (X, Y, Z)
  - Phase Gates (S, T, Inverse S, Inverse T)
  - Rotation Gates (Rx, Ry, Rz)
  - Phase Rotation Gate (P)

- **Two-Qubit Gates**
  - CNOT (Controlled-X)
  - Controlled-Y
  - Controlled-Z
  - SWAP
  - Controlled Phase Gate

- **Three-Qubit Gates**
  - Toffoli Gate (CCNOT)
  - Controlled-SWAP (Fredkin Gate)

### Measurement Capabilities
- State Vector Analysis
- Quantum State Collapse
- Expectation Value Calculations
- Probability Distribution Visualization

## Installation

### From source
```bash
git clone https://github.com/Mridul299792458/quantum_simulator.git
cd quantum_simulator/dist
pip install quantum_simulator-0.1.0-py3-none-any.whl
or
pip install quantum_simulator-0.1.0.tar.gz .
```

## Quick Start

### Creating a Bell State
```python
from quantum_simulator import QuantumCircuit, QuantumMeasurement

# Initialize a 2-qubit circuit
qc = QuantumCircuit(2)

# Create Bell state (|00> + |11>)/√2
qc.h(0)    # Apply Hadamard to first qubit
qc.cx(0,1) # Apply CNOT with control on first qubit

# Measure the state
measurement = QuantumMeasurement(qc.state)
measurement.barplot()
```

### Quantum Teleportation
```python
# Initialize 3-qubit circuit
qc = QuantumCircuit(3)

# Prepare the state to teleport (qubit 0)
qc.h(0)
qc.p(0, np.pi/4)

# Create Bell pair between qubits 1 and 2
qc.h(1)
qc.cx(1, 2)

# Perform teleportation operations
qc.cx(0, 1)
qc.h(0)

# Measure the state
measurement = QuantumMeasurement(qc.state)
measurement.barplot()
```

## Documentation

### QuantumCircuit Class
The main class for creating and manipulating quantum circuits.

```python
circuit = QuantumCircuit(n, initial_state=0)
```
Parameters:
- `n`: Number of qubits
- `initial_state`: Initial state of qubits (default: all qubits in |0⟩)

### Single-Qubit Gates
```python
circuit.h(qubit)              # Hadamard gate
circuit.x(qubit)              # Pauli-X gate
circuit.y(qubit)              # Pauli-Y gate
circuit.z(qubit)              # Pauli-Z gate
circuit.t(qubit)              # T gate
circuit.s(qubit)              # S gate
circuit.inverse_t(qubit)      # Inverse T gate
circuit.inverse_s(qubit)      # Inverse S gate
circuit.rx(qubit, θ)          # Rotation around X-axis
circuit.ry(qubit, θ)          # Rotation around Y-axis
circuit.rz(qubit, θ)          # Rotation around Z-axis
circuit.p(qubit, φ)           # Phase rotation
```

### Multi-Qubit Gates
```python
circuit.cx(control, target)    # CNOT gate
circuit.cy(control, target)    # Controlled-Y gate
circuit.cz(control, target)    # Controlled-Z gate
circuit.swap(qubit1, qubit2)   # SWAP gate
circuit.cswap(control, qubit1, qubit2)   # Controlled-SWAP gate
circuit.ccx(control1, control2, target)  # Toffoli gate
```

### QuantumMeasurement Class
Class for performing measurements and analyzing quantum states.

```python
measurement = QuantumMeasurement(state)
```

Methods:
```python
# Collapse state by measuring specific qubits
measurement.collapse(qubit_list, state_list)

# Calculate expectation value
measurement.expectation(operator)

# Visualize state probabilities
measurement.barplot()
```

## Examples

Check the [examples](examples/) directory for more detailed examples including:
- Bell State Creation
- Quantum Teleportation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Requirements

- Python ≥ 3.8
- NumPy ≥ 1.19.0
- Matplotlib ≥ 3.3.0

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Mridul Singhal
- GitHub: [Mridul299792458](https://github.com/Mridul299792458)

## Citation

If you use this package in your research, please cite:
```bibtex
@software{quantum_simulator,
  author = {Singhal, Mridul},
  title = {Quantum Circuit Simulator},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/Mridul299792458/quantum-simulator}
}
```

## Acknowledgments

- Thanks to all contributors who have helped with the development of this package
- Inspired by various quantum computing frameworks and simulators
=======
Quantum Simulator.
>>>>>>> 8190ac511fb24c320f9c7536f0b98734718a04b7
