def hello():
    print('hello user!')
def pack(blue, green, red):
    return [blue, green, red]
def eat_lunch(my_list):
    if len(my_list) == 0:
        print("Lunchbox is empty")
    else: 
        for i in range(len(my_list)):
         if i == 0:
            print(f"First i eat {my_list[0]}")
        else:
            print(f"First i eat {my_list[0]}")

hello()
print(pack("blue","green","red"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwhich"])
eat_lunch(["toast","sandwhich","eggs","meat"])