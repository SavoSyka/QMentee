from qiskit import QuantumCircuit, assemble, Aer
#from qiskit_aer import AerSimulator
#from qiskit.visualization import plot_histogram, plot_bloch_vector
#from math import sqrt, pi

from random import randint

amount_of_qubits = randint(1, 10)
amount_of_blocks = randint(5, 10)

qc = QuantumCircuit(amount_of_qubits)
for i in range (0, amount_of_blocks):
    am_of_gates = 0
    qub = 0
    qub_type = 0
    qub1 = 0
    qub2 = 0
    qub3 = 0
    am_of_gates = randint(1, 3)
    if am_of_gates == 1:
        qub = randint(0,amount_of_qubits-1)
        qub_type  = randint(0,8)
        if qub_type == 0:
            qc.id(qub)
        if qub_type == 1:
            qc.h(qub)
        if qub_type == 2:
            qc.x(qub)
        if qub_type == 3:
            qc.y(qub)
        if qub_type == 4:
            qc.z(qub)
        if qub_type == 5:
            qc.s(qub)
        if qub_type == 6:
            qc.sdg(qub)
        if qub_type == 7:
            qc.t(qub)
        if qub_type == 8:
            qc.tdg(qub)
    if am_of_gates == 2:
        qub1 = randint(0,amount_of_qubits-1)
        qub2 = randint(0,amount_of_qubits-1)
        while (qub2 == qub1):
            qub2 = randint(0,amount_of_qubits-1)
        qub_type = randint(0,3)
        #print (qub1, qub2)
        if qub_type == 0:
            qc.cx(qub1, qub2)
        if qub_type == 1:
            qc.cz(qub1, qub2)
        if qub_type == 2:
            qc.swap(qub1, qub2)
        if qub_type == 3:
            qc.iswap(qub1, qub2)
    if am_of_gates == 3:
        qub1 = randint(0,amount_of_qubits-1)
        qub2 = randint(0,amount_of_qubits-1)
        while (qub2 == qub1):
            qub2 = randint(0,amount_of_qubits-1)
        qub3 = randint(0,amount_of_qubits-1)
        while ((qub3 == qub1) or (qub3 == qub2)):
            qub3 = randint(0,amount_of_qubits-1)
        qub_type = randint(0,1)
        if qub_type == 0:
            qc.ccx(qub1,qub2,qub3)
        if qub_type == 1:
            qc.ccz(qub1,qub2,qub3)
f = open('rand_circuit.qasm', 'w')
f.write(qc.qasm())
print(qc.qasm())
print(qc)
