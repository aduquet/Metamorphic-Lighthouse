import os
import sys
import json
import tempfile

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../additional_attributes_list'))
from additional_attributes_list.list_descripter import ListDescripter

class FileParser():
    
    # id: str | None
    # data_attribute: dict | None
    
    def __init__(self, data: dict) -> None:
        self.data = data
        
    def get_td(self):
        
        for i in range(0,len(self.data)):
            td_list = self.data[str(i)]['td']
            descripter = ListDescripter(td_list)
            data_attribute = self.data.copy()
                        
            if len(td_list) != 0:
                
                data_attribute[str(i)]['size'] = descripter.get_length()
                data_attribute[str(i)]['has_zero'] = descripter.has_zero()
                data_attribute[str(i)]['cnt_zero'] = descripter.cnt_zeros()
                data_attribute[str(i)]['cnt_p_numbers'] = descripter.cnt_positive_numbers()
                data_attribute[str(i)]['cnt_n_number'] = descripter.cnt_negative_numbers()
                data_attribute[str(i)]['pp_numbers'] = descripter.pp_numbers()
                data_attribute[str(i)]['pn_numbers'] = descripter.pn_numbers()
                data_attribute[str(i)]['pp_greater_pn'] = False if  descripter.pp_numbers() > descripter.pn_numbers() else True
                data_attribute[str(i)]['sum'] = descripter.get_sum()
                data_attribute[str(i)]['min'] = descripter.get_minimum()
                data_attribute[str(i)]['max'] = descripter.get_maximum()
                data_attribute[str(i)]['range'] = descripter.get_range()
                data_attribute[str(i)]['has_duplicates'] = descripter.has_duplicates()
                data_attribute[str(i)]['is_sorted'] = descripter.is_sorted()
                data_attribute[str(i)]['cnt_distinct_values'] = descripter.count_distinct_values()
                data_attribute[str(i)]['contains_even_numbers'] = descripter.contains_even_numbers()
                data_attribute[str(i)]['contains_odd_numbers'] = descripter.contains_odd_numbers()
                data_attribute[str(i)]['contains_integers'] = descripter.contains_integers()
            
        return(data_attribute)

    # def _get_additional_attributes(td, index):
            
        # self.data[index] = 
