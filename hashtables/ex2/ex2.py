#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ticket_dict = dict()

    route = []
    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination
    current_dest = ticket_dict["NONE"]
    pos = 0
    while pos < length:
        route.append(current_dest)
        current_dest = ticket_dict[current_dest]
        pos +=1





    return route


# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# print(reconstruct_trip(tickets, 3))