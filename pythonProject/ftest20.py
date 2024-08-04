import emp
import pickle
emp1=emp.Employee()
emp2=emp.Employee()
emp1.setEmployee(101,"qwe",123)
emp2.setEmployee(102,"asd",456)
with open("empt.ser","wb") as f:
    pickle.dump(emp1,f)
    pickle.dump(emp2,f)