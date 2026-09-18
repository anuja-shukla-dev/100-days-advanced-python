import sys

numbers_list = [x for x in range(1000000)]

numbers_generator = (x for x in range(1000000))

print(sys.getsizeof(numbers_list))
print(sys.getsizeof(numbers_generator))

# 1. Which one occupies more memory?
# List occupies more memory as it stores all 1000000 in one go.

# 2. Why does the generator occupy much less memory?
# Generator will occupy much less memory because it gives value on the fly rather than storing it beforehand.

# 3. Does the generator store all 1,000,000 numbers at once?
# No, generator will not store all 1,000,000 numbers at once. It will generate numbers on the fly.