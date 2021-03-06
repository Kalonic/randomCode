def checkPlate(plate):
    plate = str(plate)
    if len(plate) != 7:
        return False
    else:
        plateArray = []
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        plate = plate.lower()
        for letter in plate:
            plateArray.append(letter)
        if alphabet.__contains__(plateArray[0]) and alphabet.__contains__(plateArray[1]) and alphabet.__contains__(plateArray[4]) and alphabet.__contains__(plateArray[5]) and alphabet.__contains__(plateArray[6]):
            try:
                plateArray[2] = int(plateArray[2])
                plateArray[3] = int(plateArray[3])
                if plateArray[2] in range(0, 10) and plateArray[3] in range(0, 10):
                    return True
                else:
                    return False
            except ValueError:
                return False
            else:
                return False
        else:
            return False

def checkTime(time1, time2):
    hours = float(time2) - float(time1)
    return hours

def checkSpeed(distance, time):
    speed = distance / time
    return str(speed)

while True:
    time1 = input('The time the car passed camera 1 in hours: ')
    try:
        time1 = float(time1)
        break
    except ValueError:
        print('Please enter a number in hours.')
        continue

while True:
    time2 = input('The time the car passed camera 1 in hours: ')
    try:
        time2 = float(time2)
        break
    except ValueError:
        print('Please enter a number in hours.')
        continue

hours = checkTime(time1, time2)
distance = 1

mph = checkSpeed(distance, hours)

plate = input('Please enter the number plate of the car: ').strip()
if not checkPlate(plate):
    print('That is not a valid numberplate. ')
else:
    mph = mph.strip('.0')
    print('The car with the numberplate \'' + plate + '\' was travelling at ' + mph + 'mph.')
