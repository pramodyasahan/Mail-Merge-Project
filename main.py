# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r".\Input\Letters\starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()

print(letter)

with open(r".\Input\Names\invited_names.txt", mode="r") as name_file:
    names = name_file.readlines()

print(names)

for name in names:
    name = name.strip()

    with open(f".\Output\ReadyToSend\letter_for_{name}.txt", mode="w") as file:
        new_letter = letter.replace("[name]", name)
        file.write(new_letter)
