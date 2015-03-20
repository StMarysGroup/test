def open_file(your_file):                           #uses user inputted file
    fp = open(your_file, 'r')                       
    lines_in_file = []
    for line in fp:
        lines_in_file = lines_in_file + [line]
    fp.close()                                      #returns list of lines where 
    return lines_in_file                            #each line of the file is a string in the list
    
def email_sender(file):
    sender_line = file[3]
    for char in sender_line:
        beginning_position = sender_line.find("<")
        ending_position = sender_line.find(">")
    extract_email = sender_line[beginning_position + 1:ending_position]
    print("Sender email:", extract_email)
    
def email_receiver(file):
    receiver_line = file[4]
    for char in receiver_line:
        beginning_position = receiver_line.find("<")
        ending_position = receiver_line.find(">")
    extract_email = receiver_line[beginning_position + 1:ending_position]
    print("Receiver email:", extract_email)


def date_sent(somefile):		#Finds the date the email was sent
    for line in somefile:
        if ":" in line:                 #Finds a line containing ‘:’
            date =  line[0 : 16]        
            return date

def subject(somefile):			#Finds the subject of the email (1st line)
    email_subject = somefile[0]	
    return email_subject

def sender_name(file):          #This function finds the name of the sender
    sender_line = file[3]       #assignes a variable to go see in position 3
    for char in sender_line:    #goes through every character of that line
        beginning_position = sender_line.find("<")  #finds the landmark "<"
    name = sender_line[0: beginning_position-1]     
    
    return "Sender's name is : " + name

def receiver_name(file):        #this function finds the name of the receiver
    receiver_line = file[4]     #assignes a variable to go see in position 4
    for char in receiver_line:  #goes through each character in that line
        beginning_position = receiver_line.find("<")    #finds the landmark "<"
    name = receiver_line[3 : beginning_position - 1]
    return "Receiver's name is: " + name


def main():
    file = input("What file would you like to input? ")
    opened_file = open_file(file)

    email_sender(opened_file)
    email_receiver(opened_file)
    
    print("Email sent on: ", date_sent(opened_file))
    print("Subject of email is: ", subject(opened_file))

    print(sender_name(opened_file))
    print(receiver_name(opened_file))

    print(ser





main()









