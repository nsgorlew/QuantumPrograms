from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# circuit with one quantum bit and one classical bit
circuit = QuantumCircuit(1, 1)
#add an X-gate
circuit.x(0)
simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit,backend=simulator).result()
statevector = result.get_statevector()
print(statevector)

#measure the first bit and put result into first classical bit
circuit.measure([0], [0])
backend = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=backend, shots=1024).result()
counts = result.get_counts()

