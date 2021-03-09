from config import initConfig
import datetime

class db_data_clear:

    def __init__(self):
        pass

    def judge_week_and_day(self):
        week = initConfig.__dict__['DICT_WEEK']
        now_time = datetime.datetime.now().strftime("%Y-%m-%d")
        date1 = datetime.datetime.strptime(now_time, "%Y-%m-%d")
        for key in week:
            date2 = datetime.datetime.strptime(key, "%Y-%m-%d")
            num = (date1 - date2).days
            if num <= 6:
                return week[key], num + 1

    def judge_time(self):
        time = initConfig.__dict__['DICT_TIME']
        now_time = datetime.datetime.now().strftime("%H:%M")
        date1 = datetime.datetime.strptime(now_time, "%H:%M")
        for key in time:
            date2 = datetime.datetime.strptime(key, "%H:%M")
            num = (date1 - date2).seconds / 60
            if num > 1000:
                num = 1440 - num
            if num <= 40:
                return time[key]

    def get_time(self, num):
        num = int(num)
        if num <= 2:
            key = 1
        elif num <= 5:
            key = 2
        elif num <= 7:
            key = 3
        elif num <= 10:
            key = 4
        elif num <= 12:
            key = 5
        else:
            key = 6
        return key

    def judge_True(self, data):
        if len(data) >= 1:
            return True
        else:
            return False

    def split_data(self,str):
        ls_1 = str.split(',')
        data = []
        for i in ls_1:
            ls_2 = i.split('-')
            if len(ls_2) == 1:
                data.append(int(ls_2[0]))
            else:
                data += [i for i in range(int(ls_2[0]),int(ls_2[1])+1)]
        return data

    def check_data_clear(self, data):
        empty = (' ', '无', ' ')
        ls = [[(), (), (), (), (), ()], [(), (), (), (), (), ()], [(), (), (), (), (), ()], [(), (), (), (), (), ()],
              [(), (), (), (), (), ()]]
        for i in range(len(data)):
            day = data[i][4].split(',')
            time = data[i][5].split(',')
            time1 = [self.get_time(i.split('-')[0]) for i in time]
            for da in day:
                for tim in time1:
                    ls[int(da) - 1][int(tim) - 1] = (data[i][-3], data[i][6], data[i][4] + '周 ' + data[i][5])
        for days in range(5):
            for times in range(6):
                if len(ls[days][times]) == 0:
                    ls[days][times] = empty
        return ls


    def find_class_data(self, data):
        class_ls = []
        week, day = self.judge_week_and_day()
        day = 3
        time = self.judge_time()
        # time = 8
        for i in data:
            weeks = self.split_data(i[3])
            days = self.split_data(i[4])
            times = self.split_data(i[5])
            if (week in weeks) and (day in days) and (time in times):
                class_ls.append(i[2])
        return class_ls, data[0][0]


class view_data_clear:

    def combine_score_student(self, data, score):
        data = list(data)
        print(score)
        for index,student in enumerate(data):
            student = list(student)
            for student_score in score:
                if student[0] == student_score[1]:
                    student += [f'{eval(student_score[2])}']
            data[index] = student
        for index_1, student_1 in enumerate(data):
            if len(student_1) == 4:
                data[index_1] = student_1 + ['0']
        return data

if __name__ == '__main__':
    data = (('202101', '001', '大数据18201', '1-6', '1,3', '7-8', 'A7108', '202101', '毛泽东思想和中国特色社会主义理论体系概论', '001',
          '大数据18201'), (
         '202101', '001', '大数据18203', '1-6', '1,3', '7-8', 'A7108', '202101', '毛泽东思想和中国特色社会主义理论体系概论', '001',
         '大数据18201'))
    db_data_clear().find_class_data(data)