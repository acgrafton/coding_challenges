"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""



# def find_survivor(num_people, kill_every):
#     """Given num_people in circle, kill [kill_every]th person, return survivor."""

#     if kill_every == 1:
#         return num_people

#     current = 0
#     people = list(range(1, num_people+1))
#     survivors = []
#     while len(people) != 1:
#         for person in people:
#             current += 1
#             if current == kill_every:
#                 current = 0
#             else:
#                 survivors.append(person)
#         people = survivors
#         survivors = []

#     return people[0]

class Node(object):
    """Doubly-linked node."""

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    @classmethod
    def make_list(cls, n):
        first = node = prev = cls(1)

        for i in range(2, n+1):
            node = Node(i, prev=prev)
            prev.next = node
            prev = node

        node.next = first
        first.prev = node
        
        return first

    def __repr__(self):
        return "<Node prev=%s data=%s next=%s>" % (
            self.prev.data, self.data, self.next.data)


def find_survivor(num_people, kill_every):

    current = Node.make_list(num_people)

    while current.next != current:
        for i in range(kill_every - 1):
            current = current.next

        current.prev.next = current.next
        current.next.prev = current.prev

        current = current.next

    return current.data



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
