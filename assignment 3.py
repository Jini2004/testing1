class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector): #"isintance" to check whether an operand is of a certain type before performing operations on it
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for+: Vector and {}".format(type(other)))
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type for -: Vector and {}".format(type(other))) 
        #"raise" to raise exceptions, which are special objects that indicate that an error or exceptional condition has occurred during the execution of a program
        
    def __mul__(self, scalar):
        if isinstance(scalar, (int,float)):
            return Vector(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Unsupported operand type for *: Vector and {}". format(type(scalar)))
        
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ValueError("Division by Zero is not allowed")
            return Vector(self.x / scalar, self.y/scalar)
        else:
            raise TypeError("Unsupported operand type for /: Vector and {}".format(type(scalar)))
        
    def __str__(self):
        return "Vector({}, {})".format(self.x, self.y)
    
#Demonstration
V1 = Vector(3,4)
V2 = Vector(1,2)

#Addition 
result_add = V1 + V2
print("Addition:", result_add)

#Substraction 
result_sub = V1 - V2
print("Substraction:", result_sub)

#Scalar Multification 
result_mul = V1 * 2
print("Scalar Multification:", result_mul)

#Scalar Division 
result_div = V1 / 2
print("Scalar Division:", result_div)