# Takes numbers in an input list.
# Passes through each digit in those numbers, from least to most significant.
# Looks at the values of those digits.
# Buckets the input list according to those digits.
# Renders the results from that bucketing.
# Repeats this process until the list is sorted.

def radix_sort(list):
  max_value = max(list)
  max_exponent = len(str(max_value))
  being_sorted = list[:]

  for exponent in range(max_exponent):
    position = exponent + 1
    index = -position

    digits = [[] for i in range(10)]

    for number in being_sorted:
      number_as_a_string = str(number)
      try:
        digit = number_as_a_string[index]
      except IndexError:
        digit = 0
      digit = int(digit)

      digits[digit].append(number)

    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted


#Test 
list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183]
print(radix_sort(list)) #Prints [40, 89, 163, 183, 199, 355, 373, 535, 559, 621, 641, 689, 830, 921, 959, 961]
