import random


class InputTransformed():
    
    def __init__(self, test_data_one_input):
        self.test_data_one_input = test_data_one_input
        # self.cons = cons
    
    # MR_PER -> Permute the components
    def mrPER(self):
        
        aux_list = self.test_data_one_input
        if type(self.test_data_one_input) == list:
            while self.test_data_one_input == aux_list:
                self.test_data_one_input = random.shuffle(self.test_data_one_input)

        return aux_list
    
    # MR_ADD -> Add a positive constant
    def mrADD(self, cons):
        aux_list = []
        
        if len(self.test_data_one_input) != 0 and type(self.test_data_one_input) == list:    
            for item in self.test_data_one_input:
                aux_list.append(item+cons)
      
        return aux_list
    
    # MR_MUL -> Multiply by a positive constant
    def mrMUL(self, cons):
        
        aux_list = []
        
        if len(self.test_data_one_input) != 0 and type(self.test_data_one_input) == list:    
            for item in self.test_data_one_input:
                aux_list.append(item * cons)
      
        return aux_list
    
    # MR_INV -> Take the inverse of each element 
    def mrINV(self):
        
        aux_list = []
        
        if len(self.test_data_one_input) != 0 and type(self.test_data_one_input) == list:    
            for item in self.test_data_one_input:
                
                if item != 0:
                    aux_list.append(1 / item )

                else:
                    aux_list.append('ZeroDivisionError')
                    
        return aux_list
    
    # MR_INC -> Add a new element (first,last position? )
    def mrINC(self, cons):
        
        if len(self.test_data_one_input) != 0 and type(self.test_data_one_input) == list :
            
            position = random.randint(0, len(self.test_data_one_input))
            self.test_data_one_input.insert(position, cons)
            
            return self.test_data_one_input
        
        else:
            return self.test_data_one_input.insert(cons)

    # MR_EXC -> Remove an element  (first,last position? )
    def mrEXC(self):
        
        if len(self.test_data_one_input) != 0 and type(self.test_data_one_input) == list :
            
            position = random.randint(0, len(self.test_data_one_input)-1)
            self.test_data_one_input.pop(position)
            return self.test_data_one_input
        
        else:
            return []
            