
import pickle
with open("ert.ser",'rb') as f:
    emp2=pickle.load(f)
    emp1=pickle.load(f)
    emp1.get()
    emp2.get()