"""
ASSIGNMENT 13B: SPRINT 6 - OBJECT ARCHITECTURE
Project: Precision PC Builder System
Developer: Predrag Komljenovic
"""

import datetime
import os
from pc_build import PCBuild

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARTS_FILE = os.path.join(BASE_DIR, "parts.txt")
BUILD_HISTORY_FILE = os.path.join(BASE_DIR, "build_history.txt")

builds = []


def get_customer_info():
    name = input("Enter Customer Name: ").strip()
    purpose = input("Build Purpose (Gaming / Office / Streaming): ").strip()
    return name, purpose


def select_components():
    print("\nSelect PC Components")

    cpu = input("CPU: ").strip()
    gpu = input("GPU: ").strip()
    ram = input("RAM: ").strip()
    storage = input("Storage: ").strip()
    case = input("Case: ").strip()

    return cpu, gpu, ram, storage, case


def calculate_total(build):
    """Calculate total cost using parts.txt"""
    total = 0.0

    try:
        with open(PARTS_FILE, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue

                category, part, price = line.strip().split(",")
                part = part.strip()
                price = float(price.strip())

                if build.get_cpu().strip().lower() == part.lower():
                    total += price
                if build.get_gpu().strip().lower() == part.lower():
                    total += price
                if build.get_ram().strip().lower() == part.lower():
                    total += price
                if build.get_storage().strip().lower() == part.lower():
                    total += price
                if build.get_case().strip().lower() == part.lower():
                    total += price

    except FileNotFoundError:
        print("Error: parts.txt file not found at:", PARTS_FILE)

    build.set_total(total)


def review_build(build):
    build.display_order()
    decision = input("\n(C) Confirm Build | (E) Edit Build: ").strip().upper()
    return decision


def save_build(build):
    try:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(BUILD_HISTORY_FILE, "a") as file:
            file.write(f"\n[{current_time}]\n")
            file.write("-----------------------------\n")
            file.write(f"Customer: {build.get_customer()}\n")
            file.write(f"Purpose: {build.get_purpose()}\n")
            file.write(f"CPU: {build.get_cpu()}\n")
            file.write(f"GPU: {build.get_gpu()}\n")
            file.write(f"RAM: {build.get_ram()}\n")
            file.write(f"Storage: {build.get_storage()}\n")
            file.write(f"Case: {build.get_case()}\n")
            file.write(f"Total: ${build.get_total():.2f}\n")

    except Exception as e:
        print("Error saving build:", e)


def edit_build(build):
    print("\nWhich part would you like to edit?")
    print("1. Customer")
    print("2. Purpose")
    print("3. CPU")
    print("4. GPU")
    print("5. RAM")
    print("6. Storage")
    print("7. Case")

    choice = input("Enter number: ").strip()

    if choice == "1":
        build.set_customer(input("Enter new customer name: ").strip())
    elif choice == "2":
        build.set_purpose(input("Enter new purpose: ").strip())
    elif choice == "3":
        build.set_cpu(input("Enter new CPU: ").strip())
    elif choice == "4":
        build.set_gpu(input("Enter new GPU: ").strip())
    elif choice == "5":
        build.set_ram(input("Enter new RAM: ").strip())
    elif choice == "6":
        build.set_storage(input("Enter new Storage: ").strip())
    elif choice == "7":
        build.set_case(input("Enter new Case: ").strip())
    else:
        print("Invalid choice.")

    calculate_total(build)


def main():
    print("PRECISION PC BUILDER SYSTEM v2.0\n")

    name, purpose = get_customer_info()
    cpu, gpu, ram, storage, case = select_components()

    build = PCBuild(name, purpose, cpu, gpu, ram, storage, case)
    calculate_total(build)

    while True:
        decision = review_build(build)

        if decision == "C":
            builds.append(build)
            save_build(build)
            print("\nBuild saved successfully.")
            break
        elif decision == "E":
            edit_build(build)
        else:
            print("Invalid choice. Please enter C or E.")


main()