from flask import render_template, current_app, session, redirect, url_for,request, flash
from flask_login import login_user
from datetime import datetime
from . import main
from .forms import CostForm, LoginForm
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
    return render_template('index.html', form=form, costs=costs, title=current_app.config['WEB_TITLE'])
    # else:
    #     return redirect(url_for('.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(login_name=form.login_name.data).first()
        if employee is not None and employee.verify_password(form.password.data):
            login_user(employee, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('无效的用户名或密码')
    return render_template('login.html', form = form, title=current_app.config['WEB_TITLE'])