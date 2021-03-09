import functools
import datetime,time

from models.data_clear import view_data_clear
from flask import Blueprint, render_template, redirect, make_response, url_for, request, flash, current_app
from models.dbManager import Manager

teacher = Blueprint('teacher', __name__)
Manager = Manager()
view_data_clear = view_data_clear()


def LoginValid(func):
    @functools.wraps(func)  ##保留原来的函数名字
    def inner(*args, **kwargs):
        try:
            pid = request.cookies.get("_PID")
        except:
            pid = " "
        if current_app.config['KEY'] in pid:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('teacher.login'))


    return inner


@teacher.route('/login', methods=["GET", "POST"])  # 登录路由
def login():
    error = ""
    if request.method == "GET":
        return render_template('login.html', error=error)
    if request.method == "POST":
        teacherid = request.form.get("userid")
        password = request.form.get("userpassword")
        if len(teacherid) >= 1 and len(password) >= 1:
            if Manager.login(teacherid, password):
                html = redirect(url_for('teacher.check'))
                code = make_response(html)
                token = current_app.config['KEY']
                pid = teacherid + token
                code.set_cookie('_PID', f'{pid}')
                return code
            else:
                error = "账号或密码错误"
        else:
            error = "账户或密码不能为空"
        return render_template('login.html', error=error)


@teacher.route('/forgot-password/', methods=["GET", "POST"])
@LoginValid
def forgot_password():
    return render_template('forgot-password.html')


@teacher.route('/check/', methods=["GET", "POST"])
@LoginValid
def check():
    teacherid = request.cookies.get('_PID')
    id = teacherid.split('{}'.format(current_app.config['KEY']))[0]
    data = Manager.find_class(id)
    if data == '无课':
        return redirect(url_for('teacher.tables'))
    score = Manager.find_score(data[2])
    students=view_data_clear.combine_score_student(data[0],score)
    print(students)
    return render_template('check.html', students=students,classes=data[1],courseid=data[2])


@teacher.route('/tables/', methods=["GET", "POST"])
@LoginValid
def tables():
    teacherid = request.cookies.get('_PID')
    id = teacherid.split('{}'.format(current_app.config['KEY']))[0]
    data = Manager.coursetable(id)
    return render_template('tables.html', data=data)


