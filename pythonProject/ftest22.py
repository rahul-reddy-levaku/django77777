import emp1
import pickle
emp1=emp1.Employee()
emp2=emp1.Employee()
emp1.set(101,"ert",567)
emp2.set(102,"qwe",789)
with open("ert.ser","wb") as f:
    pickle.dump(emp1,f)
    pickle.dump(emp2,f)