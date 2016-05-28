from flask_wtf import Form
from wtforms import StringField, DateTimeField, SubmitField, BooleanField, SelectField, TextAreaField, DecimalField,PasswordField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, EqualTo
from ..models import Department, Employee, Role


class CostForm(Form):
    event_time = DateTimeField('发生时间', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    dept_name = SelectField('部门', coerce=int, validators=[DataRequired()])
    cost_label = StringField('分类', validators=[DataRequired()])
    cost_detail = TextAreaField('备注')
    cost_money = DecimalField('金额', places=2)
    party_employee = SelectField('当事人', coerce=int, validators=[DataRequired()])
    submit = SubmitField('确认添加')

    def __init__(self):
        super(CostForm, self).__init__()
        self.dept_name.choices = [(dept.dept_id, dept.dept_name) for dept in Department.query.order_by(Department.dept_name).all()]
        self.party_employee.choices = [(emp.employee_id, emp.employee_name) for emp in Employee.query.order_by(Employee.employee_name).all()]


class LoginForm(Form):
    login_name = StringField('登录名', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('保持登陆')
    submit = SubmitField('登录')


class AddEmployee(Form):
    login_name = StringField('登录名', validators=[DataRequired(), Length(1, 64)])
    employee_name = StringField('员工名', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('密码', validators=[DataRequired(), EqualTo('password2', message='2次密码不一致')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    dept_name = SelectField('部门', coerce=int, validators=[DataRequired()])
    role_name = SelectField('职位', coerce=int, validators=[DataRequired()])

    def __init__(self):
        super(AddEmployee, self).__init__()
        self.dept_name.choices = [(dept.dept_id, dept.dept_name) for dept in Department.query.order_by(Department.dept_name).all()]
        self.role_name.choices = [(role.role_id, role.role_name) for role in Role.query.order_by(Role.role_id).all()]

    def validate_login_name(self, filed):
        # 如果表单类中定义了以validate_ 开头且后面跟着字段名的方法，这个方法就和常规的验证函数一起调用。
        if Employee.query.filter_by(login_name=filed.data).first():
            raise ValidationError('此登录名已存在。')