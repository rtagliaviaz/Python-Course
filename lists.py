#demoList = [1, "hi", 1.5, true, ["mario", "link", "samus"]]
colors = ["red", "blue", "green"]
#constructor
numbersList = list((1, 2, 3, 4 ,5))
print(numbersList)


r=list(range(1, 10))
print(r)

print(dir(colors))
print(colors[1])
print(len(colors))
print("green" in colors)

print(colors)
colors[1] = "yellow"
print(colors)

colors.append("blue")
print(colors)

colors.extend(("black", "white"))
print(colors)

colors.extend(["silver", "gold"])
print(colors)

colors.insert(1, "violet")
print(colors)

colors.insert(len(colors), "orange")
print(colors)
#remove
colors.pop()
print(colors)

colors.pop(1)
print(colors)

colors.remove('green')
print(colors)

#colors.clear()

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)
