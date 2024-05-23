import numpy as np

class ListDescripter():

    def __init__(self, data_list: list):
        self.data_list = data_list

    def get_length(self):
        return len(self.data_list)

    def isEmpty(self):
        if len(self.data_list) != 0:
            return False
        else:
            return True
    
    def has_zero(self):
        
        if len(self.data_list) != 0:
            return 0 in self.data_list
        else:
            return 'NA'
    
    def cnt_zeros(self):
        
        if len(self.data_list) != 0:
            return sum(1 for num in self.data_list if num == 0)
        else:
            return 'NA'
        
    def cnt_positive_numbers(self):
        
        if len(self.data_list) != 0:    
            return sum(1 for num in self.data_list if num > 0)
        else:
            return 'NA'
    def cnt_negative_numbers(self):
        
        if len(self.data_list) != 0:
            return sum(1 for num in self.data_list if num < 0)
        else:
            return 'NA'
    
    def more_positive_or_negative(self):
        
        if len(self.data_list) != 0:
            positive_count = sum(1 for x in self.data_list if x > 0)
            negative_count = sum(1 for x in self.data_list if x < 0)
            
            if positive_count > negative_count:
                return "p"
            elif positive_count < negative_count:
                return "n"
            else:
                return "e"
        else:
            return 'NA'    
        
    def get_minimum(self):
        
        if len(self.data_list) != 0:
            return min(self.data_list)
        else:
            return 'NA'
        
    def get_maximum(self):
        
        if len(self.data_list) != 0:
            return max(self.data_list)
        else:
            return 'NA'
        
    def get_sum(self):
        
        if len(self.data_list) != 0:
            return sum(self.data_list)
        else:
            return 'NA'
        
    def get_mean(self):
        
        if len(self.data_list) != 0:
            return np.mean(self.data_list)
        else:
            return 'NA'
        
    def get_median(self):
        
        if len(self.data_list) != 0:
            return np.median(self.data_list)
        else:
            return 'NA'
        
    def get_range(self):
        
        if len(self.data_list) != 0:
            return max(self.data_list) - min(self.data_list)
        else:
            return 'NA'
        
    def has_duplicates(self):
        
        if len(self.data_list) != 0:
            return len(self.data_list) != len(set(self.data_list))
        else:
            return 'NA'
        
    def is_sorted(self):
        if len(self.data_list) != 0:
        
            return self.data_list == sorted(self.data_list)
        else:
            return 'NA'
        
    def count_distinct_values(self):
        
        if len(self.data_list) != 0:
            return len(set(self.data_list))
        else:
            return 'NA'
        
    def contains_even_numbers(self):
        
        if len(self.data_list) != 0:
            return any(num % 2 == 0 for num in self.data_list)
        else:
            return 'NA'
        
    def contains_odd_numbers(self):
        
        if len(self.data_list) != 0:
            return any(num % 2 != 0 for num in self.data_list)
        else:
            return 'NA'
        
    def contains_integers(self):
        
        if len(self.data_list) != 0:
            return all(isinstance(num, int) for num in self.data_list)
        else:
            return 'NA'

    def contains_floats(self):
        
        if len(self.data_list) != 0:
            return all(isinstance(num, float) for num in self.data_list)
        else:
            return 'NA'
                    
    def pp_numbers(self): # Percentage of positive numbers among all numbers
        if len(self.data_list) != 0:
        
            return sum(num for num in self.data_list if num > 0) / len(self.data_list)
        else:
            return 'NA'
        
    def pn_numbers(self): # Percentage of negative number among all number
        
        if len(self.data_list) != 0:
            return sum(num for num in self.data_list if num < 0) / len(self.data_list)
        else:
            return 'NA'
    
    def weigth_of_list(self):
        
        positive_sum = sum(x for x in self.data_list if x > 0)
        negative_sum = abs(sum(x for x in self.data_list if x < 0))  # Taking absolute value for negative sum
        
        if positive_sum > negative_sum:
            return "wp"
        elif positive_sum < negative_sum:
            return "wn"
        else:
            return "we"       
        
