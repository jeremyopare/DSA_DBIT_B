from SinglyLinkedList import LinkedList

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.display()

    ll.append_at_a_location(15, 1)
    ll.display()

    search_num = int(input("Enter number to search: "))
    index = ll.search(search_num)
    if index != -1:
        print(f"Element {search_num} found at index {index}")
    else:
        print(f"Element {search_num} not found")
