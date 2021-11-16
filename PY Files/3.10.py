# Put your code here
intPrice = float(input("Enter the puchase price: "))
intDownPayment = intPrice * .10
intMonth = 0
intRate = .12
intStartBal = intPrice - intDownPayment
intMonthPay = intStartBal * .05
intEndBal = intStartBal

print("%7s%18s%17s%18s%9s%16s" % \
      ("Month", "Starting Balance",
       "Interest to Pay", "Principal to Pay",
       "Payment", "Ending Balance"))

while intEndBal > 0:
    intMonth += 1

    if intEndBal > intMonthPay:
        intIntAmount = (intEndBal * intRate) / 12
        intPrinciple = intMonthPay - intIntAmount
        intPayment = intPrinciple + intIntAmount
        intEndBal -= intPrinciple
    else:
        intIntAmount = 0
        intPrinciple = intEndBal
        intPayment = intEndBal
        intEndBal -= intEndBal

    print("%7d%18.2f%17.2f%18.2f%9.2f%16.2f" % \
        (intMonth, intEndBal + intPrinciple, intIntAmount,
        intPrinciple, intPayment, intEndBal))
