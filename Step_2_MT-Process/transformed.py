from test_data_transformer import InputTransformed 
from mr_add_mt_process import MR_ADD
from mr_mul_mt_process import MR_MUL
import numpy as np

a = InputTransformed([]).mrADD(9)
print(a)

b = InputTransformed([1,2,3,4]).mrPER()
print(b)

b = InputTransformed([]).mrPER()
print(b)

b = InputTransformed([12,4,5,6]).mrINC(900)
print(b)

b = InputTransformed([12,4,5,6]).mrEXC()
print(b)

prueba = MR_ADD(test_data_one_input=[-5,2,-3,-5], cons=2).followUpTD()
pruebamul = MR_MUL(test_data_one_input=[-5,2,-3,-5], cons=2).followUpTD()
vsn_add = MR_ADD([-5,2,-3,-5], cons = 2).mrChecker(outputTD=np.sum([-5,2,-3,-5]), outputTTD=np.sum(prueba))
vsn_mul = MR_MUL([-5,2,-3,-5], cons = 2).mrChecker(outputTD=np.sum([-5,2,-3,-5]), outputTTD=np.sum(pruebamul))

print(np.sum([-5,2,3,-5]))
print(vsn_add)
print(vsn_mul)

