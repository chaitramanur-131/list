products=["pen","book","scale","pencil"]
print("products:",products)
user_product=input("enter produt name:")
if user_product in products:
    print("product available")
else:
    print("product not available")
