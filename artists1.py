
fav_artists = ["Ado","Sleeping At Last","Two Door Cinema Club", "Lovejoy", "Araki"] #list of artists

print (f"Here are my favorite artists: {fav_artists}") #Shows the user the contents of the current list
user_suggestion = input("Suggest an artist:") #user inputs an artist suggestion

if user_suggestion in fav_artists: #if the suggestion is already on the list, print statement ensues
    print("I like this artist too!")

else: #otherwise, user suggestion is added to the list
    print("Good suggestion! Let me add it to the list.") 
    fav_artists.append(user_suggestion)
    print (f"Here are my favorite artists: {fav_artists}") #prints the new list with the added suggestion