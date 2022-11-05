firts_friend_speed = 4
second_friend_speed = 5
dog_speed = 10
distance = 1000
distance_limit = 10
dog_counter = 0
dog_direction = 1
while distance > distance_limit:
    speed = 0
    if dog_direction == 1:
        speed = firts_friend_speed + dog_speed
        dog_direction = 2
    else:
        speed = second_friend_speed + dog_speed
        dog_direction = 1
    time_to_meet = distance / speed
    distance = distance - (time_to_meet *
                           (firts_friend_speed + second_friend_speed))
    dog_counter = dog_counter + 1
    print('disntance =', distance)
print('count =', dog_counter)