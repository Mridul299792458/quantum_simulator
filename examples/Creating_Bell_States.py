from quantum_simulator import QuantumCircuit, QuantumMeasurement

							#### Creating Bell's States from |00> ####

### Bell's state: (|00> + |11>)/sqrt(2) 							
qc1 = QuantumCircuit(2)
print(f"Initial state: {qc1.state}")
qc1.h(0)
qc1.cx(0,1)
print(f"Final state: {qc1.state}")
measure = QuantumMeasurement(qc1.state)
measure.barplot()


### Bell's state: (|01> + |10>)/sqrt(2) 							
qc2 = QuantumCircuit(2)
print(f"Initial state: {qc2.state}")
qc2.h(0)
qc2.cx(0,1)
qc2.x(1)
print(f"Final state: {qc2.state}")
measure = QuantumMeasurement(qc2.state)
measure.barplot()


### Bell's state: (|00> - |11>)/sqrt(2) 							
qc3 = QuantumCircuit(2)
print(f"Initial state: {qc3.state}")
qc3.h(0)
qc3.cx(0,1)
qc3.z(0)
print(f"Final state: {qc3.state}")
measure = QuantumMeasurement(qc3.state)
measure.barplot()


### Bell's state: (|01> - |10>)/sqrt(2) 							
qc4 = QuantumCircuit(2)
print(f"Initial state: {qc4.state}")
qc4.h(0)
qc4.cx(0,1)
qc4.x(1)
qc4.z(0)
print(f"Final state: {qc4.state}")
measure = QuantumMeasurement(qc4.state)
measure.barplot()
