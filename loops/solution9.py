items = ["apple", "banana", "orange", "apple", "mango"]


# for item in items:
#     item_count = items.count(item)
#     # print(item, item_count)
#     if item_count > 1:
#         print(item)
#         break




# second solution

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate:", item)
        break
    unique_item.add(item)