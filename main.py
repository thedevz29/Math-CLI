class Math:
    def __init__(self):
        pass
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
        
    def circumference(self):
        circum_1 = float(input("Enter the radius of the circle: "))
        print(f"The circumference of the circle is {2*3.14*circum_1}")
    
    def area_circle(self):
        ar_c_1 = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is {3.14*ar_c_1**2}")
        
    def peri_square(self):
        peri_sq_1= float(input("Enter the side of the square"))
        print(f"The perimeter of the square is {peri_sq_1*4}")
        
    def area_square(self):
        ar_sq_1 = float(input("Enter the side of the square: "))
        print(f"The area of the square is {ar_sq_1**2}")
    
    def peri_rectangle(self):
        peri_rect_1 = float(input("Enter the length of the rectangle: "))
        peri_rect_2 = float(input("Enter the breadth of the rectangle: "))
        print(f"The perimeter of the rectangle is : {2(peri_rect_1+peri_rect_2)}")
    
    def area_rectangle(self):
        ar_rect_1 = float(input("Enter the length of the rectangle: "))
        ar_rect_2 = float(input("Enter the breadth of the rectangle: "))
        print(f"The area of the rectangle is {ar_rect_1*ar_rect_2}")
        
    def peri_triangle(self):
        peri_tri_1 = float(input("Enter the 1st side of the triangle: "))
        peri_tri_2 = float(input("Enter the 2nd side of the triangle: "))
        peri_tri_3 = float(input("Enter the 3rd side of the triangle: "))
        print(f"The perimeter of the triangle is {peri_tri_1+peri_tri_2+peri_tri_3}")
        
    def area_triangle(self):
        ar_tri_1 = float(input("Enter the base of the triangle: "))
        ar_tri_2 = float(input("Enter the height of the triangle: "))
        print(f'The area of the triangle is {0.5*ar_tri_1*ar_tri_2}')
        
    def percentage(self):
        per_1 = float(input("Enter the value of which you want the percentage of : "))
        per_2 = float(input("Enter the number of percentage you want to take out of the value: "))
        print(f"The percentage is {(per_2/per_1)*100}%")
        
while True:
    main = Math()
    
    print("Welcome to the Math CLI created by Atharv Sharma")
    cmd = input(">>$ ")
    if cmd == "sum":
        main.add()
        
    