class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

n = 1
names = []
print("1.- Add Name")
print("2.- Search Name")
print("0.- Exit")

while n != 0:
    n = int(input("Choice a option: "))
    match n:
        case 1:
            name = input("Type a name list 1 by 1(press 0 to exit): ")
            if name and name != "0":
                names.append(name)
        
        case 2:
            try:
                search = input("Type the name to search in the name list.")
                if search in names:
                    print("Name founded")
                else:
                    raise NotFoundException("Name not found")
            except NotFoundException as e:
                print(f"Error: {e.message}")
        
                

