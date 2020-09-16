
name="anu"
age=11
fav_passtime = "I love to do coding"  # string with a sentence like "I love to do coding"
fav_movie = "Mission Impossible"  # string with one or multiple words
height_cm = 162.5  # data type float eg. 162.5 #Make sure before concatenating, you convert float type height_cm to string using str(height_cm)
sentence_3="My height is " + str(height_cm)
print(sentence_3)
fav_poem_2_lines = '''twinkle, twinkle little star
how I wonder what you are '''
about_myself = "My name is\t" + name + ".\n I am \t" + str(age) + "\t years old." + "\n My height is \t " + str(
   height_cm) + "\n" + fav_passtime + "\t in my free time." + "\n I love watching the movie - " + fav_movie + "\n Below are the 2 lines from my favourite poem:\n" + fav_poem_2_lines
print(about_myself)
name=input("what is your name: ")
print("my name is" + name)
school=input("Which school you go to? \t ")
age=input("How old are you?\t")
info=name+" "+school +" "+age
