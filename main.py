#Pseudocode
  #price of house is $1M
  # if a person has good credit,
    # they need to put down by 10%
  # Otherwise
    # they need to put down by 20%
  # print down payment

price_of_house = 1000000
does_buyer_has_good_credit = True

if does_buyer_has_good_credit:
    down_payment = 0.1 * price_of_house
else:
    down_payment = 0.2 * price_of_house

print(f"Down Payment: ${down_payment}")