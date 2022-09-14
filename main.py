def Intro():
  print(f'Hello {name} ')

class Chatbox():
  def __init__(self, name):
    self.name = name
def init_chat():
    quit = "quit"

name = input("Hello, Welcome to Chatbox,  What is your name? " )
print("Nice to meet you " + name + "! ")


y = True
while y == True:   
  choice = input("Chatbox can talk to you about certain topics, choose a topic: \n1. school \n2. feeling \n3. number \n4. sports \n5. exit \n")
  if (choice == "1" or choice == "school" or choice == "School"):
    subject = input("What is your favorite subject? ")
    if(subject != ""):
      print("That is my favorite subject too!")
  if (choice == "feeling" or choice == "2" or choice == "Feeling"):
    feelings = input("How are you feeling today? ")
    if(feelings == "good" or feelings ==  "great" or feelings == "happy" or feelings ==       "okay"):
      print("That's Awesome")
    elif(feelings == "bad" or feelings == "sad" or feelings == "not good" or feelings ==   "depressed"):
      print("I am sorry to hear that, I hope your day gets better!")

  if (choice == "3" or choice == "number" or choice == "Number"):
      number = input("What is your favorite number? ")
      if (number != "7"):
        print("Nice, my favorite number is 7 ")
      elif(number == "7"):
        print("Thats also my favorite number!")

  if(choice == "4" or choice == "sports" or choice == "Sports"):
      sports = input("What is your favorite sport? ")
      sports_lists = ["football", "basketball", "soccer", "baseball", "tennis", "hockey",   "golf", "volleyball", "boxing", "swimming", "track", "table tennis", "badminton",   "cricket"]
      if (sports in sports_lists):
        print("Nice, My favorite sport is football, Broncos Country Let's Ride! ")
      elif(sports not in sports_lists):
        print("I have never heard of that sport! ")

  if(choice == "5"):
    print("Goodbye nice chatting with you");
    y = False

  

    