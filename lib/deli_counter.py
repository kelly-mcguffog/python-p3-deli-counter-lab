katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line = "The line is currently:"
        for index, item in enumerate(katz_deli):
            line += f" {index+1}. {item}"
        print(line)


def take_a_number(katz_deli, string):
    katz_deli.append(string)
    index = katz_deli.index(string)
    print(f"Welcome, {string}. You are number {index+1} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
    # if len(katz_deli) == 0:
    #     print("There is nobody waiting to be served!")
    # else:
    #     for index, item in enumerate(katz_deli):
    #         if index == 0:
    #             print(f"Currently serving {item}.")
    #             katz_deli.remove(item)
    

