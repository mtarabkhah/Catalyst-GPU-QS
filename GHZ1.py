import sys
import time
from catalyst import qjit
import pennylane as qml

numQubits = 26

@qml.qnode(qml.device("lightning.qubit", wires=numQubits))
def circuit():
        start_time = time.time()

        qml.Hadamard(wires=25)
        qml.CNOT(wires=[24, 23])
        qml.CNOT(wires=[23, 22])
        qml.CNOT(wires=[22, 21])
        qml.CNOT(wires=[21, 20])
        qml.CNOT(wires=[20, 19])
        qml.CNOT(wires=[19, 18])
        qml.CNOT(wires=[18, 17])
        qml.CNOT(wires=[17, 16])
        qml.CNOT(wires=[16, 15])
        qml.CNOT(wires=[15, 14])
        qml.CNOT(wires=[14, 13])
        qml.CNOT(wires=[13, 12])
        qml.CNOT(wires=[12, 11])
        qml.CNOT(wires=[11, 10])
        qml.CNOT(wires=[10, 9])
        qml.CNOT(wires=[9, 8])
        qml.CNOT(wires=[8, 7])
        qml.CNOT(wires=[7, 6])
        qml.CNOT(wires=[6, 5])
        qml.CNOT(wires=[5, 4])
        qml.CNOT(wires=[4, 3])
        qml.CNOT(wires=[3, 2])
        qml.CNOT(wires=[2, 1])
        qml.CNOT(wires=[1, 0])

        end_time = time.time()
        return (qml.state(), end_time - start_time)

jitted_circuit = qjit(circuit)
start_time = time.time()
(stateVec, execTime) = jitted_circuit()
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")