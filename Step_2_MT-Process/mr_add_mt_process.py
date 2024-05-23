import math
import traceback

class MR_ADD():
    """ MR ADD 
    Change in the input -> Add a possitive constant
    Expected change in the output -> Increase or remain constant
    """
    ttd = None
    vs = None
    vs_string = None
    td_output = None
    ttd_output = None
    
    def __init__(self, td, cons):
        self.td = td
        self.cons = cons
    
    # MR_ADD -> Add a positive constant
    def followUpTD(self):
        aux_list = []
        
        if len(self.td) != 0 and type(self.td) == list:    
            for item in self.td:
                aux_list.append(item + self.cons)
        
        return aux_list
            
    def mrChecker(self, outputTD, outputTTD):
        error_message = None
        
        self.td_output = outputTD
        self.ttd_output = outputTTD
        self.ttd = self.followUpTD()
        
        if type(self.td_output) != list and type(self.ttd_output) != list:
            try:
                if math.isclose(outputTD, outputTTD, rel_tol=1e-9, abs_tol=0) or outputTD < outputTTD:
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
                comparison_result = [x < y for x, y in zip(outputTD, outputTTD)]

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
            'td' : self.td,
            'ttd': self.ttd,
            'td_output': self.td_output,
            'ttd_output': self.ttd_output,
            'vs_str': self.vs_string,
            'vs': self.vs,
        }
        
            
            