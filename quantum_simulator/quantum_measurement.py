import numpy as np
import matplotlib.pyplot as plt

class QuantumMeasurement:

  def __init__(self, state):
    self.state = state
    self.n = int(np.log2(len(self.state)) + 0.1)
    binary_indices_list = [bin(i)[2:].zfill(self.n) for i in range(2**self.n)]
    self.basis_state = [f'|{s}>' for s in binary_indices_list]
    self.probabilities = np.array([np.real(np.conjugate(self.state[i])*(self.state[i])) for i in range(len(self.state))])

  def collapse(self, list_qubits, state_qubits):
    """
    list_qubits: a list containing qubit positions from 0 to n-1 which are measured. For e.g. if I have 3 qubit circuit and want
    to measure 1st and 3rd qubit, then list_qubits = [0,2].

    state_qubits: a list containing arrays of state vectors onto which collapse is required. In the above example if I want 1st qubit
    to collapse onto |0> and 3rd to |1> then state_qubits = [[1,0], [0,1]].
    """
    m = len(state_qubits)
    for i in range(m):
      state_qubits[i] = np.outer(np.array(state_qubits[i]),np.conjugate(np.array(state_qubits[i])))
    operator = []
    j = 0
    for i in range(self.n):
      if i in list_qubits:
        operator.append(state_qubits[j])
        j += 1
      else:
        operator.append(np.eye(2))
    collapse_operator = operator[0]
    for i in range(1, len(operator)):
      collapse_operator = np.kron(collapse_operator, operator[i])
    self.state = np.dot(collapse_operator, self.state)
    norm = np.linalg.norm(self.state)
    self.collapse_probability = norm**2
    self.state = self.state/norm
    representation = []
    for i in range(len(self.state)):
      if np.abs(self.state[i]) > 1e-5:
        representation.append(f'{self.state[i]}{self.basis_state[i]}')
    self.collapsed_state = " + ".join(representation)
    return None

  def expectation(self, operator):
    """
    operator: Provide a list of strings with length equal to number of qubits. Each string represent Pauli X, Y or Z or I identity.
    operator: E.g. for 3 qubits, operator = ['X', 'Y', 'I'].
    """
    X = np.array([[0, 1],[0, 1]])
    Y = np.array([[0, -1j],[1j, 0]])
    Z = np.array([[1, 0],[0, -1]])
    I = np.array([[1, 0],[0, 1]])
    observable = eval(operator[0])
    for i in range(1, len(operator)):
      observable = np.kron(observable, eval(operator[i]))
    self.expectation_value = np.dot(np.conjugate(self.state), np.dot(observable, self.state))
    print(self.expectation_value)
    return None

  def barplot(self):
    """
    Plots the probabilities of the basis states.
    """
    plt.bar(self.basis_state, np.real(np.conjugate(self.state)*self.state))
    plt.xlabel("Basis States")
    plt.ylabel("Probabilities")
    plt.show()
    return None
