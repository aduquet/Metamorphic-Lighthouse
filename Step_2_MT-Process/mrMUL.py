import math
import traceback
import pandas as pd

def _ttd(td, const):
    ttdAux = []
    if isinstance(td, list):
        for item in td:
            ttdAux.append(item * const)
        return ttdAux
    
    if isinstance(td, int):
        return td * const

class MR_MUL:
    def __init__(self, *args):
        # Constructor for MR_ADD class
        
        # Store the input arguments as tdArgs
        self.tdArgs = args
        
        # Initialize const to None
        self.const = None
        
        # Lists to store column names for td and ttd
        self.keyNames_td = []
        self.keyNames_ttd = []
        
        # Lists to store the results of _ttd for td and ttd
        self.ttd = []
        self.td = []
        
        self.vs = None
        self.vs_string = None

    def followUP(self, const):
        # Method to perform follow-up calculations
        
        # Set the value of const
        self.const = const
        
        # Iterate through the input arguments
        for i, arg in enumerate(self.tdArgs):
            # Generate column names for td and ttd
            self.keyNames_td.append('td_' + str(i + 1) + '_mr_mul')
            self.keyNames_ttd.append('ttd_' + str(i + 1) + '_mr_mul')
            
            # Calculate and store the result of _ttd for td
            self.ttd.append(_ttd(td=arg, const=self.const))
            
            # Store the arg 
            self.td.append(arg) 
            
        # Create a DataFrame with columns for td
        self.df = pd.DataFrame(columns=self.keyNames_td)
        
        # Create a DataFrame with columns for ttd (Note: You should adjust this based on your requirements)
        df_aux = pd.DataFrame(columns=self.keyNames_ttd)
        
        # Insert the calculated values for td into the DataFrame
        self.df.loc[len(self.df)] = self.td
        
        # Insert the calculated values for ttd into the DataFrame (Note: You should adjust this based on your requirements)
        df_aux.loc[0] = self.ttd

        # Concatenate the two DataFrames horizontally
        result = pd.concat([self.df, df_aux], axis=1)

        return result
    
    def mrChecker(self, td_output, ttd_output):
        
        error_message = None
        
        try:
            if isinstance(td_output, list) and isinstance(ttd_output, list):
                #TODO: check element by element comparison 
                pass   
            
            else:
                if math.isclose(td_output, ttd_output, rel_tol= 1e-9) or td_output < ttd_output:
                    self.vs = 0
                    self.vs_string = 'no-violated'
                    
                else:
                    self.vs = 1
                    self.vs_string = 'violated'
                
                return self.mrCheckerResults()
                
        except (TypeError, ValueError, ZeroDivisionError):
            error_message = traceback.format_exc()
            
            # TODO: check what exception type occured :) 
            # TODO: save error message in txt with the td id
            
            self.vs = 'error'
            self.vs_string = 'error'
    
    def mrCheckerResults(self):
        return {
            'vs_mr_add': self.vs,
            'vs_mr_add': self.vs_string
        }
# Example Usage
td_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3], 3,4,5]
td_list = [1, 2, 3]

cons = 2
mr_add = MR_MUL(td_list)
print(mr_add.followUP(cons))
