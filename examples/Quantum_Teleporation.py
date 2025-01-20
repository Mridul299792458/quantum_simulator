from quantum_simulator import *
from numpy import kron, array

""" Quantum Teleportation using the Bell's State |b> = (\00> + \11>)/sqrt to transport the information |psi> = (alpha*\0> + beta*\1>) 
from Alice's qubit to Bob's Qubit. """


def state_representation(A,B):
	C = []
	for i in range(len(A)):
		if abs(B[i]) > 1e-5:
			C.append(f"{B[i]}{A[i]}")
	C = " + ".join(C)
	return C
		

## Create the Bell state |b>.
qc = QuantumCircuit(2)
print(f"Initial state: {state_representation(qc.basis_states, qc.state)}")
print("\n")
qc.h(0)
qc.cx(0,1)
b = qc.state
print(f"|b> = {state_representation(qc.basis_states, qc.state)}")
print("\n")

"""
1st qubit goes to Alex and 2nd goes to Bob. They are seperated in space.
"""

## Define the state |psi>.
# example values of alpha and beta:
alpha = 0.5
beta = 0.8660
psi = array([0.5, 0.8660])
print(f"alpha = {alpha}, beta = {beta}")
print("\n")


## Create a tensor product state |phi> = |psi>|b>.
phi = kron(psi, b)

"""
1st and 2nd qubit is with Alex and 3rd is with Bob. Hence, Alice can measure first two qubits.
"""

## Alex measures first two qubits and sends the information to Bob through classical channels. The results of measurement for Alex could collapse the state for first two qubits to: |00> or |01> or |10> or |11>.
# Let's consider all the posibilities and send information to Bob as M,N which represents measurement states of 1st and 2nd qubit respectively.

## Create a new quantum circuit with 3 qubits and initial state as |phi>.
circuit = QuantumCircuit(3, phi)
 

## Use Bell Measurement between 1st and 2nd qubits.
circuit.cx(0,1)
circuit.h(0)
print(f"|phi> = {state_representation(circuit.basis_states, circuit.state)}")
print("\n")

measurement00 = QuantumMeasurement(circuit.state)
measurement01 = QuantumMeasurement(circuit.state)
measurement10 = QuantumMeasurement(circuit.state)
measurement11 = QuantumMeasurement(circuit.state)

# Collapsing the state after measurement.
measurement00.collapse([0,1],[[1,0],[1,0]])
measurement01.collapse([0,1],[[1,0],[0,1]])
measurement10.collapse([0,1],[[0,1],[1,0]])
measurement11.collapse([0,1],[[0,1],[0,1]])


# If Alex sends 00 Bob gets:
print(f"Alex measures 00 then  |collapsed_state> = {state_representation(circuit.basis_states, measurement00.state)}")
print("\n")

# If Alex sends 01 Bob gets:
print(f"Alex measures 01 then  |collapsed_state> = {state_representation(circuit.basis_states, measurement01.state)}")
print("\n")
circuit.state = measurement01.state
circuit.x(2)
print(f"Z^(1)X^(0)|collapsed_state> = {state_representation(circuit.basis_states, circuit.state)}")
print("\n")

# If Alex sends 10 Bob gets:
print(f"Alex measures 10 then  |collapsed_state> = {state_representation(circuit.basis_states, measurement10.state)}")
print("\n")
circuit.state = measurement10.state
circuit.z(2)
print(f"Z^(0)X^(1)|collapsed_state> = {state_representation(circuit.basis_states, circuit.state)}")
print("\n")

# If Alex sends 11 Bob gets:
print(f"Alex measures 11 then  |collapsed_state> = {state_representation(circuit.basis_states, measurement11.state)}")
print("\n")
circuit.state = measurement11.state
circuit.x(2)
circuit.z(2)
print(f"Z^(1)X^(1)|collapsed_state> = {state_representation(circuit.basis_states, circuit.state)}")
print("\n")









