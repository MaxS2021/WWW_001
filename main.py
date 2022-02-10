from flask import Flask, url_for, request, render_template, json
from flask import redirect

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/success')
def success():
    param = {}
    param['username'] = "Пользователь"
    param['title'] = 'Успешная регистрация'
    return render_template('success.html', **param)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)

@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', title='Новости', news=news_list)

@app.route('/ochered')
def ochered():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    #param['title'] = 'Домашняя страница'
    return render_template('ochered.html', **param)

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')