def get_list_of_wagons(*nums):
    return list(nums)

print (get_list_of_wagons(1, 7, 12, 3, 14, 8, 5))

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    wagon = each_wagons_id[2:] + each_wagons_id[:2]
    one_index = wagon.index(1)
    fixed = wagon[:one_index + 1] + missing_wagons + wagon [one_index + 1:]
    return fixed


print (fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]))

def add_missing_stops(route, **stops):
    route["stops"] = list(stops.values())
    return route



print (add_missing_stops({"from": "New York", "to": "Miami"},
                    stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
                    stop_4="Jacksonville", stop_5="Orlando"))

def extend_route_information(route, more_route_information):
    route.update(more_route_information)
    return route

print (extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}))

def fix_wagon_depot(wagons_rows):
    zip_rows = zip(*wagons_rows)
    return [list(row) for row in zip_rows]


print (fix_wagon_depot([[(2, "red"), (4, "red"), (8, "red")],[(5, "blue"), (9, "blue"), (13,"blue")],[(3, "orange"), (7, "orange"), (11, "orange")],]))