import pandas as pd 

T0 = pd.read_csv("TEST 0.csv", sep = ";")
T1 = pd.read_csv("TEST 1.csv", sep = ";")
T2 = pd.read_csv("TEST 2.csv", sep = ";")
T3 = pd.read_csv("TEST 3.csv", sep = ";")
T4 = pd.read_csv("TEST 4.csv", sep = ";")
Tlite = pd.read_csv('TEST lite.csv', sep=";")
Tr0 = pd.read_csv("TRAIN 0.csv", sep = ";")
Tr1 = pd.read_csv("TRAIN 1.csv", sep = ";")
Tr2 = pd.read_csv("TRAIN 2.csv", sep = ";")
Tr3 = pd.read_csv("TRAIN 3.csv", sep = ";")
Tr4 = pd.read_csv("TRAIN 4.csv", sep = ";")

print(Tr3)