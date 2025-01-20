import numpy as np

class QuantumCircuit:
  """
  |0> = np.array([1,0]).
  |1> = np.array([0,1]).
  """
  def __init__(self, n, initial_state = 0):
    """
    Initializes the total number of qubits n, required in the quantum circuit. If initial_state == 0, this means that all
    the qubits are initialized in state |0>.

    The user can provide list of combined state if required.
    For e.g. if n = 2 and 1st qubit = (1/sqrt(2))(|0> + |1>) and 2nd qubit = |1> then,
    initial_state = [0,np.sqrt(2)*1,0,np.sqrt(2)*1]. If n = 2 and the initial state is a Bell's state = (|00> + |11>)/sqrt(2),
    then user can provide initial_state = [(1/sqrt(2))*1,0,0,(1/sqrt(2))*1].
    """
    self.n = n
    initial_state = np.array(initial_state)
    if initial_state.ndim == 0:
      self.state = np.zeros((2**self.n,))
      self.state[0] = 1
    else:
      self.state = initial_state
    self.state = self.state.astype(complex)
    self.binary_indices_list = [bin(i)[2:].zfill(self.n) for i in range(2**self.n)]
    self.basis_states = [f"|{s}>" for s in self.binary_indices_list]



                                                   ####### Single-Qubit Gates #######
  def h(self, qubit_position):
    """
    Single qubit Hadamard Gate.
    qubit_position: 0 to n-1.
    """
    operator = (1/np.sqrt(2))*np.array([[1,1],[1,-1]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None

  def x(self, qubit_position):
    """
    Single qubit Pauli X Gate.
    qubit_position: 0 to n-1.
    """
    operator = np.array([[0,1],[1,0]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None

  def y(self, qubit_position):
    """
    Single qubit Pauli Y Gate.
    qubit_position: 0 to n-1.
    """
    operator = np.array([[0,-1j],[1j,0]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None

  def z(self, qubit_position):
    """
    Single qubit Pauli Z Gate.
    qubit_position: 0 to n-1.
    """
    operator = np.array([[1,0],[0,-1]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None

  def s(self, qubit_position):
    """
    Single qubit S Gate.
    qubit_position: 0 to n-1.
    """
    operator = np.array([[1,0],[0,1j]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None

  def inverse_s(self, qubit_position):
    """
    Single qubit Inverse S Gate.
    qubit_position: 0 to n-1.
    """
    operator = np.array([[1,0],[0,-1j]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None

  def t(self, qubit_position):
    """
    Single qubit T Gate.
    qubit_position: 0 to n-1.
    """
    operator = np.array([[1,0],[0,np.exp(1j*np.sqrt(np.pi/4))]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None

  def inverse_t(self, qubit_position):
    """
    Single qubit Inverse T Gate.
    qubit_position: 0 to n-1.
    """
    operator = np.array([[1,0],[0,np.exp(-1j*np.sqrt(np.pi/4))]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None

  def p(self, qubit_position, phi):
    """
    Single qubit Phase Gate with phi in radians.
    qubit_position: 0 to n-1.
    """
    operator = np.array([[1,0],[0,np.exp(1j*phi)]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None

  def rx(self, qubit_position, phi):
    """
    Single qubit Rotation X Gate with phi in radians.
    qubit_position: 0 to n-1.
    """
    operator = np.array([[np.cos(phi/2),-1j*np.sin(phi/2)],[-1j*np.sin(phi/2),np.cos(phi/2)]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None

  def ry(self, qubit_position, phi):
    """
    Single qubit Rotation Y Gate with phi in radians.
    qubit_position: 0 to n-1.
    """
    operator = np.array([[np.cos(phi/2),-1*np.sin(phi/2)],[np.sin(phi/2),np.cos(phi/2)]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None

  def rz(self, qubit_position, phi):
    """
    Single qubit Rotation Z Gate with phi in radians.
    qubit_position: 0 to n-1.
    """
    operator = np.array([[np.exp(-1j*phi/2),0],[0,np.exp(1j*phi/2)]])

    if qubit_position == 0:
      gate = operator
      for i in range(1, self.n):
        gate = np.kron(gate, np.eye(2))
    elif qubit_position == self.n-1:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
    else:
      gate = np.eye(2)
      for i in range(1, qubit_position):
        gate = np.kron(gate, np.eye(2))
      gate = np.kron(gate, operator)
      for i in range(qubit_position+1, self.n):
        gate = np.kron(gate, np.eye(2))
    self.state = np.dot(gate, self.state)
    return None


                                                    ####### Two-Qubit Gates #######
  def cx(self, control_qubit, action_qubit):
    """
    Two qubit CNOT Gate.
    control_qubit, action_qubit: 0 to n-1.
    """
    binary_indices_array = np.array([[int(i) for i in char] for char in self.binary_indices_list])
    copy = binary_indices_array.copy()
    binary_indices_array[np.logical_and(copy[:,control_qubit] == 1, copy[:,action_qubit] == 0),action_qubit] = 1
    binary_indices_array[np.logical_and(copy[:,control_qubit] == 1, copy[:,action_qubit] == 1),action_qubit] = 0
    sorted_array = np.array([int(''.join(map(str, row)),2) for row in binary_indices_array])
    duplicate = self.state.copy()
    self.state = np.array([duplicate[i] for i in sorted_array])
    return None

  def cy(self, control_qubit, action_qubit):
    """
    Two qubit Controlled Y Gate.
    control_qubit, action_qubit: 0 to n-1.
    """
    binary_indices_array = np.array([[int(i) for i in char] for char in self.binary_indices_list])
    copy = binary_indices_array.copy()
    binary_indices_array[np.logical_and(copy[:,control_qubit] == 1, copy[:,action_qubit] == 0),action_qubit] = 1
    binary_indices_array[np.logical_and(copy[:,control_qubit] == 1, copy[:,action_qubit] == 1),action_qubit] = 0
    condition1 = np.where(np.logical_and(copy[:,control_qubit] == 1, copy[:,action_qubit] == 0))[0]
    condition2 = np.where(np.logical_and(copy[:,control_qubit] == 1, copy[:,action_qubit] == 1))[0]
    sorted_array = np.array([int(''.join(map(str, row)),2) for row in binary_indices_array])
    duplicate = self.state.copy()
    self.state = np.array([duplicate[i] for i in sorted_array])
    for i in condition1:
      self.state[i] = -1j*self.state[i]
    for i in condition2:
      self.state[i] = 1j*self.state[i]
    return None

  def cz(self, control_qubit, action_qubit):
    """
    Two qubit Controlled Z Gate.
    control_qubit, action_qubit: 0 to n-1.
    """
    binary_indices_array = np.array([[int(i) for i in char] for char in self.binary_indices_list])
    condition = np.where(np.logical_and(binary_indices_array[:,control_qubit] == 1, binary_indices_array[:,action_qubit] == 1))[0]
    for i in condition:
      self.state[i] = -self.state[i]
    return None

  def cp(self, control_qubit, action_qubit, k):
    """
    Two qubit Controlled Phase Gate with phase factor e^(i*2*pi/(2^k)).
    control_qubit, action_qubit: 0 to n-1.
    """
    binary_indices_array = np.array([[int(i) for i in char] for char in self.binary_indices_list])
    condition = np.where(np.logical_and(binary_indices_array[:,control_qubit] == 1, binary_indices_array[:,action_qubit] == 1))[0]
    for i in condition:
      self.state[i] = np.exp(1j*2*np.pi/(2**k))*self.state[i]
    return None

  def swap(self, qubit1, qubit2):
    """
    Two qubit SWAP Gate.
    qubit1, qubit2: 0 to n-1.
    """
    binary_indices_array = np.array([[int(i) for i in char] for char in self.binary_indices_list])
    copy = binary_indices_array.copy()
    binary_indices_array[np.logical_and(copy[:,qubit1] == 1, copy[:,qubit2] == 0),qubit2] = 1
    binary_indices_array[np.logical_and(copy[:,qubit1] == 1, copy[:,qubit2] == 0),qubit1] = 0
    binary_indices_array[np.logical_and(copy[:,qubit1] == 0, copy[:,qubit2] == 1),qubit2] = 0
    binary_indices_array[np.logical_and(copy[:,qubit1] == 0, copy[:,qubit2] == 1),qubit1] = 1
    sorted_array = np.array([int(''.join(map(str, row)),2) for row in binary_indices_array])
    duplicate = self.state.copy()
    self.state = np.array([duplicate[i] for i in sorted_array])
    return None


                                                    ####### Three-Qubit Gates #######

  def ccx(self, control_qubit1, control_qubit2, action_qubit):
    """
    Three qubit CCNOT or Toffoli Gate.
    control_qubit1, control_qubit2, action_qubit: 0 to n-1.
    """
    binary_indices_array = np.array([[int(i) for i in char] for char in self.binary_indices_list])
    copy = binary_indices_array.copy()
    binary_indices_array[np.logical_and(np.logical_and(copy[:,control_qubit1] == 1, copy[:,control_qubit2] == 1), copy[:,action_qubit] == 0),action_qubit] = 1
    binary_indices_array[np.logical_and(np.logical_and(copy[:,control_qubit1] == 1, copy[:,control_qubit2] == 1), copy[:,action_qubit] == 1),action_qubit] = 0
    sorted_array = np.array([int(''.join(map(str, row)),2) for row in binary_indices_array])
    duplicate = self.state.copy()
    self.state = np.array([duplicate[i] for i in sorted_array])
    return None

  def cswap(self, control_qubit, qubit1, qubit2):
    """
    Three qubit controlled SWAP Gate.
    control_qubit, qubit1, qubit2: 0 to n-1.
    """
    binary_indices_array = np.array([[int(i) for i in char] for char in self.binary_indices_list])
    copy = binary_indices_array.copy()
    binary_indices_array[np.logical_and(copy[:,control_qubit] == 1, np.logical_and(copy[:,qubit1] == 1, copy[:,qubit2] == 0)),qubit2] = 1
    binary_indices_array[np.logical_and(copy[:,control_qubit] == 1, np.logical_and(copy[:,qubit1] == 1, copy[:,qubit2] == 0)),qubit1] = 0
    binary_indices_array[np.logical_and(copy[:,control_qubit] == 1, np.logical_and(copy[:,qubit1] == 0, copy[:,qubit2] == 1)),qubit2] = 0
    binary_indices_array[np.logical_and(copy[:,control_qubit] == 1, np.logical_and(copy[:,qubit1] == 0, copy[:,qubit2] == 1)),qubit1] = 1
    sorted_array = np.array([int(''.join(map(str, row)),2) for row in binary_indices_array])
    duplicate = self.state.copy()
    self.state = np.array([duplicate[i] for i in sorted_array])
    return None
