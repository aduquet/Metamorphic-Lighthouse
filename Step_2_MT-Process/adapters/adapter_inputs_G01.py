from mr_add_mt_process import MR_ADD
from mr_exc_mt_process import MR_EXC
from mr_inc_mt_process import MR_INC
from mr_inv_mt_process import MR_INV
from mr_mul_mt_process import MR_MUL
from mr_per_mt_process import MR_PER

class AdapterInputs():
    
    ttd_mr_per = None
    ttd_mr_add = None
    ttd_mr_mul = None
    ttd_mr_inv = None
    ttd_mr_inc = None
    ttd_mr_exc = None
    
    def __init__(self, test_data_one_input):
        self.test_data_one_input = test_data_one_input

    def _mr_per(self):
        # self.ttd_mr_per = MR_PER(self.test_data_one_input).followUpTD()
        return MR_PER(self.test_data_one_input).followUpTD()
        
    def _mr_add(self, const):
        # self.ttd_mr_add = MR_ADD(self.test_data_one_input, const).followUpTD()
        return MR_ADD(self.test_data_one_input, const).followUpTD()

    def _mr_mul(self, const):
        # self.ttd_mr_mul = MR_MUL(self.test_data_one_input, const).followUpTD()
        return MR_MUL(self.test_data_one_input, const).followUpTD()

    def _mr_inv(self):
        # self.ttd_mr_inv = MR_INV(self.test_data_one_input).followUpTD()
        return MR_INV(self.test_data_one_input).followUpTD()

    def _mr_inc(self, const):
        # self.ttd_mr_inc = MR_INC(self.test_data_one_input, const).followUpTD()
        return MR_INC(self.test_data_one_input, const).followUpTD()
         
    def _mr_exc(self):
        # self.ttd_mr_exc = MR_EXC(self.test_data_one_input).followUpTD()
        return MR_EXC(self.test_data_one_input).followUpTD()
        
    def ttd_all_mrs(self, const):
        
        return {
            'td' : self.test_data_one_input,
            'ttd_mr_per': self._mr_per(),
            'ttd_mr_add': self._mr_add(const=const),
            'ttd_mr_mul': self._mr_mul(const=const),
            'ttd_mr_inv': self._mr_inv(),
            'ttd_mr_inc': self._mr_inc(const=const),
            'ttd_mr_exc': self._mr_exc(),
        }