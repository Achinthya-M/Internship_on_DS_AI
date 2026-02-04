numbers = [10,20,30,40]
coordinates = (5,10)
print(numbers)
print(coordinates)

a = [100,200,300,400,500,600,700,800,900]
print(a[-3:-1]) 
print(a[-1:-3]) 
print(a[1:4:2])
print(a[1:7:2])
print(a[-7:-3:2])

marks = [95,75,85,65]
marks.append(55)
print(marks)
marks.pop()
marks.sort()
print(marks)
marks.reverse()
print(marks)

#task 1
list = ["Apple","Banana","Carrot","Dates"]
print(list)
list.append("Egg")
print(list)
list.remove("Banana")
print(list)
list.sort()
print(list)

#task 2
temperatures = [22,24,25,28,30,29,27,26,24,22]
print(temperatures[0])
print(temperatures[-1])
print(temperatures[3:6])
print(temperatures[-3:])

#task 3
screen_res = (1920,1080)
print(f"Current Resolution:{screen_res[0]}x{screen_res[1]}")
#screen_res[0] = 1280
print("Tuple cannot be modified")