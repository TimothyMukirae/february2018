word1 = input("Enter a word: ")
word2 = input("Enter a word: ")

letters1 = {}
letters2 = {}

for letter in word1:
	
	#Check if letter is in dictionary
	if letter in letters1:
		#If the letter is in the dictionary, increase its value by 1
		letters1[letter] = letters1[letter] + 1
	#If the letter is not in the dicitonary
	else:
		#Add it to the dictionary with a default value of 1
		letters1[letter] = 1

	#If letter is nnot in dictionary create a key value pair with a default value of 1
	#If the letter is in the dictionary increase its value by 1
	# letters1[letter] = letters1.get( letter, 0 ) + 1
	

#Repeat for word2 and letters2
for letter in word2:
	
	#Check if letter is in dictionary
	if letter in letters2:
		#If the letter is in the dictionary, increase its value by 1
		letters2[letter] = letters2[letter] + 1
	#If the letter is not in the dicitonary
	else:
		#Add it to the dictionary with a default value of 1
		letters2[letter] = 1


	#If letter is nnot in dictionary create a key value pair with a default value of 1
	#If the letter is in the dictionary increase its value by 1
	# letters2[letter] = letters2.get( letter, 0 ) + 1


#If both dictionaries have the same key:value pairs they are equal to eachother
if letters1 == letters2:
	#If they are equal then they are anagrams
	print("ANAGRAM")
#IF they are not equal they are not anagrams
else:
	print("NOT AN ANAGRAM")
