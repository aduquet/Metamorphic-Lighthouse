from mr_add_mt_process import MR_ADD
from mr_exc_mt_process import MR_EXC
from mr_inc_mt_process import MR_INC
from mr_inv_mt_process import MR_INV
from mr_mul_mt_process import MR_MUL
from mr_per_mt_process import MR_PER

class AdapterMRchecker():
    
    def __init__(self, inputs_outputs, const):
        self.inputs_outputs = inputs_outputs
        self.test_data_one_input = inputs_outputs['td']
        self.cons = const

    def _mr_per(self):
        # self.ttd_mr_per = MR_PER(self.test_data_one_input).followUpTD()
        return MR_PER(self.test_data_one_input).mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_per'])
        
    def _mr_add(self):
        # self.ttd_mr_add = MR_ADD(self.test_data_one_input, const).followUpTD()
        return MR_ADD(self.test_data_one_input, self.cons).mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_add'])

    def _mr_mul(self):
        # self.ttd_mr_mul = MR_MUL(self.test_data_one_input, const).followUpTD()
        return MR_MUL(self.test_data_one_input, self.cons).mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_mul'])

    def _mr_inv(self):
        # self.ttd_mr_inv = MR_INV(self.test_data_one_input).followUpTD()
        return MR_INV(self.test_data_one_input).mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_inv'])

    def _mr_inc(self):
        # self.ttd_mr_inc = MR_INC(self.test_data_one_input, const).followUpTD()
        return MR_INC(self.test_data_one_input, self.cons).mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_inc'])
         
    def _mr_exc(self):
        # self.ttd_mr_exc = MR_EXC(self.test_data_one_input).followUpTD()
        return MR_EXC(self.test_data_one_input).mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_exc'])
    
    def all_mrs_checker(self):
        self.inputs_outputs['vs_str_mr_per'] = self._mr_per()['vs_str']
        self.inputs_outputs['vs_str_mr_add'] = self._mr_add()['vs_str']
        self.inputs_outputs['vs_str_mr_mul'] = self._mr_mul()['vs_str']
        self.inputs_outputs['vs_str_mr_inv'] = self._mr_inv()['vs_str']
        self.inputs_outputs['vs_str_mr_inc'] = self._mr_inc()['vs_str']
        self.inputs_outputs['vs_str_mr_exc'] = self._mr_exc()['vs_str']

        self.inputs_outputs['vs_mr_per'] = self._mr_per()['vs']
        self.inputs_outputs['vs_mr_add'] = self._mr_add()['vs']
        self.inputs_outputs['vs_mr_mul'] = self._mr_mul()['vs']
        self.inputs_outputs['vs_mr_inv'] = self._mr_inv()['vs']
        self.inputs_outputs['vs_mr_inc'] = self._mr_inc()['vs']
        self.inputs_outputs['vs_mr_exc'] = self._mr_exc()['vs']
        
        return self.inputs_outputs