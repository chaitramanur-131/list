present_count=0
absent_count=0
attendance=[1,0,1,0,0,1,1]
for n in attendance:
    if 1 ==n:
        print("present")
        present_count+=1
    elif 0==n:
        print("absent")
        absent_count+=1
    else:
        print("none")
print("present_count:",present_count)
print("absent_count:",absent_count)
total=present_count+absent_count
print("total:",total)
present_percentage=total/present_count
print("present_percentage:",present_percentage)
absent_percentage=total/absent_count
print("absent_count:",absent_count)
