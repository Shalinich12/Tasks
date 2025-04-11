def reserve(bus_no, seats):
    buses = {
        'bus1': 20,
        'bus2': 42,
        'bus3': 12
    }
    if bus_no in buses:
        if seats <= buses[bus_no]:
            buses[bus_no] -= seats
            return f"booked {seats} successfully"
        else:
            return "seats not available"
    else:
        return "invalid bus number"


print(reserve("bus1", 10))