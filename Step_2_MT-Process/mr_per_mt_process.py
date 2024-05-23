import random
import math
import traceback

class MR_PER():
    """ MR PER 
    Change in the input -> Randomly permute the elements
    Expected change in the output -> Remain constant
    """
    
    ttd = None
    vs = None
    vs_string = None
    td_output = None
    ttd_output = None
    
    def __init__(self, test_data_one_input):
        self.test_data_one_input = test_data_one_input
    
    def followUpTD(self):
        
        all_equal = len(set(self.test_data_one_input)) == 1
                
        aux_list = self.test_data_one_input.copy()
        if all_equal != 1 and len(self.test_data_one_input) != 0 and type(self.test_data_one_input) == list:
            while self.test_data_one_input == aux_list:
                random.shuffle(aux_list)
            return aux_list
        else:
            return aux_list
        
    def mrChecker(self, outputTD, outputTTD):
        
        self.td_output = outputTD
        self.ttd_output = outputTTD
        self.ttd = self.followUpTD()

        if type(self.td_output) != list and type(self.ttd_output) != list:
            try:
                if math.isclose(outputTD, outputTTD, rel_tol=1e-9, abs_tol=0):
                    self.vs = 0
                    self.vs_string = 'No-violate'
                
                else:
                    self.vs = 1
                    self.vs_string = 'Violate'
                    # return 1, 'Violated'
                    
                return self.mrCheckerResult()
            
            except TypeError:
                error_message = traceback.format_exc()
                self.vs = 'error'
                self.vs_string = 'error'
                return self.mrCheckerResult()
        else:
            try:
                if set(outputTD) == set(outputTTD):
                    self.vs = 0
                    self.vs_string = 'No-violate'
                
                else:
                    self.vs = 1
                    self.vs_string = 'Violate'
                    # return 1, 'Violated'
                    
                return self.mrCheckerResult()
            
            except TypeError:
                error_message = traceback.format_exc()
                self.vs = 'error'
                self.vs_string = 'error'
                return self.mrCheckerResult()            
                
    def mrCheckerResult(self):
        
        return {
            'td' : self.test_data_one_input,
            'ttd': self.ttd,
            'td_output': self.td_output,
            'ttd_output': self.ttd_output,
            'vs_str': self.vs_string,
            'vs': self.vs,
        }
        
            
            