# Created 12/19/2020
# This is a secure password generator using alphabetic and numeric characters
# This generates crptographically secure random passwords using the secrets module
# This also calcuates the probability of randomly guessing the password

# Written by Paul A. Turner of the University of Central Florida
# College of Sciences | Department of Statistics & Data Science
# Bachelor of Science, Statistics

import secrets
import string
import statistics
import matplotlib.pyplot as plt

def main():

    a = input(">> Enter Number of Requests: ")
    b = input(">> Enter Password Length: ")
    c = int(a)
    d = int(b)

    # calculates the probability of the password being randomly guessed
    # passwords consist of letters, punctuation, and digits, totaling 36 possibilities. choosing the right letter is a 1/68 chance, which exponentially grows as more characters are added to the password.
    # formula: (1/36)^n, where n is the number of chacters in the password 
    prob = pow((1/36), d)

    # prints out the probability of guessing the password randomly; due to low probability, probability is represented as Ne-n, where N is the probability, and -n is the number of decimal places unable to be represented.
    print("\n >> WARNING: Passwords are NOT STORED, save the passowrd before closing the window <<")
    print("\n>> Probability of guessing individual passwords: " + str(prob) + "\n")

    # creates the alphabet of characters that can be chosen for the password
    alphabet = string.ascii_letters + string.digits

    # Prints the output of the generated passwords
    i = 0

    while (i < c):
        password = ''.join(secrets.choice(alphabet) for i in range (d))
        if(i == (c-1)):
            print("Password:\t" + password)
        else:
            print(str(i+1) +":\t"+ password+"\n")
        i = i+1
    
    j = 1
    probGuess = []
    count = []
    
    print("\n")
    
    while(j < d+1):
        probGuess.append(pow(1/36,j))
        count.append(j)
        j = j+1
    plt.title("Probability of Randomly Guessing Password\nCalculated by (1/36)^n, where n is the length of the password")
    plt.xlabel("Length of Password (by character)")
    plt.ylabel("Probability")
    plt.plot(count, probGuess)
    

if __name__ == "__main__":
    main()