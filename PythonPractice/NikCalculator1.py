# update this calculator adding bodmas aclculator like{ (1+2+3+4)/3 }
class Calculator:
  def__init__(self, num1,num2):
    self.num1=num1
    self.num2=num2

  ans=True
  while ans:
      print ("""
      1.Addition 
      2.Subtraction
      3.Multiplication
      4.Division
      5.Exit
      """)
    
    
      #function for all the operations
      def operations(self):
        if respond==1:
          print("The addition is",(self.num1 + self.num2))
        elif respond==2:
          print("The subtraction is",(self.num1 - self.num2))
        elif respond==3:
          print("The Multiplication is",(self.num1 * self.num2))
        elif respond==4:
          print("The Division is",(self.num1 / self.num2)) 
        elif ans !="":
          print("\n Invalid Choice Try again")

    

try:
      #taking input from user and validating it
      response=input("Enter your choice : ") 
      respond=int(response)
      if(respond==5):
        print('exited')
        exit(0)
    
      val1=input("Enter first number : ")
      val2=input("Enter second number:")
    
      num1=float(val1)
      num2=float(val2)
except ZeroDivisionError as e:
      print('Exception Occur:Zero Division Error',e)
except ValueError as e:
      print('invalid input>> only integer or float values are acceptable',e)
except Exception as e:
      print('OOPS, SOMETHING WENT WRONG!>> PleaseTry Again',e)


obj=Calculator
obj.operations(num1,num2)
