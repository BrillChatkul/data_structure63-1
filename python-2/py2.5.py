class funString:
    input_String = ''
    input_Number = 0
    output_String = ''
    def __init__(self,input_String,input_Number):
        self.input_String = input_String
        self.input_Number = input_Number

        if self.input_Number == 1:
            self.output_String = str(len(self.input_String))
            
        elif self.input_Number == 2:
            
            for i in self.input_String :
                if(ord(i)<90):
                    i = chr(ord(i)+32)
                else:
                    i = chr(ord(i)-32)
                self.output_String += i
        
        elif self.input_Number == 3:
            idx_input = len(self.input_String)
            while idx_input > 0:
                idx_input -= 1
                self.output_String += self.input_String[idx_input]
                
        elif self.input_Number == 4:
            for i in self.input_String:
                if i not in self.output_String:
                    self.output_String += i


           
       
    def __str__(self):
        return self.output_String
    
    


    

ScanInput = input('Enter String and Number of Function : ')
DataList = ScanInput.split()
dString = DataList[0]
dNumber = int(DataList[1])
a = funString(dString,dNumber)
print(a)
