from time_calculator import add_time
from unittest import main

#print expected: 1:08 AM (next day)
print(add_time("11:06 PM", "2:02"))

#print expected: 17:21 PM, Wednesday (2 days later)
print(add_time("09:40 PM,", "55:41", "Monday"))

# Run unit tests automatically
main(module='test_module', exit=False)