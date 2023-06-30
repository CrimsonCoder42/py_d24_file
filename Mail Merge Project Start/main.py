#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def replace_name(name):
    with open("Input/Letters/starting_letter.txt") as file:
        content = file.read()
        new_content = content.replace(f"[name]", name)
        final_content = new_content.replace("Angela", "Devin")
        return final_content

def write_to(data, name):
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as file:
        file.write(data)


with open("Input/Names/invited_names.txt") as file:
        content = file.readlines()
        for item in content:
            name = item.strip()
            letter = replace_name(name)
            write_to(letter, name)
