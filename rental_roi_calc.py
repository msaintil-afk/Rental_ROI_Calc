class Roi_calc:
    def __init__(self):
        self.properties = []
        self.properties_address = {}
        self.property_expenses = {}
        self.rental_income = {}
        
        
        
    
    # add properties 
    def add_property(self):
        property_response = input('What nickname would you like to name your property i.e rental #1? ')
        self.properties.append(property_response)
        print(f"You've just addded the {property_response} property")
        print(f"Here's a list of your properties {self.properties}")
            
    # add property address and property total cost
        address_response = input("What is the address of the property?")
        print(f"You've just added {address_response} property address")
        address_cost = input("What is the total cost of this property?")
        self.properties_address[address_response] = address_cost
        print(f"Here's a list of property addresses {self.properties_address.keys()}")
            
    # add property expenses
    def add_expenses(self):
        print(f"{self.properties_address.keys()}")
        expense_reponse = input("Which Property Address would you like to add expenses for?" )
        expense_amount = input ("What is the total monthly expense for this property?")
        self.property_expenses[expense_reponse] = expense_amount
        print(f"Here's a list of your properties with expenses: {self.property_expenses}")
    
    # add rental income
    def add_rental_income(self):
        print(self.properties_address.keys())
        request_income_response = input("What is the address you would like to add the rental income to?")
        add_income_response = input("What is the rental income for this address?")
        self.rental_income[request_income_response] = add_income_response
        print(f"Here is a list for your properties with the rental income: {self.rental_income}")



    # run 
def run():
    user = Roi_calc()
    """
        Method allowing users to input property details to calculate Return of investment (ROI) on a Rental property investment.
    """
    while True:
        print("""
        What would you like to do?
        
        [1] - add a property 
        [2] - add rental income
        [3] - add total monthly rental expenses i.e(tax,insurance,mortgage,utilities,maintaince)
        [4] - check ROI on a property
        [5] - quit app
    """)
        response = input('Which option would you like to choose? (1, 2, 3, 4, 5)')
        
        if response == '1':
            user.add_property()
        elif response == '2':
            user.add_rental_income()
        elif response == '3':
            user.add_expenses()
        elif response == '4':
            pass
        elif response == '5':
            print(f"Thanks for using the roi calc app.")
            break
        else:
            print("Incorrect input... Try again.")
run()