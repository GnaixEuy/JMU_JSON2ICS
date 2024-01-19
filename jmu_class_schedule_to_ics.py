# -*- coding:utf-8 -*-
import datetime
import hashlib
import json
import os
import re

import pytz
from icalendar import Calendar, Event


# 为什么要sha1？
def sha1(data):
    return hashlib.sha1(data.encode('utf-8')).hexdigest()


# 在这里粘贴你获得的json
yourjson = {"workID": "201941054017", "Name": "苏粤翔", "className": "软件1991", "courses": [
    {"couName": "概率论与数理统计", "couDayTime": 1, "coudeTime": "12", "couRoom": "诚毅6-401", "couTeaName": "潘蕴静",
     "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994", "allWeek": "1-9", "three": "n"},
    {"couName": "软件设计与体系结构（JAVAEE）【中软】", "couDayTime": 1, "coudeTime": "12", "couRoom": "诚毅13-205",
     "couTeaName": "朱鹭山", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "10-15", "three": "n"},
    {"couName": "毛泽东思想和中国特色社会主义理论体系概论", "couDayTime": 1, "coudeTime": "34", "couRoom": "诚毅4-301",
     "couTeaName": "程保锐", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "1-14", "three": "n"},
    {"couName": "WEB前端开发基础【中软】", "couDayTime": 1, "coudeTime": "56", "couRoom": "诚毅13-205",
     "couTeaName": "张小平", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "1-15", "three": "n"},
    {"couName": "WEB前端开发基础【中软】", "couDayTime": 1, "coudeTime": "78", "couRoom": "诚毅13-205",
     "couTeaName": "张小平", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "1-15", "three": "n"},
    {"couName": "大学英语(4)", "couDayTime": 2, "coudeTime": "12", "couRoom": "诚毅1-203", "couTeaName": "曾雪梅",
     "className": "软件1991", "comboClassName": "软件1991,软件1992", "allWeek": "1-15", "three": "n"},
    {"couName": "数据库概论", "couDayTime": 2, "coudeTime": "34", "couRoom": "诚毅9-505", "couTeaName": "夏丽丽",
     "className": "软件1991", "comboClassName": "软件1991,软件1992", "allWeek": "1-15", "three": "n"},
    {"couName": "职业素质与大学生活【中软】（4）", "couDayTime": 2, "coudeTime": "56", "couRoom": "诚毅6-401",
     "couTeaName": "谢中", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "13-14", "three": "n"},
    {"couName": "WEB前端开发基础【中软】", "couDayTime": 2, "coudeTime": "56", "couRoom": "诚毅13-205",
     "couTeaName": "张小平", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "15-15", "three": "n"},
    {"couName": "形势与政策(4)", "couDayTime": 2, "coudeTime": "78", "couRoom": "", "couTeaName": "陈利平",
     "className": "软件1991", "comboClassName": "电商1991,电商1992,软件1991,软件1992,软件1993,软件1994",
     "allWeek": "9-12", "three": "n"},
    {"couName": "职业素质与大学生活【中软】（4）", "couDayTime": 2, "coudeTime": "78", "couRoom": "诚毅6-401",
     "couTeaName": "谢中", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "13-14", "three": "n"},
    {"couName": "数据库概论", "couDayTime": 3, "coudeTime": "12", "couRoom": "诚毅13-605", "couTeaName": "夏丽丽",
     "className": "软件1991", "comboClassName": "软件1991,软件1992", "allWeek": "1-15", "three": "n"},
    {"couName": "概率论与数理统计", "couDayTime": 3, "coudeTime": "34", "couRoom": "诚毅6-401", "couTeaName": "潘蕴静",
     "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994", "allWeek": "1-9", "three": "n"},
    {"couName": "WEB前端开发基础【中软】", "couDayTime": 3, "coudeTime": "34", "couRoom": "诚毅13-205",
     "couTeaName": "张小平", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "15-15", "three": "n"},
    {"couName": "毛泽东思想和中国特色社会主义理论体系概论", "couDayTime": 4, "coudeTime": "12", "couRoom": "诚毅4-301",
     "couTeaName": "程保锐", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "1-14", "three": "n"},
    {"couName": "大学英语(4)", "couDayTime": 4, "coudeTime": "34", "couRoom": "诚毅14-305", "couTeaName": "曾雪梅",
     "className": "软件1991", "comboClassName": "软件1991,软件1992", "allWeek": "1-15", "three": "n"},
    {"couName": "体育与健康(4)", "couDayTime": 4, "coudeTime": "78", "couRoom": "", "couTeaName": "篮球场",
     "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994", "allWeek": "1-18", "three": "n"},
    {"couName": "软件设计与体系结构（JAVAEE）【中软】", "couDayTime": 5, "coudeTime": "12", "couRoom": "诚毅9-503",
     "couTeaName": "朱鹭山", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "5-10", "three": "n"},
    {"couName": "软件设计与体系结构（JAVAEE）【中软】", "couDayTime": 5, "coudeTime": "12", "couRoom": "诚毅13-205",
     "couTeaName": "朱鹭山", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "11-15", "three": "n"},
    {"couName": "数据库概论", "couDayTime": 5, "coudeTime": "34", "couRoom": "诚毅7-507", "couTeaName": "夏丽丽",
     "className": "软件1991", "comboClassName": "软件1991,软件1992", "allWeek": "1-2", "three": "n"},
    {"couName": "思想政治理论课实践教学", "couDayTime": 5, "coudeTime": "56", "couRoom": "诚毅4-201",
     "couTeaName": "陈利平", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "2-14", "three": "n"},
    {"couName": "软件设计与体系结构（JAVAEE）【中软】", "couDayTime": 5, "coudeTime": "78", "couRoom": "诚毅13-205",
     "couTeaName": "朱鹭山", "className": "软件1991", "comboClassName": "软件1991,软件1992,软件1993,软件1994",
     "allWeek": "1-15", "three": "n"}]}
# 或者填入你获得的json的地址
yourjson_local: str | None = r"C:\Users\nbdhc\WebstormProjects\kebiao\kebiao.json"
# 路径存在时读
if os.path.exists(yourjson_local):
    with open(yourjson_local, 'r', encoding='utf-8') as file:
        yourjson = json.load(file)

# 在这里修改你开学第一周时间
# yourstarttime = '2021-03-01'
yourstarttime = '2024-02-26'


def get_semesters_to_json():
    return [{"Name": "2020-2021学年第一学期", "Code": "20201"}, {"Name": "2020-2021学年第二学期", "Code": "20202"},
            {"Name": "2021-2022学年第一个学期", "Code": "20211"}]


def get_course_take_weeks(all_week):  # 返回课程上课的周
    course_take_weeks = []
    is_interval = 0
    if '单周' in all_week:
        is_interval = 1
    elif '双周' in all_week:
        is_interval = 2
    match_object = re.match(r'(\d+)-(\d+)', all_week)
    if match_object:
        start_week = int(match_object.group(1))
        end_week = int(match_object.group(2))
        for i in range(start_week, end_week + 1):
            if is_interval == 0 or (is_interval == 1 and i % 2 != 0) or (is_interval == 2 and i % 2 == 0):
                course_take_weeks.append(i)
    return course_take_weeks


def get_course_date(course_in_day_of_week, which_week, first_day_date_str=yourstarttime):  # 返回上课的日期
    first_day_date = datetime.datetime.strptime(
        first_day_date_str, r'%Y-%m-%d')
    return first_day_date + datetime.timedelta(days=(which_week - 1) * 7 + (course_in_day_of_week - 1))


def get_course_take_time(course_time):  # 返回上课时间
    course_time_table = {'12': [[8, 0, 0], [9, 35, 0]],
                         '34': [[10, 5, 0], [11, 40, 0]],
                         '56': [[14, 0, 0], [15, 35, 0]],
                         '78': [[15, 55, 0], [17, 30, 0]],
                         '910': [[19, 0, 0], [20, 35, 0]]}
    return course_time_table[course_time][0], course_time_table[course_time][1]


def get_course_take_time_by_course_start_unit(course_start_unit: int, course_end_unit: int = None):
    course_time_table = {1: [[8, 0, 0], [9, 35, 0]],
                         3: [[10, 5, 0], [11, 40, 0]],
                         5: [[14, 0, 0], [15, 35, 0]],
                         7: [[15, 55, 0], [17, 30, 0]],
                         9: [[19, 0, 0], [20, 35, 0]]}
    return course_time_table[course_start_unit][0], course_time_table[course_start_unit][1]


def main():

    time_zone = pytz.timezone('Asia/Shanghai')
    with open(yourjson_local, 'r',encoding='utf-8') as file:
        kebiao_data = json.load(file)

    calendar = Calendar()
    calendar.add('prodid', '-//My calendar product//mxm.dk//')
    calendar.add('version', '2.0')

    for course in kebiao_data:
        # 课程在星期几
        course_in_day_of_week = int(course['weekday'])
        # 课程开始和结束的时间单位
        course_start_unit = int(course['startUnit'])
        course_end_unit = int(course['endUnit'])
        # 课程的上课周次
        course_weeks = course['weekIndexes']

        # 这里需要根据实际的时间表来计算课程的具体时间
        course_begin_time, course_end_time = get_course_take_time_by_course_start_unit(course_start_unit,
                                                                                       course_end_unit)

        for week in course_weeks:
            # 计算课程的具体日期
            course_date = get_course_date(course_in_day_of_week=course_in_day_of_week, which_week=week)

            event = Event()
            event.add('summary', course['courseName'])
            event.add('dtstart',
                      datetime.datetime(course_date.year, course_date.month, course_date.day, course_begin_time[0],
                                        course_begin_time[1], course_begin_time[2], tzinfo=time_zone))
            event.add('dtend',
                      datetime.datetime(course_date.year, course_date.month, course_date.day, course_end_time[0],
                                        course_end_time[1], course_end_time[2], tzinfo=time_zone))
            event.add('location', course['room'])
            calendar.add_component(event)

    output_file_name = 'schedule.ics'
    with open(output_file_name, 'wb') as output_file:
        output_file.write(calendar.to_ical())


if __name__ == '__main__':
    main()
