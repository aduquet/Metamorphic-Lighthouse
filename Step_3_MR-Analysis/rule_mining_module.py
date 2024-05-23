from mlxtend.frequent_patterns import apriori, association_rules
from itertools import combinations
import pandas as pd

class RuleMiningModule(object):
    
    def __init__(self, data, support, conf):
        self.data = data
        self.support = support
        self.conf = conf

    def enconde(self):
        
        df = self.data.copy()
        df = df.drop(columns = ['key_original_file', 'vs', 'contains_floats', 'contains_integers', 'contains_even_numbers', 'contains_odd_numbers'])

        for col in df.columns:
            df[col] = df[col].astype(str)

        # Apply one-hot encoding to convert categorical data to binary format
        df_encoded = pd.get_dummies(df)
        # df_encoded = df_encoded.drop(columns = ['isEmpty_False', 'has_zeros_False', 'has_duplicates_False', 'is_sorted_False',
        #                                         'contains_even_numbers_False', 'contains_odd_numbers_False'])

        # column_name_mapping = { 'isEmpty_True': 'isEmpty',
        #                         'has_zeros_True': 'has_zeros',
        #                         'has_duplicates_True': 'has_duplicates',
        #                         'is_sorted_True': 'is_sorted',
        #                         'contains_even_numbers_True': 'contains_even_numbers',
        #                         'contains_odd_numbers_True': 'contains_odd_numbers',
        #                     }
        
        df_encoded = df_encoded.drop(columns = ['isEmpty_False', 'has_zeros_False', 'has_duplicates_False', 'is_sorted_False',
                                                 ])

        column_name_mapping = { 'isEmpty_True': 'isEmpty',
                                'has_zeros_True': 'has_zeros',
                                'has_duplicates_True': 'has_duplicates',
                                'is_sorted_True': 'is_sorted',
                               
                            }        
        # return df_encodexd.rename(columns=column_name_mapping)
        return df_encoded
    
    
    def ruleGenerator_v(self, df_encode, path_store):

        k = df_encode.keys()
        if 'vs_str_No-violate' in k:
            df_encode = df_encode.drop(columns = ['vs_str_No-violate'])
            
        # print(df_encode)
            
        # df_encode.to_csv( path_store + '_encode_v.csv', index=False)

        # Apply the Apriori algorithm to find frequent itemsets
        frequent_itemsets = apriori(df_encode, min_support=0.1, use_colnames=True)

        # Generate association rules
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)

        # Filter rules where 'vs_str_Violate' is the only item in the consequents
        violated_rules = rules[
            (rules['consequents'].astype(str).str.contains("'vs_str_Violate'")) & 
            (rules['consequents'].apply(lambda x: len(x) == 1))]       
        # Filter rules with lift greater than 1
        relevant_rules = violated_rules[violated_rules['lift'] > 0.01]

        relevant_rules['antecedents'] = relevant_rules['antecedents'].apply(lambda x: list(x))
        relevant_rules['consequents'] = relevant_rules['consequents'].apply(lambda x: list(x))
        
        rs = relevant_rules.sort_values(by='antecedent support', ascending=False)
        rs.to_csv( path_store + '_v.csv', index=False)

        contradictory_antecedents = [
            ['weigth_of_list_wn', 'has_zeros_False'],
            ['weigth_of_list_wn', 'has_zeros_True'],
            ['weigth_of_list_wn', 'has_duplicates_False'],
            ['weigth_of_list_wn', 'has_duplicates_True'],
            ['weigth_of_list_wn', 'is_sorted_False'],
            ['weigth_of_list_wn', 'is_sorted_True'],
            ['weigth_of_list_wn', 'contains_even_numbers_True'],
            ['weigth_of_list_wn', 'contains_even_numbers_False'],
            ['weigth_of_list_wn', 'contains_odd_numbers_False'],
            ['weigth_of_list_wn', 'contains_odd_numbers_True'],
            ['weigth_of_list_wn', 'more_positive_or_negative_e'],
            ['weigth_of_list_wn', 'more_positive_or_negative_n'],
            # Add more contradictory antecedents as needed
        ]
        filter_rules = relevant_rules[~relevant_rules['antecedents'].apply(lambda x: any(set(contradiction).issubset(x) for contradiction in contradictory_antecedents))]

        filter_rules.to_csv( path_store + '_filtered_v.csv', index=False)

    def ruleGenerator_nv(self, df_encode, path_store):
        
        k = df_encode.keys()
        if 'vs_str_Violate' in k:
            df_encode = df_encode.drop(columns = ['vs_str_Violate'])
        
        if 'vs_str_error' in k:
            df_encode = df_encode.drop(columns = ['vs_str_error'])
        
        # df_encode.to_csv( path_store + '_encode_nv.csv', index=False)

        # Apply the Apriori algorithm to find frequent itemsets
        frequent_itemsets = apriori(df_encode, min_support=0.1, use_colnames=True)
        
        # Generate association rules
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
        # Filter rules where 'vs_str_Violate' is the only item in the consequents
        violated_rules = rules[
            (rules['consequents'].astype(str).str.contains("'vs_str_No-violate'")) & 
            (rules['consequents'].apply(lambda x: len(x) == 1))]       
        
        # Filter rules with lift greater than 1
        relevant_rules = violated_rules[violated_rules['lift'] > 1]

        relevant_rules['antecedents'] = relevant_rules['antecedents'].apply(lambda x: list(x))
        relevant_rules['consequents'] = relevant_rules['consequents'].apply(lambda x: list(x))
            
        rs = relevant_rules.sort_values(by='antecedent support', ascending=False)
        rs.to_csv( path_store + '_nv.csv', index=False)
        
        if len(rs) == 0:
            rules.to_csv( path_store + '_nv.csv', index=False)
            
            
        contradictory_antecedents = [
            ['weigth_of_list_wn', 'has_zeros_False'],
            ['weigth_of_list_wn', 'has_zeros_True'],
            ['weigth_of_list_wn', 'has_duplicates_False'],
            ['weigth_of_list_wn', 'has_duplicates_True'],
            ['weigth_of_list_wn', 'is_sorted_False'],
            ['weigth_of_list_wn', 'is_sorted_True'],
            ['weigth_of_list_wn', 'contains_even_numbers_True'],
            ['weigth_of_list_wn', 'contains_even_numbers_False'],
            ['weigth_of_list_wn', 'contains_odd_numbers_False'],
            ['weigth_of_list_wn', 'contains_odd_numbers_True'],
            ['weigth_of_list_wn', 'more_positive_or_negative_e'],
            ['weigth_of_list_wn', 'more_positive_or_negative_n'],
            # Add more contradictory antecedents as needed
        ]
        filter_rules = relevant_rules[~relevant_rules['antecedents'].apply(lambda x: any(set(contradiction).issubset(x) for contradiction in contradictory_antecedents))]

        filter_rules.to_csv( path_store + '_filtered_nv.csv', index=False)

    def ruleGenerator_e(self, df_encode, path_store):
    
        k = df_encode.keys()
        if 'vs_str_No-violate' in k:
            df_encode = df_encode.drop(columns = ['vs_str_No-violate'])
        
        if 'vs_str_Violate' in k:
            df_encode = df_encode.drop(columns = ['vs_str_Violate'])
        
        df_encode = df_encode[df_encode['vs_str_error'] != False]
        df_encode.to_csv( path_store + '_encode.csv', index=False)

        # Apply the Apriori algorithm to find frequent itemsets
        frequent_itemsets = apriori(df_encode, min_support=0.1, use_colnames=True)
        # Generate association rules
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

        # Filter rules where 'vs_str_Violate' is the only item in the consequents
        violated_rules = rules[
            (rules['consequents'].astype(str).str.contains("'vs_str_error'")) & 
            (rules['consequents'].apply(lambda x: len(x) == 1))]       
        # Filter rules with lift greater than 1
        relevant_rules = violated_rules[violated_rules['lift'] > 1]

        relevant_rules['antecedents'] = relevant_rules['antecedents'].apply(lambda x: list(x))
        relevant_rules['consequents'] = relevant_rules['consequents'].apply(lambda x: list(x))
            
        rs = rules.sort_values(by='antecedent support', ascending=False)
        # rss = rs[rs['consequents'] != '(vs_str_error)']
        # rss = rss[rss['antecedents'] != '(vs_str_error)']
        
        rs_filtered = rs[rs['antecedents'].apply(lambda x: 'vs_str_error' in x) | rs['consequents'].apply(lambda x: 'vs_str_error' in x)]
        rs_filtered.to_csv( path_store + '_e.csv', index=False)

        contradictory_antecedents = [
            ['weigth_of_list_wn', 'has_zeros_False'],
            ['weigth_of_list_wn', 'has_zeros_True'],
            ['weigth_of_list_wn', 'has_duplicates_False'],
            ['weigth_of_list_wn', 'has_duplicates_True'],
            ['weigth_of_list_wn', 'is_sorted_False'],
            ['weigth_of_list_wn', 'is_sorted_True'],
            ['weigth_of_list_wn', 'contains_even_numbers_True'],
            ['weigth_of_list_wn', 'contains_even_numbers_False'],
            ['weigth_of_list_wn', 'contains_odd_numbers_False'],
            ['weigth_of_list_wn', 'contains_odd_numbers_True'],
            ['weigth_of_list_wn', 'more_positive_or_negative_e'],
            ['weigth_of_list_wn', 'more_positive_or_negative_n'],
                # Add more contradictory antecedents as needed
        ]
        filter_rules = relevant_rules[~relevant_rules['antecedents'].apply(lambda x: any(set(contradiction).issubset(x) for contradiction in contradictory_antecedents))]
        filter_rules.to_csv( path_store + '_filtered_e.csv', index=False)
            

    def generate_or_rules(seld, rules):
        new_rules = []
        for _, rule in rules.iterrows():
            antecedents = rule['antecedents']
            if 'vs_str_Violate' in rule['consequents']:
                consequents = ['vs_str_Violate']
                for antecedent_comb in combinations(antecedents, 2):
                    new_rule = tuple(antecedent_comb) + tuple(consequents)
                    new_rules.append({'antecedents': set(antecedent_comb), 'consequents': consequents})
        return pd.DataFrame(new_rules)

        # Generate rules with 'or' conditions

        # df_encode = pd.get_dummies(df_encode)
        # print(df_encode)
        # itemSets, rules = apriori(df_encode, min_support=self.support)
        # rules = association_rules(itemSets, metric="confidence", min_threshold=0.7)
        # # Filter rules where 'vs_str' is violated
        # violated_rules = rules[rules['consequents'].astype(str).str.contains("'vs_str_Violate'")]
        # print(violated_rules)
        # return itemSets, rules