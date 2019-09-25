# A company has determind that its annual profit is typically 23 percent of
# total sales. Write a pogram that ask the user to enter the projected amount
# of total sale, and then displays the profit that will be made from that
# amount.
# Hint: Use the value 0.23 to represent 23 percent.
# 24 SEP 2019
#CTI-110 P2T1 - Sales Prediction
#That Vo
#


# Get th eprojected total sales.
total_sales = float(input('Enter the projected sales: '))

# Calcuate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
