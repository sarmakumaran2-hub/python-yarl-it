id=3001
name="seelan"
grade="10A"
nic=200511111111

output1=("student id is " +str(id)+"\nstudent name is "+name+
"\nstudent grade is"+grade+"\nstudent nic is "+str(nic))
print(output1)

output2=("student id is %d  \nstudent name is %s \nstudent grade is %s \nstudent nic is %d " %(id,name,grade,nic))
print(output2)

output3=("student id is {} \nstudent name is {} \nstudent grade is {} \nstudent nic is {}".format(id,name,grade,nic))
print(output3)

output4=("student id is {0} \nstudent name is {1} \nstudent grade is {2} \nstudent nic is {3}".format(id,name,grade,nic))
print(output4)

output5=(f"student id is {id} \nstudent name is {name} \nstudent grade is {grade} \nstudent nic is {nic}")
print(output5)

output6=("student id is",id,"student name is",name,)
print(output6)