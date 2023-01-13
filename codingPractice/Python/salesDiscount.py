print('Variables & Datatypes - Exercise')
#Create appropriate Variables for Item name, the price 
#and how many you have in stock

item = 'hammer'
in_stock = 6
price = 17.99
discount_as_percent = 50
#discount_as_percent = int(input("What percent discount is your *Lucky Rabbit* coupon code?"))
discounted_price = round(price*((100-discount_as_percent)/100),2)
print(f"This {item} costs ${price}. There are {in_stock} left in stock.")
print(f"BUT -  buy now and save {str(discount_as_percent)}% during this sale! \nYES! That means you can get this {item} for ${discounted_price:.2f} ")