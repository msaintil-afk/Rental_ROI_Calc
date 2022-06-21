class Roi_calc:
    def __init__(self):
        self.properties = []
        self.properties_address = {}
        self.property_expenses = {}
        self.rental_income = {}
        self.rental_roi = {}
        
        
        
        
    
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

    #method to calc roi (roi = rental income-expenses / total cost)
    def calc_roi(self):
        print("Here's a list of your properties with rental income/cost/expenses.")
        print(f"Here's your property/income:{self.rental_income}\nHere's your property/total cost:{self.properties_address}\nHere's your property/total expenses:{self.property_expenses}")
        roi_address = input("Select the property you would like to calc your ROI...")
        total_cost_response = int(input("Confirm the total cost of your property?"))
        rental_income_response = int(input(f"Confirm your monthly rental income"))
        rental_expense_response = int(input(f"Confirm your total monthly rental expenses"))
        cash_flow = rental_income_response - rental_expense_response
        yearly_cash_flow = cash_flow * 12
        roi = (yearly_cash_flow / total_cost_response) * 100
        self.rental_roi[roi_address] = roi
        print(f"Here is a list of your properties with your yeary roi percentages: {self.rental_roi} ")

    #function to show roi on investment
    def show_roi(self):
        print(f"Here is a list of your properties with your yeary roi percentages: {self.rental_roi} ")



#function to create border around text *used for text menu
def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

#variable to contain text menu
menu = ("""
        What would you like to do?
        
        [1] - add a property 
        [2] - add rental income
        [3] - add total monthly rental expenses i.e(tax,insurance,mortgage,utilities,maintaince)
        [4] - check ROI on a property
        [5] - show ROI on listed properties
        [6] - quit app
    """)


    # run method for user menu input
def run():
    user = Roi_calc()
    """
        Method allowing users to input property details to calculate Return of investment (ROI) on a Rental property investment.
    """
    while True:
        print(bordered(menu))
        response = input('Which option would you like to choose? (1, 2, 3, 4, 5, 6)')
        
        if response == '1':
            user.add_property()
        elif response == '2':
            user.add_rental_income()
        elif response == '3':
            user.add_expenses()
        elif response == '4':
            user.calc_roi()
        elif response == '5':
            user.show_roi()
        elif response == '6':
            print(f"Thanks for using the roi calc app.")
            break
        else:
            print("Incorrect input... Try again.")
run()