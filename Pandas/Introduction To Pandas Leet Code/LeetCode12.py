import pandas as suraj
student1={'ids':[1,2,3,4,5],'name':["sumeet","suraj","balaji","rudra","jaga"],'age':[21,22,23,24,25]}
df1=suraj.DataFrame(student1)
student2={'ids':[6,7,8,9,10],'name':["sumeet","suraj","balaji","rudra","jaga"],'age':[21,22,23,24,25]}
df2=suraj.DataFrame(student2)
df_concatenated = suraj.concat([df1, df2])

print(df_concatenated)
