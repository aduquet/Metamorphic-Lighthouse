import random
import math
import traceback

class MR_EXC():
    """ MR EXC 
    Change in the input -> Remove an element
    Expected change in the output -> Decrease or remain constant
    """
    
    ttd = None
    vs = None
    vs_string = None
    td_output = None
    ttd_output = None
    
    def __init__(self, test_data_one_input):
        self.test_data_one_input = test_data_one_input
    
    def followUpTD(self):
        aux_list = self.test_data_one_input.copy()
        if len(self.test_data_one_input) != 0 and type(self.test_data_one_input) == list :
            
            position = random.randint(0, len(self.test_data_one_input)-1)
            aux_list.pop(position)
            return aux_list
        
        else:
            return []
    
    def mrChecker(self, outputTD, outputTTD):
        error_message = None

        self.td_output = outputTD
        self.ttd_output = outputTTD
        self.ttd = self.followUpTD()
        
        if type(self.td_output) != list and type(self.ttd_output) != list:
    
            try:
                if math.isclose(outputTD, outputTTD, rel_tol=1e-9, abs_tol=0) or outputTD > outputTTD:
                    self.vs = 0
                    self.vs_string = 'No-violate'

                else:
                    self.vs = 1
                    self.vs_string = 'Violate'
                
                return self.mrCheckerResult()
                    
            except TypeError:
                error_message = traceback.format_exc()
                self.vs = 'error'
                self.vs_string = 'error'
                return self.mrCheckerResult()
            
        else:
            try:
                if len(outputTD) > len(outputTTD):
                    self.vs = 0
                    self.vs_string = 'No-violate'

                else:
                    self.vs = 1
                    self.vs_string = 'Violate'
                
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
        
            
            