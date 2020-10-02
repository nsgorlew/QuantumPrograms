# bernstein-vazirani algorithm to guess a binary number out of n items in 1 try
# import libraries
from qiskit import *

secretnumber = '111000'

# specify circuit
circuit = QuantumCircuit(len(secretnumber)+1, len(secretnumber))

# apply h gate to every qubit but the last
circuit.h(range(len(secretnumber)))
# apply x gate on last qubit and h gate
circuit.x(len(secretnumber))
circuit.h(len(secretnumber))

circuit.barrier()

# box to encode secret number
for ii, yesno in enumerate(reversed(secretnumber)):
    if yesno == '1':
        circuit.cx(ii, len(secretnumber))

circuit.barrier()

# apply h gates to every qubit except the last
circuit.h(range(len(secretnumber)))

circuit.barrier()
circuit.measure(range(len(secretnumber)), range(len(secretnumber)))

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator, shots=1).result()
counts = result.get_counts()
print(counts)
