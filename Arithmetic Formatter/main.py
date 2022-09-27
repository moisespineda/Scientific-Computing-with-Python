from arithmetic_arranger import arithmetic_arranger
from unittest import main
#testing with out the result
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

#testing with result
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

#test module
main(module='test_module', exit=False)