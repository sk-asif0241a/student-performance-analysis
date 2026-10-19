#Mini Project on Student Performance Analysis:
print('Student Marks')
print('------- -----')
import numpy as np
names=np.array(['Dinesh','Ravi','Raju','Kusma','Asif','Krishna'])
subjects=np.array(['Tel','Hin','Eng','Mat','Sci','Soc'])
marks=np.array([[89,97,85,86,90,79],
                [78,57,48,78,58,45],
                [68,45,36,42,32,85],
                [54,77,45,75,54,97],
                [45,56,67,78,89,90],
                [58,66,88,41,64,43]])
for i in range(len(names)):
    print(f'{names[i]}\t{marks[i]}')
print()
#Calculate student total,average,result and grade.
print('Student Total,Average,Result and Grade')
print('------- -------------------- --- -----')
total=np.sum(marks,axis=1)
average=np.mean(marks,axis=1)
result_text=np.all(marks>=35,axis=1)
result=np.where(result_text,'Pass','Fail')
conditions=np.array([(result=='Pass')&(average>=75),
                    (result=='Pass')&(average>=65),
                    (result=='Pass')&(average>=45),
                    (result=='Pass')&(average>=35),
                    (result=='Pass')&(average<35)])
values=np.array(['A-Grade','B-Grade','C-Grade','D-Grade','E-Grade'])
grade = np.select(conditions,values,default='No Grade') 
print('Names\tTotal\tAverage\tResult\tGrade')
for i in range(len(names)):
    print(f'{names[i]}\t{total[i]}\t{round(average[i],2)}\t{result[i]}\t{grade[i]}')
print()
#Subject Wise Analysis.
print('Subject Ranking')
print('------- -------')
sub_average=np.mean(marks,axis=0)
sub_max=np.max(marks,axis=0)
sub_min=np.min(marks,axis=0)
print('Subject\tAverage\tMaximum\tMinimum')
for i in range(len(subjects)):
    print(f'{subjects[i]}\t{round(sub_average[i],2)}\t{sub_max[i]}\t{sub_min[i]}')
print()
#Student Wise Analysis.
print('Student Ranking')
print('------- -------')
rank_index=np.argsort(total)[::-1]
print('Names\tRank')
for rank,index in enumerate(rank_index):
    print(f'{names[index]}\t{rank+1}')
print()
#Class Wise Analysis.
print('Class Performance')
print('----- -----------')
class_total=np.sum(marks)
class_average=np.mean(marks)
class_top=np.argmax(total)
class_least=np.argmin(total)
class_pass=np.count_nonzero(result=='Pass')
class_fail=np.count_nonzero(result=='Fail')
class_agrade=np.count_nonzero(grade=='A-Grade')
class_bgrade=np.count_nonzero(grade=='B-Grade')
class_cgrade=np.count_nonzero(grade=='C-Grade')
class_dgrade=np.count_nonzero(grade=='D-Grade')
class_egrade=np.count_nonzero(grade=='E-Grade')
print('Total Class Marks=',class_total)
print('Class Average=',round(class_average,2))
print(f'Class Topper={names[class_top]}\tMarks={total[class_top]}')
print(f'Class Duller={names[class_least]}\tMarks={total[class_least]}')
print('No. of students pass=',class_pass)
print('No. of students fail=',class_fail)
print('No. of students got A-Grade=',class_agrade)
print('No. of students got B-Grade=',class_bgrade)
print('No. of students got C-Grade=',class_cgrade)
print('No. of students got D-Grade=',class_dgrade)
print('No. of students got E-Grade=',class_egrade)
print('            The End          ')
