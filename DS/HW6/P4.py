class Calculator:
    """
    Key strategy : put digits and operation in buffer and excute at transaction
    0 -> 01 -> 013 -> 0135
    if +-, append the number in buffer to list
    """

    def __init__(self):
        self.result = 0
        self.formula = []
        self.curruent_digit = ""
    
    def buffer_to_list(self):
        #if there is something in buffer,
        if self.curruent_digit != "":
            #turn things in buffer to int
            num = int(self.curruent_digit)
            # add to formula
            self.formula.append(num)
            #initialize
            self.curruent_digit = ""

    def digit(self, num):
        # add input number to buffer
        self.curruent_digit += str(num)

    def plus(self):
        self.buffer_to_list()
        if self.formula[-1] == "+":
            pass
        elif self.formula[-1] == "-":
            self.formula[-1] = "+"
        else:
            self.formula.append("+")

    def minus(self):
        self.buffer_to_list()
        if self.formula[-1] == "-":
            pass
        elif self.formula[-1] == "+":
            self.formula[-1] = "-"
        else:
            self.formula.append("-")

    def clear(self):
        self.curruent_digit = ""
        self.formula = []




    def equal(self):
        # when there is somthing in buffer and nothing in formula
        if (self.curruent_digit == "") and (len(self.formula) == 0) :
            #return current digit
            return 0
        
        self.buffer_to_list()

         # Turn formula into result
        result = 0
        result = self.formula[0]
        # odd i items are operator, even i items are numbers
        for i in range(1,len(self.formula),2):
            if self.formula[i] == '+':
                result += self.formula[i+1]
            else:
                result -= self.formula[i+1]
        return result
