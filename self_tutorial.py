# https://www.youtube.com/watch?v=oaiQ5hYKHTE

class Employee:
    def set_salary(self, value): # set_salary is an attribute of a class that holds a 
                                # function object. 'self' here points to the class instance.
                                # That will be 'e' below
        self.salary = value # value is being passed to salary

e = Employee() # e is a class instance
e.set_salary(2000) # set_salary is a function
                    # we are passing 2000 to the value parameter, which will become salary
                    
print(e.salary) 

