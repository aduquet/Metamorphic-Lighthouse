import math
import traceback

class MR_INV():
    """ MR MR_INV 
    Change in the input -> Take the inverse of each element 
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
        aux_list = []
        
        # MR_INV -> Take the inverse of each element
        if len(self.test_data_one_input) != 0 and type(self.test_data_one_input) == list:    
            for item in self.test_data_one_input:
                if item != 0:
                    aux_list.append(1 / item )

                else:
                    aux_list.append('ZeroDivisionError')
        
        return aux_list
    
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
                comparison_result = [x > y for x, y in zip(outputTD, outputTTD)]

                if all(comparison_result):
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
        
            
            