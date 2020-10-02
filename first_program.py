# import libraries
from qiskit import *
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit.tools.monitor import job_monitor

# create 2 bit quantum register
qr = QuantumRegister(2)

# create 2 bit classical register
cr = ClassicalRegister(2)

#create quantum circuit
circuit = QuantumCircuit(qr, cr)

#create entanglement with hadamard gate
circuit.h(qr[0])

#quantum logical gate (controlled x gate)
circuit.cx(qr[0], qr[1])

# measure from quantum registers and store in classical registers
circuit.measure(qr, cr)

#simulate quantum circuit on local machine
simulator = Aer.get_backend('qasm_simulator')

#execute circuit
result = execute(circuit, backend=simulator).result()
plot_histogram(result.get_counts(circuit))

IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_16_melbourne')
job = execute(circuit, backend=qcomp)
job_monitor(job)
result = job.result()
plot_historgram(result.get_counts(circuit))


