from flask import Flask, url_for, request, render_template, json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)

@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)

@app.route('/ochered')
def ochered():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    #param['title'] = 'Домашняя страница'
    return render_template('ochered.html', **param)

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')