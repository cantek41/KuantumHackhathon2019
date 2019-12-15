from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram
import numpy as np


simulator = Aer.get_backend('qasm_simulator')

import pandas as pd
import random as rd

kapilar=["h","x","z","y"]

dizi=[]

colms=["Giris","kapilar","cikis"]

df=pd.DataFrame(columns=colms)
for i in range(1000):
    row=[]
    for j in range(4):
        a=rd.randint(0,3)       
        row.append(kapilar[a])
    dizi.append(row)


resultT=[]
for row in dizi:
    rowT=[]
    circuit = QuantumCircuit(1, 1)
    circuit.x(0)
    for kapi in row:
        if kapi=="h":
            circuit.h(0)
        elif kapi=="x":
            circuit.x(0)
        elif kapi=="y":
            circuit.y(0)
        elif kapi=="h":
            circuit.h(0)
    circuit.measure([0], [0])    
    job = execute(circuit, simulator, shots=1000)
    result = job.result()# Returns counts
    counts = result.get_counts(circuit)
    print(counts)
    a=0
    try:
        a=counts["1"]
    except:
        a=0
        
    resultT.append(rowT)
    k=row[0]+row[1]+row[2]+row[3]
    df.loc[len(df)]=[1,k,a]


filePath=r"C:\Users\cantek\Downloads\rr.xls"  
df.to_excel("rr.xls")
data={"kapilar":dizi,"sonuclar":resultT}
f=pd.DataFrame.from_dict(data, orient='index')

df1_transposed = f.T

df1_transposed.to_excel(filePath)

len(counts)
    