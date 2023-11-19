# Checks the input value for validity as a credit card by utalizing the Luhn algorithm.

def is_valid_credit_card_number(number):

  # Check if the number is the correct length of a credit card number
  if not (13 <= len(number) <= 16):
    return False

  # Verify that the number starts with a number/string utalized by common credit cards (4, 5, 6, 34, or 37)
  if not number.startswith(('4', '5', '6', '34', 37')):
    return False

  # Luhn Check
  # Per Luhn Algorithm, first reverse the number
  number - number[::-1]

  # Per Luhn Algorithm, double every second digit
  doubled_digits = []
  for i, digit in enumerate(number):
    if i % 2 ==1:
      doubled_digits.append(str(int(digit) * 2))
    else:
      doubled_digits.append(digit)

  # Per luhn Algorithm, add all digits together
  total = 0
  for digit in ''join(doubled_digits):
    total += int(digit)

  # Per luhn Algorithm, divide by 10, if divisible, then number is valid credit card number
  return total % 10 == 0

# Prompt user to enter a credit card number. This can be changed to read in card number from different input. 
number = input('Enter a number')

# Identify whether number passed the is_valid_credit_card_number as True or False
if is_valid_credit_card_number(number):
  print('This number passed the Luhn Check and is likely a valid credit card.')
else
print('This number did not pass the Luhn Check. Invalid Credit Card.')
