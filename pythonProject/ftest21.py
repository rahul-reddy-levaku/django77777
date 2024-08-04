
import pickle
import emp

with open("empt.ser","rb") as f:
    emp1=pickle.load(f)
    emp2=pickle.load(f)
    emp1.printEmployee()
    emp2.printEmployee()