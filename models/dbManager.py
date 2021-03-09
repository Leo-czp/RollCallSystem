import pymysql
from config import dbConfig
from models.data_clear import db_data_clear

class Manager:

    def __init__(self):
        self.db_data_clear = db_data_clear()
        self.connect = pymysql.connect(host=dbConfig.__dict__['HOST'],
                               port=3306,
                               user=dbConfig.__dict__['USERNAME'],
                               passwd=dbConfig.__dict__['USERPASSWORD'],
                               db=dbConfig.__dict__['DB'])
        self.cursor = self.connect.cursor()

    def CRU(self, sql):
        self.connect.ping(reconnect=True)
        try:
            self.cursor.execute('{};'.format(sql))
            self.connect.commit()
            self.connect.close()
            return True
        except:
            return False

    def look(self, sql): # The query
        self.connect.ping(reconnect=True)
        try:
            self.cursor.execute('{};'.format(sql))
            data = self.cursor.fetchall()
            self.connect.commit()
            self.connect.close()
            return data
        except:
            return False

    def login(self,teacherID,password):
        sql = "select * from teacher where (teacherID = '{}' and password = '{}') or (teacherEmail = '{}' and password = '{}')".format(teacherID,password,teacherID,password)
        self.connect.ping(reconnect=True)
        try:
            data = self.look(sql)
            return self.db_data_clear.judge_True(data)
        except:
            return False

    def coursetable(self, id):
        self.connect.ping(reconnect=True)
        sql = "select * from coursetimetable t1 join course t2 on t1.courseID = t2.courseID where t1.teacherID='{}'".format(id)
        try:
            data = self.look(sql)
            return self.db_data_clear.check_data_clear(data)
        except:
            return False

    def find_class(self,id):
        self.connect.ping(reconnect=True)
        sql = "select * from coursetimetable t1 join course t2 on t1.courseID = t2.courseID where t1.teacherID='{}'".format(id)
        try:
            data = self.look(sql)
            class_ls, courseid = self.db_data_clear.find_class_data(data)
            if self.db_data_clear.judge_True(class_ls):
                return self.find_student(class_ls), class_ls, courseid
            else: return '无课'
        except:
            return False

    def find_student(self, ls):
        self.connect.ping(reconnect=True)
        sql = 'select * from student where '
        for i in ls:
            sql += "classID = '{}' " .format(i)
            if i != ls[-1]:
                sql += 'or '
        try:
            data = self.look(sql)
            return data
        except:
            return False

    def find_score(self, courseId):
        self.connect.ping(reconnect=True)
        sql = "select * from score where courseid = '{}'".format(courseId)
        try:
            data = self.look(sql)
            return data
        except:
            return False



if __name__ == '__main__':
    Manager().find_score('202101')
    #print(Manager().get_time('5'))
    # print(dbConfig.__dict__['USERPASSWORD'])

    # ls = [[('','无',''),('','无','')],[],[],[],[]]