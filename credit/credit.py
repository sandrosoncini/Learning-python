from cs50 import get_string

valid = ""
while (valid.isnumeric() == False):
    valid = get_string("Number: ")

card = list(map(int, str( valid)))
size = len(card)


def card_name():
    if (size is 15):
        if(card[0] is 3 and (card[1] is 3 or card[1] is 7)):
            print("AMEX")
    elif(size is 16 or size is 13):
        if(card[0] is 5 and (card[1] >= 1 or card[1] <= 5)):
            print("MASTERCARD")
        elif(card[0] is 4): 
            print("VISA")
    else:
        print("INVALID")
        
def luhns_method():      
    new_list = []
    counter = 1 
        
    while counter <= size:
        if (counter % 2 == 0):
            value = card[size - counter] * 2
            string = str(value)
            if len(string) > 1:
                new_list.append(int(string[0]))
                new_list.append(int(string[1]))
            else:
                new_list.append(value)
        else: 
            new_list.append(card[size - counter])        
        counter += 1
        
            
    to_str = str(sum(new_list))
    
    if to_str[len(to_str) - 1] is '0':
        card_name ()
    else:
        print("INVALID")
        
luhns_method()

        
    
    
        
       






