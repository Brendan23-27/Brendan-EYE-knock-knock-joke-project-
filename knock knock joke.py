"""
Brendan Eye 1/12/24 This is my knock knock joke project
"""
username = input("what is your name?: ")
joke =input(f" hi {username}" " would you like to hear a joke?: ")
if joke.lower()==("yes"):   
    answer=input("knock knock:")
    if answer==("who's there?"):
            response=input("cow says:") 
            if response.lower()==("cow says who?"):
                response=print("no the cow says moo")
            elif response==("moo"):
                    print("wow you're smart you figured out the joke")
            else:
                print("you were suposted to say the cow says who")
    else:
        print("you were suposetd to say who's their")
else:
    print("that's unfortunte it was a good one") 
   

        
  
