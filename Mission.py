
from typing import Iterable

class Mission:
    
    def replace_first(items: list) -> Iterable:
        if len(items) > 1:
            first = items[0]
            items.pop(0)
            items.append(first)
        return items
    
    def checkio(number: int) -> str:
        # Your code here
        # It's main function. Don't remove this function
        # It's using for auto-testing and must return a result for check.

        # replace this for solution
        if(number % 3 == 0 and number % 5 == 0):
            return 'Fizz Buzz'
        elif(number % 3 == 0):
            return 'Fizz'
        elif(number % 5 == 0):
            return 'Buzz'
        else:
            str(number)
            
    def checkio(number, number2):
        if number % 15 == 0:
            return 'Fizz Buzz'
        if number % 5 == 0:
            return 'Buzz'
        if number % 3 == 0:
            return 'Fizz'
        return str(number)
    
    checkio=lambda n, m, o:("Fizz "*(1-n%3)+"Buzz "*(1-n%5))[:-1]or str(n)
                
#assert Mission.checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
#assert Mission.checkio(6) == "Fizz", "6 is divisible by 3"
#assert Mission.checkio(5) == "Buzz", "5 is divisible by 5"
#assert Mission.checkio(7) == "7", "7 is not divisible by 3 or 5"
