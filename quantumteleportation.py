from qiskit import *

#3 qubit circuit and 3 classical bits
circuit = QuantumCircuit(3, 3)

# want to teleport information on q0 to q2

# apply x gate to q0
circuit.x(0)
#need to create entanglement between q1 and q2 by applying h gate on q1 and then controlled x gate between q1 and q2
circuit.h(1)
circuit.cx(1,2)
# need cx gate from q0 to q1 and h gate on q0
circuit.cx(0,1)
circuit.h(0)

#measure
circuit.barrier()
circuit.measure([0,1], [0,1])

circuit.barrier()
circuit.cx(1,2)
circuit.cz(0,2)

#see if q2 is now a classical 1 when measured
circuit.measure(2, 2)
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator, shots=1024).result()
counts = result.get_counts()
print(counts)
