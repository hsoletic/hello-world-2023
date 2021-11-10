print("range 1 to 10")
for x in range(1,10):
    print(x)

items = ["item1", "item2", "item3"]

print("item in items")
for item in items:
    print(item)

print("using the length of the array")
for x in range(len(items)):
    print("x is" + str(x))
    print("item is" + items[x])

global x
x = 0

def increaseCount():
    global x
    x += 1

while x <10:
        x += 1
        print(x)


    