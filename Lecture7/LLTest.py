from LinkedList import LinkedList

lst = LinkedList()

# Add elements to the list
lst.add("Antigua and Barbuda")  # Add Antigua to the list
print("(1)", lst)

lst.insert(0, "St Lucia")  # Add St Lucia to the beginning of the list
print("(2)", lst)

lst.add("Russia")  # Add Russia to the end of the list
print("(3)", lst)

lst.addLast("Ukraine")  # Add Ukraine to the end of the list
print("(4)", lst)

lst.insert(2, "England")  # Add UK to the list at index 2
print("(5)", lst)

lst.insert(5, "Jamaica")  # Add Jamaica to the list at index 5
print("(6)", lst)

lst.insert(0, "Uganda")  # Same as list.addFirst("Antigua and Barbuda")
print("(7)", lst)

# Remove elements from the list
lst.removeAt(0)  # Remove the element at index 0
print("(8)", lst)

lst.removeAt(3)  # Remove the element at index 2
print("(9)", lst)

lst.removeAt(lst.getSize() - 1)  # Remove the last element
print("(10)", lst)
