a,b = map(int,input().split())

map =  {
    1:31,
    3:31,
    5:31,
    7:31,
    8:31,
    10:31,
    12:31,
    4:30,
    6:30,
    9:30,
    11:30,
    2:28
}

day = {
    0:"MON",
    1:"TUE",
    2:"WED",
    3:"THU",
    4:"FRI",
    5:"SAT",
    6:"SUN"
}


day_sum = 0
for i in range(1,a):
    day_sum += map[i]

day_sum += (b-1)

print(day[day_sum%7])


