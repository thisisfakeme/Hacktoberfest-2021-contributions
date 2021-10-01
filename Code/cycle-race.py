#define variables
isTestPass = ""
isRoundPass = ""

#display welcome message
print("\n------ Welcome to Downtown Cycle Race ------\n")

#start infinite loop
while (True):

    #take user input for medical test
    isTestPass = input("Did you pass the medical test (yes/no): ")
    
    #continue to 10 rounds
    #lower() used to trun input into lowercase
    #strip() used to remove unnecessary whitespaces in input
    if (isTestPass.lower().strip()=="yes"):
    
        #display preliminary stage welcome messages
        print("\nGreat, you can proceed to ten rounds")

        #loop through 10 rounds
        for i in range(1,11):
          
            #start infinite loop to keep in same round until user input valid input
            while (True):
          
                #ask user about round completion
                isRoundPass = input("\nDid you complete round "+str(i)+"? (yes/no): ")

                #terminate program if round fail
                if (isRoundPass.lower()=="no"):
                    print("\nSORRY! You cannot proceed to the final stage. Try again next time.")
                    break #break second while loop

                #go to next rounds
                elif (isRoundPass.lower()=="yes"):
                    #print "selected for final stage" when the last round complete
                    if (i==10):
                        print("\nCONGRATULATIONS! You have selected for the final stage!")
                        break #break second while loop

                    #continue to next round
                    else:
                        print("CONGRATULATIONS! Proceed to round",i+1)
                        break #break second while loop

                #display invalid input and ask same question    
                else:
                    print("INVALID INPUT! Please enter a valid input")

            #end loop if user fail round
            if(isRoundPass.lower()=="no"):
                break #break for loop
        break  #break first while loop
            
    #display unable to participate message
    elif (isTestPass.lower()=="no"):
        print("\nSORRY! You cannot participate in the race!")
        break  #break first while loop

    #if user input is invalid, repeat the process
    else:
        print("\nINVALID INPUT! Please enter a valid input\n")

#display thankyou message
print("\n------ Thank You for Joining with Us ------")