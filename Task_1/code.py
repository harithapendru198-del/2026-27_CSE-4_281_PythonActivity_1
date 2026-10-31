

products = []

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    products.append([name, price, quantity])

budget = float(input("\nEnter your budget: "))

total = 0

for p in products:
    total += p[1] * p[2]

print("\nOriginal Total:", total)

if total >= 5000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("Discount:", discount)
print("Amount after discount:", final_amount)

if final_amount > budget:

    print("\nBudget exceeded!")
    print("Reducing product quantities...")

    while final_amount > budget:

        reduced = False

        for p in products:
            if p[2] > 0:
                p[2] -= 1
                reduced = True

                total = sum(x[1] * x[2] for x in products)

                if total >= 5000:
                    discount = total * 0.10
                else:
                    discount = 0

                final_amount = total - discount

                if final_amount <= budget:
                    break

        if not reduced:
            break

print("\nFinal Shopping Basket")

for p in products:
    print(p[0], "Quantity:", p[2])

print("Final Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)
print("Remaining Budget:", budget - final_amount)

