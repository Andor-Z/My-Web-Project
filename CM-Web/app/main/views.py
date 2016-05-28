from flask import render_template, current_app, session, redirect, url_for,request, flash
from flask_login import login_user, login_required, logout_user
from datetime import datetime
from . import main
from .forms import CostForm, LoginForm, AddEmployee
from .. import db
from..models import Cost, Department, Employee


@main.route('/', methods=['GET', 'POST'])
def index():
    form = CostForm()
    if form.validate_on_submit():
        c = Cost(
            record_time=form.event_time.data,
            cost_label=form.cost_detail.data,
            cost_detail=form.cost_detail.data,
            cost_money=form.cost_money.data,
            dept=Department.query.get(form.dept_name.data),
            employee=Employee.query.get(form.party_employee.data)
        )
        db.session.add(c)
        return redirect(url_for('main.index'))
    form.event_time.data = datetime.utcnow()
    costs = Cost.query.order_by(Cost.event_time.desc()).all()
    # if current_user.is_authenticated:
    return render_template('index.html', form=form, costs=costs)
    # else:
    #     return redirect(url_for('.login'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(login_name=form.login_name.data).first()
        if employee is not None and employee.verify_password(form.password.data):
            login_user(employee, form.remember_me.data)
            # 用户访问未授权的 URL 时会显示登录表单，Flask-Login会把原地址保存在查询字符串的 next 参数中，这个参数可从 request.args 字典中读取。如果查询字符串中没有 next 参数，则重定向到首页。
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('无效的用户名或密码')
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出。')
    return redirect(url_for('main.index'))


@main.route('/admin/add_employee', methods=['GET', 'POST'])
def add_employee():
    form = AddEmployee()
    if form.validate_on_submit():
        employee = Employee(login_name=form.login_name,
                            )
