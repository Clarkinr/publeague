# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("Welcome to the publeague tournament tracker!\n")
tour_name = input("What is the name of your tournament\n")
num_teams = input("Please enter the number of teams in your torunament: \n")
print(f"Your tournament bracket will contain {num_teams} teams\n")
print("Please select a tournament type:\n 1. Round Robin\n 2. Round Robin Double Split\n 3. Single Elimination\n 4. Double Elimination\n")
tour_typ = input("Type number for option 1, 2, 3 or 4 : \n")

def generate_single_elim(self, num_teams, tour_typ, team_names):
    self.num_teams = num_teams
    self.tour_typ = tour_typ
    self.team_names = [team_names]

list1 = list() #empty list

num = input("How many elements do you want") #user tells the range(optional)

#iterating till user's range is reached
for i in range(int(num)): 
    n = input("Enter a value ")#asking for input of 1 value 
    list1.append(int(n))#adding that value to the list

print(list1)