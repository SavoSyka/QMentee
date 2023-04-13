#f = open('rand_circuit.qasm', 'r')
from qiskit import QuantumCircuit, assemble, Aer
#from qiskit_aer import AerSimulator
#from qiskit.visualization import plot_histogram, plot_bloch_vector
#from math import sqrt, pi

from random import randint
qc = QuantumCircuit.from_qasm_file('rand_circuit.qasm')
print(qc)
print(qc.data, sep='\n')
print(len(qc.data))

j = 0
decomp_circ = QuantumCircuit(len(qc.data))
for i in qc.data:
    if i[0].name == 'z':
        q = qc.data[j].qubits[0].index
        decomp_circ.z(q)
    if i[0].name == 'x':
        q = qc.data[j].qubits[0].index
        decomp_circ.x(q)
    if i[0].name == 'y':
        q = qc.data[j].qubits[0].index
        decomp_circ.y(q)
    if i[0].name == 'h':
        q = qc.data[j].qubits[0].index
        decomp_circ.h(q)
    if i[0].name == 't':
        q = qc.data[j].qubits[0].index
        decomp_circ.t(q)
    if i[0].name == 'tdg':
        q = qc.data[j].qubits[0].index
        decomp_circ.tdg(q)
    if i[0].name == 's':
        q = qc.data[j].qubits[0].index
        decomp_circ.s(q)
    if i[0].name == 'sdg':
        q = qc.data[j].qubits[0].index
        decomp_circ.sdg(q)


    if i[0].name == 'cz':
        q1 = qc.data[j].qubits[0].index
        q2 = qc.data[j].qubits[1].index
        print('cz', q1, q2)
        decomp_circ.cz(q1, q2)
    if i[0].name == 'cx':
        q1 = qc.data[j].qubits[0].index
        q2 = qc.data[j].qubits[1].index
        print('cx', q1, q2)
        decomp_circ.h(q2)
        decomp_circ.cx(q1, q2)
        decomp_circ.h(q2)
    if i[0].name == 'swap':
        # print(1)
        q1 = qc.data[j].qubits[0].index
        q2 = qc.data[j].qubits[1].index
        print('swap', q1, q2)
        decomp_circ.h(q2)
        decomp_circ.cz(q1, q2)
        decomp_circ.h(q2)

        decomp_circ.h(q1)
        decomp_circ.cz(q2, q1)
        decomp_circ.h(q1)

        decomp_circ.h(q2)
        decomp_circ.cz(q1, q2)
        decomp_circ.h(q2)
    if i[0].name == 'iswap':
        q1 = qc.data[j].qubits[0].index
        q2 = qc.data[j].qubits[1].index
        print('iswap', q1, q2)
        decomp_circ.s(q1)
        decomp_circ.s(q2)
        decomp_circ.h(q1)
        decomp_circ.cx(q1, q2)
        decomp_circ.cx(q2, q1)
        decomp_circ.h(q2)
    if i[0].name == 'ccx' or i[0].name == 'toffoli':
        q1 = qc.data[j].qubits[0].index
        q2 = qc.data[j].qubits[1].index
        q3 = qc.data[j].qubits[2].index
        print('toffoli', q1, q2, q3)

        decomp_circ.cz(q2, q3)
        decomp_circ.h(q3)
        decomp_circ.tdg(q3)
        decomp_circ.h(q3)
        decomp_circ.cz(q1, q3)
        decomp_circ.h(q3)
        decomp_circ.t(q3)
        decomp_circ.h(q3)
        decomp_circ.cz(q2, q3)
        decomp_circ.h(q3)
        decomp_circ.tdg(q3)
        decomp_circ.h(q3)
        decomp_circ.cz(q1, q3)
        decomp_circ.h(q3)
        decomp_circ.t(q3)
        decomp_circ.t(q2)
        decomp_circ.h(q3)
        decomp_circ.h(q2)
        decomp_circ.cz(q1, q2)
        decomp_circ.h(q2)
        decomp_circ.tdg(q2)
        decomp_circ.t(q1)
        decomp_circ.h(q2)
        decomp_circ.cz(q1, q2)
        decomp_circ.h(q2)

    if i[0].name == 'ccz':
        q1 = qc.data[j].qubits[0].index
        q2 = qc.data[j].qubits[1].index
        q3 = qc.data[j].qubits[2].index
        print('ccz', q1, q2, q3)

        decomp_circ.h(q3)
        decomp_circ.cz(q2, q3)
        decomp_circ.h(q3)
        decomp_circ.tdg(q3)
        decomp_circ.h(q3)
        decomp_circ.cz(q1, q3)
        decomp_circ.h(q3)
        decomp_circ.t(q3)
        decomp_circ.h(q3)
        decomp_circ.cz(q2, q3)
        decomp_circ.h(q3)
        decomp_circ.tdg(q3)
        decomp_circ.h(q3)
        decomp_circ.cz(q1, q3)
        decomp_circ.h(q3)
        decomp_circ.t(q3)
        decomp_circ.t(q2)

        decomp_circ.h(q2)
        decomp_circ.cz(q1, q2)
        decomp_circ.h(q2)
        decomp_circ.tdg(q2)
        decomp_circ.t(q1)
        decomp_circ.h(q2)
        decomp_circ.cz(q1, q2)
        decomp_circ.h(q2)

    j += 1
print(decomp_circ)
f = open('decomposed_circuit.qasm', 'w')
f.write(decomp_circ.qasm())