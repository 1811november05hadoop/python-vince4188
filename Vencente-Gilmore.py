#!/usr/bin/env python3

'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''

'''
Use the main function for testing purposes and to show me results for all functions.
'''
def main():
	#reverse
	print(reverse('abcdef'))
	print(reverse('She sold seashells by the seashore'))
	#acronym
	print(acronym('Portable Network Graphics'))
	print(acronym('portable network graphics'))
	#armstrong
	print("Is 10 an armstrong number: " + str(armstrong(10)))
	print("Is 153 an armstrong number: " + str(armstrong(153)))
	#primeFactors
	print(primeFactors(8))
	print(primeFactors(901255))
	#whichTriangle
	print(whichTriangle(5,5,5))
	print(whichTriangle(5,5,10))
	print(whichTriangle(4,5,6))
	#scrabble
	print(scrabble('cabbage'))
	#pangram
	print(str(pangram('The quick brown fox jumps over the lazy dog')))
	print(str(pangram('not a pangram at all')))
	#sort
	print(sort([5,4,9,1,2]))
	print(sort([2,4,5,1,3,1]))
	#rotate
	print(rotate(5, 'omg'))
	print(rotate(26, 'word'))
	print(rotate(13, 'The quick brown fox jumps over the lazy dog'))
	#evenAndOdds
	evenAndOdds()
'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''
#done
def reverse(string):
	length = len(string) - 1
	result = ""
	for i in range(length, -1, -1):
		result += string[i]
	return result
'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
#done
def acronym(phrase):
	split = phrase.upper().split()
	length = len(split)
	result = ''
	for i in range(0, length):
		result += str(split[i])[0]
	return result
'''
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
#done
def whichTriangle(sideOne, sideTwo, sideThree):

	if sideOne == sideTwo and sideTwo == sideThree:
		return 'equlateral'
	elif sideOne == sideTwo or sideOne == sideThree or sideTwo == sideThree:
		return 'isoceles'
	else:
		return 'scalene'

'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
#done
def scrabble(word):
	one = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']
	two = ['d', 'g']
	three = ['b', 'c', 'm', 'p']
	four = ['f', 'h', 'v', 'w', 'y']
	five = ['k']
	eight = ['j', 'x']
	ten = ['q', 'z']
	word = word.lower()
	value = 0
	for c in word:
		if c in one:
			value += 1
		elif c in two:
			value += 2
		elif c in three:
			value += 3
		elif c in four:
			value += 4
		elif c in five:
			value += 5
		elif c in eight:
			value += 8
		elif c in ten:	
			value += 10
		else:
			print("Not a letter")	
	return value
'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.

param: int
return: bool
'''
#done
def armstrong(number):
	power = len(str(number))
	total = 0
	for i in range(0, power):
		total += pow(int(str(number)[i]), power)
	return total == number
'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
#done
def primeFactors(number):
	result = list()
	
	while number % 2 == 0:
		result.append(2)
		number = number/2

	for i in range(3,int(number+1),2):
		while number % i == 0:
			result.append(i)
			number = number/i
		if number == 1:
			break
	return result
'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
#done
def pangram(sentence):
	sentence = sentence.lower()
	letterSet = set()
	for c in sentence:
		if c != ' ':
			letterSet.add(c)
	if len(letterSet) == 26:
		return True
	else:
		return False
'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way

param: list
return: list
'''
def sort(numbers):
	index = 0
	for i in range(0,len(numbers)-1):
		index = i
		swap = i
		for j in range(i+1, len(numbers)):
			if numbers[index] > numbers[j]:
				swap = numbers[j]
				index = j
		if index != i:
			numbers[index] = numbers[i]
			numbers[i] = swap
	return numbers
'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.

Ciphertext is written out in the same formatting as the input including
spaces and punctuation.

Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
#done
def rotate(key, string):
	result = ""
	for c in string:
		temp = ord(c)
		if temp >= 97 and temp <= 122:
			if (temp + key) > 122:
				temp = 96 + (temp + key - 122)
			else:
				temp += key
		elif temp >=65 and temp <= 90:
			if (temp + key) > 90:
				temp = 64 + (temp + key - 90)
			else:
				temp += key
		result += chr(temp) 
	return result
'''
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none, from the keyboard
return: nothing
'''
#done
def evenAndOdds():
	even = open('even.txt', 'w')
	odd = open('odd.txt', 'w')
	for i in range(0, 10):
		temp = int(input("Enter a number: "))
		if temp%2 == 0:
			even.write(str(temp) + '\n')
		else:
			odd.write(str(temp) + '\n')
	even.close()
	odd.close()



if __name__ == "__main__":
    main()
