'''
Created on Sep 21, 2024

@author: Sumeet Agrawal
'''


class Employee:
    classtype = "simple"
    # self.class_var = 123 
    
    def __init__(self, nam, sal):
        # Whenever this Employee class will be instantiated, the object level variables will be initialized through this constructor
        self.name = nam
        self.salary = sal
        
        
    @property
    def get_name(self):
        return self.name
    
    def increase_sal(self, inc_num):
        self.salary = self.salary + inc_num
        print(f"new salary is: {self.salary}")
        
    
class DlpEmployee(Employee):
    
    def __init__(self, name, sal):
        super().__init__(name, sal)        
    
    def handle_escalation(self):
        print("DLP employee is handling the escalation")
        

if __name__ == '__main__':
    emp1 = DlpEmployee("Sumeet", 21000)
    print(emp1.classtype)
    #print(emp1.class_var)
    print(emp1.get_name)
    emp1.increase_sal(1000)
    emp1.handle_escalation()
    
'''    
CONCLUSIONS
1. Object of child class as well as Child class itself can all directly access parent class methods. No need to instantiate
2. Class variable before init is for maintaining class level constants and in init, we can initiate object variables...
... differently for each object (E.g., college name remains constant for all students but while creating student, we ...
... can initialize object for different college depts. at run time.
3. @property helps to access object values from methods as if accessing props / attributes...
...Helps to hide implementation (called as Encapsulation) - another imp concept of OOPS

'''

        
