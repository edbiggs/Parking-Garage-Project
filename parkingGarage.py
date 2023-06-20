# The class should contain at least three methods:
# - takeTicket
#    - This should decrease the amount of tickets available by 1
#    - This should decrease the amount of parkingSpaces available by 1
# - payForParking
#    - Display an input that waits for an amount from the user and store it in a variable
#    - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#    - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
#    - If the ticket has been paid, display a message of "Thank You, have a nice day"
#    - If the ticket has not been paid, display an input prompt for payment
#       - Once paid, display message "Thank you, have a nice day!"
#    - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#    - Update tickets list to increase by 1 (meaning add to the tickets list)

import time

class Parking_Garage: 
    def __init__(self, tickets, spaces, current_ticket, timer_start,timer_end,amount_due, ticket_paid):
        self.tickets = tickets
        self.spaces = spaces
        self.current_ticket = current_ticket
        self.timer_start = timer_start
        self.timer_end = timer_end
        self.amount_due = amount_due
        self.ticket_paid = ticket_paid

    def takeTicket(self):
        self.timer_start = time.time()
        self.current_ticket = True
        self.tickets -= 1
        self.spaces -= 1


    def payForParking(self):
        self.timer_end = time.time()
        time_passed = (self.timer_end - self.timer_start) 
        if time_passed < 10:
            print("You don't owe anything")
        else:
            if self.ticket_paid == False:        
                if time_passed > 10 < 20:
                    self.amount_due += 5
                elif time_passed > 20 < 30:
                    self.amount_due += 10
                else:
                    self.amount_due = 300
                try:
                    pay_prompt = int(input(f"Your total is: ${self.amount_due}. How much would you like to pay?"))
                except: 
                    print("Please type a valid number")          
                if pay_prompt >= self.amount_due:
                    print("Thank you for your purchase. You have 15 minutes to leave.") 
                    self.current_ticket = False
                    self.ticket_paid = True
                    self.timer_start = time.time()
                else:
                    self.amount_due -= pay_prompt
                    print(f"You still owe {self.amount_due}")
            if self.ticket_paid == True:
                print("You've already paid for your ticket")

        
    def leaveGarage(self):
        self.timer_end = time.time()
        time_passed = self.timer_end - self.timer_start
        if time_passed > 10:
            if self.ticket_paid == True:
                if self.timer_end - self.timer_start < 900:
                    print("Thank you, have a nice day!")
                else:
                    sucker_fee_prompt =("You gotta be quicker than that! You now owe $3,465. Would you like to pay now?(Y/N)").lower()
                    if sucker_fee_prompt == "y":
                        try:
                            pay_prompt = input(f"Your total is: ${self.amount_due}. How much would you like to pay?")
                        except: 
                            print("Please type a valid number")
                        if pay_prompt == self.amount_due:
                            print("Thank you for your purchase.")
                        elif pay_prompt < self.amount_due:
                            self.amount_due -= pay_prompt
                            while self.amount_due > 0:
                                input(f"You still owe {self.amount_due}. How much would you like to pay?")  
                                continue
                    else:
                        print("If you would like to disuss financing options with one of our team members, please call 1-800-123-456")        
            else:
                while self.ticket_paid == False:
                    response = input("You haven't paid your ticket yet. Would you like to pay now?(Y/N)").lower()
                    if response == "y":
                        try:
                            pay_prompt = int(input(f"Your total is: ${self.amount_due}. How much would you like to pay?"))
                        except: 
                            print("Please type a valid number")                     
                        if pay_prompt >= self.amount_due:
                            print("Thank you for your purchase.") 
                            self.current_ticket = False
                            self.ticket_paid = True
                    else:
                        continue
        print("Thank you for visiting.")
    
    def view_spaces(self):
        print(self.spaces)

    def view_tickets(self):
        print(self.tickets)
    
    def view_rates():
        print(rates)



ticket_list = 100

spaces_list = 100

my_ticket = None

my_parking_session =  Parking_Garage(ticket_list, spaces_list, my_ticket,0,0,0,False)

rates = {"Less than 10 seconds": "$0", "Less than 20 seconds": "$5", "less than 30 seconds": "$10", "Longer than 30 seconds": "$3,465"}

def view_rates():
    print(rates)

def run():
        startup = input("Welcome to the only parking garage available for several miles! Would you like to enter?(Y/N)").lower()
        if startup == 'y':
            my_parking_session.takeTicket()
            while True:
                action = input("What would you like to do?(Pay,Leave,View spaces, View tickets, View rates)").lower()
                if action == "pay":
                    my_parking_session.payForParking()
                    continue
                elif action == "leave":
                    my_parking_session.leaveGarage()
                    break
                elif action == "view spaces":
                    my_parking_session.view_spaces()
                    continue
                elif action == "view tickets":
                    my_parking_session.view_tickets()
                    continue        
                elif action == "view rates":
                    confirmation1 = input("Sorry, I didn't quite catch that. What did you want to do?(Pay,Leave,View spaces, View tickets, View rates)").lower()
                    if confirmation1 == "view rates":
                        confirmation2 = input("You know, spots fill up pretty quickly here. You might be better off just taking a ticket and worrying about the rates later. Are you sure you want to waster your valuable time reading a bunch of boring numbers?(Y/N)").lower()
                        if confirmation2 == "y":
                            my_parking_session.view_rates()
                else:
                    print("Input not recognized")
                    continue
            else:
                print("Oh... Well, alright then.")
                
                
run()









