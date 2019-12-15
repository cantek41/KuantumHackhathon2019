from qiskit import(
  QuantumCircuit,
  execute,
  Aer)


simulator = Aer.get_backend('qasm_simulator')

def send(status,row):
    circuit = QuantumCircuit(1, 1)
    if status==1:
        circuit.x(0)        
    for kapi in row:
        if kapi=="h":
            circuit.h(0)
        elif kapi=="x":
            circuit.x(0)
        elif kapi=="y":
            circuit.y(0)
        elif kapi=="z":
            circuit.z(0)
    circuit.measure([0], [0])    
    job = execute(circuit, simulator, shots=1000)
    result = job.result()# Returns counts
    counts = result.get_counts(circuit)
#    print(counts)
    return counts