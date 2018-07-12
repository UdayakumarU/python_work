n = input()
n = n.lower()
vowel =['a','e','i','o','u']
con =['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
if n in vowel:
	print("Vowel")
elif n in con:
	print("Consonant")
else :
    print("Invalid")
