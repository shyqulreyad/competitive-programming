from typing import List
class solution:
    def Sum_of_square(self,num):
        suum = 0
        while num > 0:
            digit = num % 10
            suum += digit *digit
        return suum
        
    def HappyNumber(self,number):
        Happy_map = {}
        while number !=1:
            number = self.Sum_of_square(number)
            if number in Happy_map:
                return "sad"
            Happy_map[number] = number
        return "happy"
        
        

            
                    
happy = solution()
print(happy.HappyNumber(9))

