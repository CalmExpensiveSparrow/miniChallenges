
def numletter():
    letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    numletter_dict = {}

    for letter in letters:
        num = ord(letter) - 96  # Convert letter to number value
        numletter_dict[str(num)] = letter  # "1": "a"

    return numletter_dict

def xxx(given_number: str):  # given_number = "3,2,1"
    numletter_dict = numletter()
    num_list = [int(given_number[i]) for i in range(len(given_number))]  # num_list = [3, 2, 1]
    # combos.reverse()

    for i in range(1, len(given_number)):
        add = int(given_number[i-1])
        if add > 2:
            continue
        num = add*10 + int(given_number[i])
        num_list.append(num)
        add = 0

    for num in num_list:
        numstr = str(num)
        if numstr in numletter_dict:
            print(f"{numstr}: {numletter_dict[numstr]}")


    # ["1", "12", "123"]
xxx("111")





