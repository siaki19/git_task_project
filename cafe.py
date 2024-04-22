# Creating my list menu. 
menu = ['coffee','tosty','desserts','tea']

# Creating the first dictionary. 
stock = {'coffee':20,
        'tosty':10,
        'desserts':50,
        'tea':25
        }

# Creating the second dictionary with the prices.
price = {'coffee':2,
        'tosty':4,
        'desserts':3,
         'tea':1
         }

# Creating a for loop , to find out the total stock worth in cafe.
total_stock = 0
for i in menu:
 total_stock += stock[i] * price[i]
print(total_stock)
        