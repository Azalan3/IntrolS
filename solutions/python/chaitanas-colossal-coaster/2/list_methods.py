def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    if ticket_type == 0:
        normal_queue.append(person_name)

    return normal_queue

print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich"))
print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye"))


def find_my_friend(queue, friend_name):
    if friend_name in queue:
        return queue.index(friend_name) 
    return -1

print(find_my_friend(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve"))

def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index, person_name)
    return queue

print(add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky"))


def remove_the_mean_person(queue, person_name):
    if person_name in queue:
        queue.remove(person_name)
    return queue

print(remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran"))

def how_many_namefellows(queue, person_name):
    return queue.count(person_name)

print(how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha"))

def remove_the_last_person(queue):
    last_person = queue.pop()
    return last_person

print(remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))

def sorted_names(queue):
    return sorted(queue)
print(sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))