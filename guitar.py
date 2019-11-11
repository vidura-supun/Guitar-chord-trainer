#!/usr/bin/python

dlist =[]
list1 = ['A', 'D', 'E']
list2 = ['A', 'D', 'E', 'Am', 'Dm', 'Em']
list3 = ['A', 'D', 'E', 'C', 'G', 'Am', 'Dm', 'Em']

def main():
    banner = """
       _____
                      q o o p
                      q o!o p
                      d o!o b
                       \!!!/
                       |===|
                       |!!!|
                       |!!!|
                       |!!!|
                       |!!!|
                       |!!!|
                      _|!!!|__
                    .+=|!!!|--.`.
                  .'   |!!!|   `.\
                 /     !===!     \\
                 |    /|!!!|\    ||
                  \   \!!!!!/   //
                   )   `==='   ((
                 .'    !!!!!    `..
                /      !!!!!      \\
               |       !!!!!       ||
               |       !!!!!       ||
               |       !!!!!       ||
                \     =======     //
                 `.    ooooo    .;' ~vidura supun~
                   `-._______.
            """
    print(banner)
    print("\n\n~Select the level~\n\n1.Beginner: A, D, E\n2.Not so beginner: A, D, E, Am, Dm, Em\n2. Intermediate: A, D, E, C, G, Am, Dm, Em\n\n")
    dec = input("LEVEL:")
    if dec=="1": list == list1
    elif dec=="2": list == list2
    elif dec=="3": list == list3
    else: defList()

def defList():
    print("Put in the chords you wanna practice CAWBOI-")
    custC = "1"
    while custC!="":
        custC = input("")
        dList.append(custC)
