class PCBuild:
    def __init__(self, customer, purpose, cpu, gpu, ram, storage, case):
        self.__customer = customer
        self.__purpose = purpose
        self.__cpu = cpu
        self.__gpu = gpu
        self.__ram = ram
        self.__storage = storage
        self.__case = case
        self.__total = 0.0

    # Setters
    def set_customer(self, customer):
        self.__customer = customer

    def set_purpose(self, purpose):
        self.__purpose = purpose

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_gpu(self, gpu):
        self.__gpu = gpu

    def set_ram(self, ram):
        self.__ram = ram

    def set_storage(self, storage):
        self.__storage = storage

    def set_case(self, case):
        self.__case = case

    def set_total(self, total):
        self.__total = total

    # Getters
    def get_customer(self):
        return self.__customer

    def get_purpose(self):
        return self.__purpose

    def get_cpu(self):
        return self.__cpu

    def get_gpu(self):
        return self.__gpu

    def get_ram(self):
        return self.__ram

    def get_storage(self):
        return self.__storage

    def get_case(self):
        return self.__case

    def get_total(self):
        return self.__total

    # Display method
    def display_order(self):
        print("\nPRECISION PC BUILDER SUMMARY")
        print("--------------------------------")
        print(f"1. Customer: {self.__customer}")
        print(f"2. Purpose: {self.__purpose}")
        print(f"3. CPU: {self.__cpu}")
        print(f"4. GPU: {self.__gpu}")
        print(f"5. RAM: {self.__ram}")
        print(f"6. Storage: {self.__storage}")
        print(f"7. Case: {self.__case}")
        print(f"8. Total Build Cost: ${self.__total:.2f}")