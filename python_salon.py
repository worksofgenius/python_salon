hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

# Loop through prices list and add each to total_price
for price in prices:
  total_price += price

average_price = total_price/len(prices)

# Print average price
print('Average Haircut Price: ' + str(average_price))

# Reduce prices by 5
new_prices = [price - 5 for price in prices]
print('New Prices: ' + str(new_prices))

# Calculate last week's revenue
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print('Total Revenue: ' + str(total_revenue))

# Calculate average daily revenue
average_daily_revenue = total_revenue/7
print('Average Daily Revenue: ' + str(average_daily_revenue))

# Feature cuts < 30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] - 1]
print('Cuts Under 30: ' + str(cuts_under_30))
