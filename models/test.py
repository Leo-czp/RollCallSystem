import datetime,time
from config import initConfig




def jduge_course(week,day,time,teacherID):
    print(week,day,time)

week, day = judge_week()
time = judge_time()
jduge_course(week, day, time)
