import qiskit
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# On créer un circuit quantique avec n qubits et n bits classiques
n= 3
qc = QuantumCircuit( n, n)

# on applique des portes Hadamard (H) à nos n qubits, on mesure les qubits et on stocke les résultats dans les bits classiques correspondants
mesure=[i for i in range(n)]
for i in range(n):
    qc.h(i)
qc.measure(mesure, mesure)



# On compile pour l'executer sur un similateur
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1)
result = job.result()

counts = result.get_counts(qc)
bitstring= counts.most_frequent()
bitstring = bitstring[::-1] #big, little indian conversion
valueTube1 = int(bitstring,2)

normValueTube1= valueTube1/(2**n)

print(normValueTube1)


DistanceMax=3 # Valeur objective à choisir en fonction de la vitesse
normDistanceMax = DistanceMax/(2**n)

def respectDistanceTuyau (normValueTube1, normDistanceMax):
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, simulator)
    job = execute(compiled_circuit, simulator, shots=1)
    result = job.result()

    counts = result.get_counts(qc)
    bitstring2= counts.most_frequent()
    bitstring2 = bitstring2[::-1] #big, little indian conversion
    valueTube2 = int(bitstring2,2)

    normValueTube2= valueTube2/(2**n)
    while abs(normValueTube1-normValueTube2 )<normDistanceMax :
        normValueTube2=normValueTube2
        return normValueTube2
        
    return respectDistanceTuyau(normValueTube1, normDistanceMax)
    

