# Student A
def encoder( password):
    encoded=""
    for digit in password:
        if int(digit)+3>9:
            n= (int(digit)+3)%10
            encoded= encoded +str(n)
        else:
            encoded= encoded +str(int(digit)+3)
    return encoded

def decoder(encoded):
    Decoded=""
    for digit in encoded:
        if int(digit) -3<0:
            n=10 -1*(int(digit)-3)
            Decoded = Decoded + str(digit)
        else:
            Decoded= Decoded + str(int(digit)-3)
    return Decoded


def main ():
    Password=""
    encoded=""

    while True:
        print("Menu")
        print("-------------")
        print("""1. Encode
    2. Decode
    3. Quit """)

        option= int(input("Please enter an option: "))

        if option==1:
            Password = input("Please enter your password to encode: ")
            encoded= encoder(Password)
            print("Your password has been encoded and stored!")

        elif option==2:
            decoded= decoder(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")

        elif option==3:
            break

if __name__=="__main__":
	main()
