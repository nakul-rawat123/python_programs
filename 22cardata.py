class data:
    def speed(s, speeds):
        speeds.sort()
        print(f'your highest speed was: {speeds[-1]} and lowest speed was: {speeds[0]}')
    def distance(s, total_distance):
        print('total distance traveled is:', total_distance)
total_distance = 0
speeds = []
car1 = data()
while True:
    speed = int(input('what was your speed? '))
    speeds.append(speed)
    car1.speed(speeds)
    distance = int(input('how much distance did u travel? '))
    total_distance += distance
    car1.distance(total_distance)