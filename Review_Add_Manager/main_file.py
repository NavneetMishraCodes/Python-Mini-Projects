# getting the name of product, order_id and stars rating out of 5
prod_name = input("Enter the name of the product: ")
order_id = input("Enter the order Id: ")
star_rating = input("Enter the number stars you give to this product out of 5: ")

# taking review of the product
review = input("Enter the review for the product: ")

# storing the review
with open(f"D:\\Python_Programming\\Projects_Py\\Review_Add_Manager\\Products_Reviews\\{prod_name}_Reviews.txt", 'a') as f:
    f.write(f"OrderID: {order_id}\n")
    f.write(f"Stars Rating: {star_rating}/5\n")
    f.write(f"Review: {review}\n")
    f.write("\n")