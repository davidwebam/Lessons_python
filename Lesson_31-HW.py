"""
•Write Clock class, which will receive the number
of seconds in __init__.
•This class has a method (__str__) returning time
in HH:MM:SS format.
•Implement the magical methods of operators to
increase and decrease the number of seconds
and compare with each other.
"""

class Clock:
  def __init__(self, seconds):
    if not isinstance(seconds | int):
      raise TypeError('Seconds must be an integer')
    self.seconds = seconds
    
  def __str__(self):
    hours = self.seconds // 3600
    minutes = (self.seconds % 3600) // 60
    seconds = self.seconds % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'
  
  def __add__(self, other):
    if isinstance(other | int):
      return Clock(self.seconds + other)
    raise TypeError('Other must be an integer')
  
  def __radd__(self, other):
    return self.__add__(other)
  
  def __sub__(self, other):
    if isinstance(other | int):
      return Clock(self.seconds - other)
    raise TypeError('Other must be an integer')
  
  def __iadd__(self, other):
      if isinstance(other, int):
          self.seconds = (self.seconds + other) % 86400
          return self
      raise TypeError("Can only add integer seconds")

  # -=
  def __isub__(self, other):
      if isinstance(other, int):
          self.seconds = (self.seconds - other) % 86400
          return self
      raise TypeError("Can only subtract integer seconds")
    
    
c = Clock(3661)
print(c)          

c += 60
print(c)          

c = c + 3600
print(c)          

c -= 7200
print(c)          


"""
1․ Գրել Calculator class, որը․
   - __init__ ում կստանա թիվ և կստուգի այդ թվի int կամ float լինելը, հակառակ դեպքում կվերադարձնի Error,
   - կունենա միայն getter մեթոդ տրված թիվը ստանալու համար, իսկ այդ թիվը կլինի private,
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+, -, *, /, //, %, **),
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+=, -=, *=, /=, //=, %=, **=),
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (==, >, >=, <, <=, !=),
   - վերոնշյալ մեթոդները ռեալիզացված կլինեն այնպես, որ աշխատեն նաև Calculator կլասի երկու օբյեկտների համար,
   - կունենա համապատասխան magic մեթոդներ, որոնք թույլ կտան օբյեկտը տպելուց․ ստանալ թիվը (__str__), ստանալ թիվը և թվի տիպը (__repr__)։
"""

class Calculator:
    def __init__(self, number):
        if not isinstance(number, (int, float)):
            raise TypeError("Error: number must be int or float")
        self.__number = number   


    @property
    def number(self):
        return self.__number


    def __get_value(self, other):
        if isinstance(other, Calculator):
            return other.__number
        elif isinstance(other, (int, float)):
            return other
        else:
            raise TypeError("Unsupported type")


    def __add__(self, other):
        return Calculator(self.__number + self.__get_value(other))

    def __sub__(self, other):
        return Calculator(self.__number - self.__get_value(other))

    def __mul__(self, other):
        return Calculator(self.__number * self.__get_value(other))

    def __truediv__(self, other):
        return Calculator(self.__number / self.__get_value(other))

    def __floordiv__(self, other):
        return Calculator(self.__number // self.__get_value(other))

    def __mod__(self, other):
        return Calculator(self.__number % self.__get_value(other))

    def __pow__(self, other):
        return Calculator(self.__number ** self.__get_value(other))


    def __iadd__(self, other):
        self.__number += self.__get_value(other)
        return self

    def __isub__(self, other):
        self.__number -= self.__get_value(other)
        return self

    def __imul__(self, other):
        self.__number *= self.__get_value(other)
        return self

    def __itruediv__(self, other):
        self.__number /= self.__get_value(other)
        return self

    def __ifloordiv__(self, other):
        self.__number //= self.__get_value(other)
        return self

    def __imod__(self, other):
        self.__number %= self.__get_value(other)
        return self

    def __ipow__(self, other):
        self.__number **= self.__get_value(other)
        return self


    def __eq__(self, other):
        return self.__number == self.__get_value(other)

    def __ne__(self, other):
        return self.__number != self.__get_value(other)

    def __lt__(self, other):
        return self.__number < self.__get_value(other)

    def __le__(self, other):
        return self.__number <= self.__get_value(other)

    def __gt__(self, other):
        return self.__number > self.__get_value(other)

    def __ge__(self, other):
        return self.__number >= self.__get_value(other)


    def __str__(self):
        return str(self.__number)

    def __repr__(self):
        return f"Calculator(number={self.__number}, type={type(self.__number).__name__})"



a = Calculator(10)
b = Calculator(3)

print(a + b)        
print(a - 2)        
print(a * b)        
print(a / b)        

a += 5
print(a)            

print(a > b)        
print(repr(a))      
