"""
Inventory System Module
-----------------------
This module manages an inventory of items, allowing adding, removing,
checking low stock, and saving/loading data from a JSON file.
"""

import json
from datetime import datetime

# Global variable to hold inventory data
stock_data = {}


def add_item(item: str, qty: int = 0, logs=None):
    """
    Add a specified quantity of an item to the inventory.
    
    Args:
        item (str): The name of the item to add.
        qty (int): The quantity to add (can be negative to reduce stock).
        logs (list, optional): List to store operation logs.
    """
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        print(f"Invalid input for item '{item}' or quantity '{qty}'.")
        return

    if logs is None:
        logs = []

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: int):
    """
    Remove a quantity of an item from the inventory.
    
    Args:
        item (str): Item name to remove from.
        qty (int): Quantity to remove.
    """
    if not isinstance(qty, (int, float)):
        print(f"Invalid quantity: {qty}")
        return

    if item not in stock_data:
        print(f"Item '{item}' not found.")
        return

    stock_data[item] -= qty
    if stock_data[item] <= 0:
        del stock_data[item]


def get_qty(item: str) -> int:
    """
    Get the current quantity of an item.
    
    Args:
        item (str): Item name to check.
    
    Returns:
        int: Quantity available (0 if not found).
    """
    return stock_data.get(item, 0)


def load_data(file_path: str = "inventory.json"):
    """
    Load inventory data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file.
    """
    global stock_data
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print(f"Error reading '{file_path}'. File might be corrupted.")
        stock_data = {}


def save_data(file_path: str = "inventory.json"):
    """
    Save inventory data to a JSON file.
    
    Args:
        file_path (str): Path to the JSON file.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=2)


def print_data():
    """
    Print a summary report of all items in the inventory.
    """
    print("\n📦 Inventory Report 📦")
    if not stock_data:
        print("No items in inventory.")
        return
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5):
    """
    Check which items have quantities below a certain threshold.
    
    Args:
        threshold (int): Minimum acceptable quantity.
    
    Returns:
        list: Items below the threshold.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """
    Demonstrate inventory operations.
    """
    logs = []

    add_item("apple", 10, logs)
    add_item("banana", 2, logs)
    add_item("orange", 0, logs)

    remove_item("apple", 3)
    remove_item("grape", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low stock items: {check_low_items()}")

    save_data()
    load_data()
    print_data()

    # Replace eval with a safe demonstration
    print("Demo complete — no eval used for safety.")

    # Optional: print logs
    print("\nLogs:")
    for log in logs:
        print(log)


if __name__ == "__main__":
    main()
