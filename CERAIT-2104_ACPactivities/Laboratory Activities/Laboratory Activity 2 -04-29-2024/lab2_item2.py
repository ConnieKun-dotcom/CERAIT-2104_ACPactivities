while True:
  purchase_amount = float(input("Enter the total purchase amount: "))
  initial_purchase_amount = purchase_amount
  discount = purchase_amount * 0.05
  final_price = purchase_amount - discount

  print(f"Initial Purchase Amount: {initial_purchase_amount:.2f}")
  print(f"Discount: {discount:.2f}")
  print(f"Final Price: {final_price:.2f}")

  again = input("Do you want to try again? (yes/no): ")
  if again.lower() != "yes":
    print("Thank you!")
    break