from flask import Flask

# 1. CI Тестілеуге Арналған Функция
def add(a, b):
    # **Сценарий 1 (Success) үшін дұрыс логиканы қалдырамыз**
    return a + b

# 2. Flask Серверін Іске Қосуға Арналған Қолданба Объектісі
app = Flask(__name__)

@app.route('/')
def index():
    return 'CI Pipeline Alpha: The app is running. Try accessing /add/<int:a>/<int:b> to use the add function.'

@app.route('/add/<int:a>/<int:b>')
def api_add(a, b):
    # Тестіленетін функцияны API арқылы пайдалану
    result = add(a, b)
    # JSON форматында қайтару
    return {'result': result}

if __name__ == '__main__':
    # Жергілікті әзірлеу кезінде іске қосу
    app.run(debug=True)