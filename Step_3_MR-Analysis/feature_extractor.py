from additional_attributes_list.list_descripter import ListDescripter
import pandas as pd

class FeatureExtractor(object):
    def __init__(self, key: str, instance: dict):
        
        self.instance = instance
        self.key = key
        
    def new_dataset(self):
        
        td = self.instance['td']
        vs = self.instance['vs']
        vs_str = self.instance['vs_str']
        
        ld = ListDescripter(td)
        
        main_df = { 
                   'key_original_file' : self.key,
                #    'size': ld.get_length(),
                   'isEmpty': ld.isEmpty(),
                   'has_zeros': ld.has_zero(),
                #    'cnt_zeros': ld.cnt_zeros(),
                #    'cnt_positive_numbers': ld.cnt_positive_numbers(),
                #    'cnt_negative_numbers': ld.cnt_negative_numbers(),
                #    'get_minimum': ld.get_minimum(),
                #    'get_maximum': ld.get_maximum(),
                #    'get_sum':ld.get_sum(),
                #    'get_mean': ld.get_mean(),
                #    'get_median': ld.get_median(),
                #    'get_range': ld.get_range(),
                   'has_duplicates': ld.has_duplicates(),
                   'is_sorted': ld.is_sorted(),
                #    'count_distinct_values': ld.count_distinct_values(),
                   'contains_even_numbers': ld.contains_even_numbers(),
                   'contains_odd_numbers': ld.contains_odd_numbers(),
                   'contains_integers': ld.contains_integers(),
                   'contains_floats': ld.contains_floats(),
                #    'pp_numbers': ld.pp_numbers(),
                #    'pn_numbers': ld.pn_numbers(),
                   'more_positive_or_negative': ld.more_positive_or_negative(),
                   'weigth_of_list': ld.weigth_of_list(),
                   'vs': vs,
                   'vs_str': vs_str
        }
        
        return main_df

        
        
