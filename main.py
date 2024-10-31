class Commands:
    def __init__(self, user):
        self.user = user
        if user == "Atharv":
            print("Access Granted")
        else:
            print("Acess Denied")
            exit()
            
    def add(self):
        add_1 = float(input("Enter the first number which you want to add: "))
        add_2= float(input("Enter the second number you want to add:"))
        print(f"The sum is {add_1+add_2}")
    
    def subtract(self):
        
        sub_1 = float(input ("Please enter the first number : "))
        sub_2 = float(input("Please ener the second number : "))
        print(f"The difference is {sub_1-sub_2}:")
        
    def multiply(self):
        
        mul_1 = float(input ("Please enter the first number : "))
        mul_2 = float(input("Please ener the second number : "))
        print(f"The product is {mul_1*mul_2}")
        
    def divide(self):
        div_1= float(input ("Please enter the first number : "))
        div_2 = float(input("Please enter the second number : "))
        try:
            print(f"The qoutient is :{div_1/div_2}")
            
        except ZeroDivisionError:
            print("OOPS THERE IS A ZERODIVISION ERROR")


    def square(self):
        sq_1 = float(input("Enter the number you want to find the square of: "))
        print(f"The square of the number is : {sq_1**2}")
        
    
    def cube(self):
        cu_1 = float(input("Enter the number you want the cube of: "))
        print(f"The cube of the number is {cu_1**3}")
        
    def sq_root(self):
        sqrt_1 = float(input("Enter the number you want the square root of: "))
        
        print(f"The sqaure root of the number is {sqrt_1 ** 0.5}")
        
    def cu_root(self):
        curt_1 = float(input("Enter the number you want the cube root of : "))
        print(f"The cube root of the number is {curt_1**(1/3)}")
        
    def remainder(self):
        rem_1= float(input ("Please enter the first number : "))
        rem_2 = float(input("Please enter the second number : "))
        print(f"The remainder is {rem_1%rem_2}")
        
    def exponent(self):
        ex_1 = float(input("Enter the base of the exponent : "))
        ex_2 = float(input("Enter the power of the exponent: "))
        print(f"The number calculated is {ex_1**ex_2}")
        
        