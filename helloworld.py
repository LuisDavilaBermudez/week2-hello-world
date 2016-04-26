# Luis Davila-Bermudez

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

#First it says hello
print('Hello Sir/Madam.')
print('What is your name?') #Then it asks for your name
myname = input()
print('Hello, ' + myname) #it then says hello to you in english
print('What language would you prefer?')#it then asks for your prefered language
language = input()
print('You have chosen ' + language)#it then tells you what language you chose
if language == 'English':
    print('Hello Sir')#it then greets you if you chose a valid language
elif language == 'Spanish':
    print('Hola Senor')
elif language == 'German':
    print('Guten Tag')

exit
    

