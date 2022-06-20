class Roi_calc:
    def __init__(self):
        self.properties = []
        self.properties_address = {}
        self.property_expenses = {}
        
        
    
    # add properties 
    def add_property(self):
        property_response = input('What nickname would you like to name your property i.e rental 1? ')
        self.properties.append(property_response)
            
    # add property address
    def choose_user(self):
        while True:
            print('Users:')
            for user in self.users:
                print(user)
            current = input('Choose a user: ')
            if current in self.users:
                self.current_user = current
                break
            else:
                print(f"{current} is not a user.")
            
    # add property expenses
    def add_to_watch_list(self, query=""):
        show = Series()
        show.get_info(query)
        self.watch_list.append(show)
        print(f"{show.title} has been added to the watchlist")
    
    # show list of properties
    def choose_from_watch_list(self):
        for series in self.watch_list:
            print(f"\n\n{series} | Episodes: {len(series)}")
            print(f"\nSummary: \n{series.summary}")
            print(f"\nCast: \n{series.cast}")
            display(Image(series.episodes[0].link))
            
        watch = input('What do you want to watch? ')
        
        if watch.lower() in list(map( lambda x: x.title.lower(), self.watch_list)):
            for series in self.watch_list:
                if series.title.lower() == watch.lower().strip():
                    series.play()
        else:   
            response = input(f'{watch} is not in your watch list. Would you like to add it? y/N')
            if response in ('yes','y'):
                self.add_to_watch_list(watch)
                self.watch_list[-1].play()

    # run 
    def run(self):
        """
            Method allowing users to input property details to calculate Return of investment (ROI) on a Rental property investment.
        """
        print("""
            What would you like to do?
            
            [1] - add a property 
            [2] - add rental income
            [3] - add monthly rental expenses i.e(tax,insurance,mortgage,utilities,maintaince)
            [4] - check ROI on a property
            [5] - quit app
        """)
        
        while True:
            response = input('Which option would you like to choose? (1, 2, 3, 4, 5)')
            
            if response == 1:
                pass
            elif response == 2:
                pass
            elif response == 3:
                pass
            elif response == 4:
                pass
            elif response == 5:
                print(f"Thanks for using the roi calc app.")
                break
            else:
                print("Incorrect input... Try again.")