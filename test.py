
month_map = {
    ',': '',
}

item = "1,503,166,644.7071228"
count = 0
for key, value in month_map.items():
    item = item.replace(key, value)
print(item)
