import os
import csv

filePath = 'Store.csv'

def createCSV():
    if not os.path.exists(filePath):
        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'quantity'])
            print("***********************************\n")
    else:
        print(f"Found existing '{filePath}'.")

def addProducts(name, quantity):
    try:
        with open(filePath, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, quantity])
        print(f"Added '{name}' with quantity '{quantity}'.")
    except csv.Error as e:
        print(f"Error writing '{filePath}': {e}")

def readProducts():
    try:
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            print("\n========== Current Products ==========\n")
            for row in reader:
                print(f"{row['name']:20} {row['quantity']}")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found")
    except csv.Error as e:
        print(f"Error reading '{filePath}': {e}")

def updateProduct(name, newQuantity):
    try:
        rows = []
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] == name:
                    row['quantity'] = newQuantity
                rows.append(row)
        with open(filePath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'quantity'])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Updated quantity for '{name}' to '{newQuantity}'.")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found.")
    except csv.Error as e:
        print(f"Error writing '{filePath}': {e}")

def deleteProduct(name):
    try:
        rows = []
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] != name:
                    rows.append(row)
        with open(filePath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'quantity'])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Deleted product '{name}'.")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found.")
    except csv.Error as e:
        print(f"Error writing '{filePath}': {e}")

def main():
    createCSV()
    while True:
        print("\n===== Product Management Menu =====")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product Quantity")
        print("4. Delete Product")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            readProducts()
        elif choice == '2':
            name = input("Enter product name: ")
            quantity = input("Enter product quantity: ")
            addProducts(name, quantity)
        elif choice == '3':
            name = input("Enter product name to update: ")
            newQuantity = input("Enter new product quantity: ")
            updateProduct(name, newQuantity)
        elif choice == '4':
            name = input("Enter product name to delete: ")
            deleteProduct(name)
        elif choice == '5':
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Try Again.")

if __name__ == '__main__':
    main()
