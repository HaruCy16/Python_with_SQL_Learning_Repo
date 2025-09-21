#PROGRAM FOR CREATING A GROCERY MARKET
"""
  PROGRAM FEATURES
  1. Add money balance
  2. Add to cart
  3. Purchase product
  4. Remove to card
"""


"""
  CLASSES, CONSTANTS, 
"""
#ITEM ARRAYS FOODS
itemFruits = ["Apple", "Banana", "Orange", "Grapes", "Mango", "Dragon fruit"]
itemVegetables = ["Carrot", "Broccoli", "Spinach", "Potato", "Tomato", "Cucumber"]
itemDairy = ["Milk", "Cheese", "Yogurt", "Butter", "Cream", "Ice Cream"]
itemBakery = ["Bread", "Bagel", "Muffin", "Croissant", "Cake", "Pie"]
itemMeat = ["Chicken", "Beef", "Pork", "Lamb", "Turkey", "Fish"]
itemBeverages = ["Water", "Soda", "Juice", "Tea", "Coffee", "Smoothie"]

#ITEMS PRICES
fruitsPrices = [10, 20, 20, 30, 50, 100]
vegetablesPrices = [15, 25, 30, 20, 10, 15]
dairyPrices = [40, 60, 50, 70, 80, 90]
bakeryPrices = [25, 30, 35, 40, 45, 50]
meatPrices = [100, 200, 150, 250, 300, 350]
beveragesPrices = [10, 20, 30, 15, 25, 35]

#ADD CART CLASS AND METHOD
class Add_Cart:
  def add_cart(self, item, selectedPrices):
    self.item = item
    self.selectedPrices = selectedPrices
    # cart.append(self.item)
    cart_items_add().cart.append(self.item)
    print(f"{self.item} has been added to your cart for ${self.selectedPrices}.")

#REMOVE CART CLASS AND METHOD
class Remove_Cart:
  def remove_cart(self, item):
    self.item = item
    if self.item in cart_items_add().cart:
      cart_items_add().cart.remove(self.item)
      print(f"{self.item} has been removed from your cart.")
    else:
      print(f"{self.item} is not in your cart.")

#POLYMORPHISM FUNCTION TO DISPLAY ITEMS
class Fruits_Display:
  def show_items(self):
    for i in range (len(itemFruits)):
      print(f"{i + 1}. {itemFruits[i]} - ${fruitsPrices[i]}")

class Vegetables_Display:
  def show_items(self):
    for i in range (len(itemVegetables)):
      print(f"{i + 1}. {itemVegetables[i]} - ${vegetablesPrices[i]}")

class Dairy_Display:
  def show_items(self):
    for i in range (len(itemDairy)):
      print(f"{i + 1}. {itemDairy[i]} - ${dairyPrices[i]}")

class Bakery_Display:
  def show_items(self):
    for i in range (len(itemBakery)):
      print(f"{i + 1}. {itemBakery[i]} - ${bakeryPrices[i]}")

class Meat_Display:
  def show_items(self):
    for i in range (len(itemMeat)):
      print(f"{i + 1}. {itemMeat[i]} - ${meatPrices[i]}")

class Beverages_Display:
  def show_items(self):
    for i in range (len(itemBeverages)):
      print(f"{i + 1}. {itemBeverages[i]} - ${beveragesPrices[i]}")

#INITIALIZATION OF ITEM FUNCTION TO THEIR DISTINCT CATEGORY
fruits = Fruits_Display()
vegetables = Vegetables_Display()
dairy = Dairy_Display()
bakery = Bakery_Display()
meat = Meat_Display()
beverages = Beverages_Display()

"""
  START OF THE PROGRAM
"""
#STARTING WINDOW
print("Welcome to Cy Grocery Store\n")
print("Please enter your balance: ")
balanceMoney = (int(input()))

#DISPLAY ITEMS AND PRICES
print("\nAvailable Products:")
print("\nFruits:")
(fruits.show_items())

print("\nVegetables:")
(vegetables.show_items())

print("\nDairy:")
(dairy.show_items())

print("\nBakery:")
(bakery.show_items())

print("\nMeat:")
(meat.show_items())

print("\nBeverages:")
(beverages.show_items())

print("|--------------------------------------------------|")

"""
  PROGRAM FUNCTIONS CONNECTED TO CLASS METHODS
"""
#CART ADD FUNCTION TO DISPLAY ITEMS BASED ON USER CHOICE
def cart_items_add():
  cart = []

  #USER CHOICE
  menuChoice = 0;
  
  #ENTER WHAT TYPE OF ITEM WANT TO BUY
  print("\nWhat type of item do you want to add to your cart or exit to main menu?")
  print("1. Fruits")
  print("2. Vegetables")
  print("3. Dairy")
  print("4. Bakery")
  print("5. Meat")
  print("6. Beverages")
  print("7. Exit to main menu")
  print("You have a balance of: $" + str(balanceMoney))
  print("Please enter the number of your choice (1 - 6): ")
  #ASK USER FOR TYPE(INPUT NUMBERS 1 - 6)
  menuChoice = int(input())

  #DISPLAY ITEMS BASED ON USER CHOICE BY USING POLYMORPHISM STORED IN SELECTED ITEMS VARIABLE

  # Choose the correct array based on menuChoice
  selectedItems = []
  selectedPrices = []

  match menuChoice:
      case 1:
          selectedItems = itemFruits
          selectedPrices = fruitsPrices
          fruits.show_items()
      case 2:
          selectedItems = itemVegetables
          selectedPrices = vegetablesPrices
          vegetables.show_items()
      case 3:
          selectedItems = itemDairy
          selectedPrices = dairyPrices
          dairy.show_items()
      case 4:
          selectedItems = itemBakery
          selectedPrices = bakeryPrices
          bakery.show_items()
      case 5:
          selectedItems = itemMeat
          selectedPrices = meatPrices
          meat.show_items()
      case 6:
          selectedItems = itemBeverages
          selectedPrices = beveragesPrices
          beverages.show_items()
      case 7:
          print("Exiting to main menu.\n")
          return
      case _:
          print("Invalid choice. Please select a number between 1 and 6.")
  addCart = Add_Cart()
  
  # ASK USER FOR ITEM TO ADD TO CART THROUGH LOOP
  print("\nPlease enter the name of the item you want to add to your cart: ")
  itemToAdd = input()

  # Check if the item exists in the selectedItems list (case insensitive)
  found = False
  for i in range(len(cart_items_add().selectedItems)):
      if cart_items_add().itemToAdd.lower() == cart_items_add().selectedItems[i].lower():  # ignore case
          cart_items_add().addCart.add_cart(cart_items_add().selectedItems[i], cart_items_add().selectedPrices[i])
          found = True
      print("Item added successfully.")
      break

  if not found:
      print("Invalid item. Please enter a correct product name.")

#CART REMOVE FUNCTION TO DELETE ITEMS FROM CART
def cart_items_remove():
  removeCart = Remove_Cart()
  return removeCart

#VIRTUAL CART VIEW FUNCTION
def cart_items_view():
  if not cart_items_add().cart:
    print("Your cart is empty.")
  else:
    for item in cart_items_add().cart:
      print(f"- {item}")

#MAIN MENU IN LOOPS
while True:
  print("\nMain Menu:")
  print("1. Add to cart")
  print("2. Remove from cart")
  print("3. View cart")
  print("4. Checkout")
  print("5. Exit")
  print("Please enter the number of your choice (1 - 5): ")
  mainChoice = int(input())

  if mainChoice == 1:
    cart_items_add()
  elif mainChoice == 2:
    print("\nPlease enter the name of the item you want to remove from your cart: ")
    itemToRemove = input()
    cart_items_remove().remove_cart(itemToRemove)
  elif mainChoice == 3:
    cart_items_view()
  elif mainChoice == 4:
    totalCost = 0
    for item in cart_items_add().cart:
      # Find the price of each item
      if item in itemFruits:
        index = itemFruits.index(item)
        totalCost += fruitsPrices[index]
      elif item in itemVegetables:
        index = itemVegetables.index(item)
        totalCost += vegetablesPrices[index]
      elif item in itemDairy:
        index = itemDairy.index(item)
        totalCost += dairyPrices[index]
      elif item in itemBakery:
        index = itemBakery.index(item)
        totalCost += bakeryPrices[index]
      elif item in itemMeat:
        index = itemMeat.index(item)
        totalCost += meatPrices[index]
      elif item in itemBeverages:
        index = itemBeverages.index(item)
        totalCost += beveragesPrices[index]

    print(f"\nTotal cost: ${totalCost}")
    if totalCost > balanceMoney:
      print("Insufficient balance. Please remove some items from your cart.")
    else:
      balanceMoney -= totalCost
      cart_items_add().cart.clear()
      print(f"Purchase successful! Remaining balance: ${balanceMoney}")
  elif mainChoice == 5:
    print("Thank you for shopping with us!")
    break
  else:
    print("Invalid choice. Please select a number between 1 and 5.")