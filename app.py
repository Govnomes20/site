from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zodiac.db'
db = SQLAlchemy(app)

# Модель для знаков зодиака
class Zodiac(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    horoscope = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

# Создаем базу данных
with app.app_context():
    db.create_all()

# Гороскопы для каждого знака зодиака
horoscopes = {
    'Овен': 'Сегодня будет удачный день для начала новых начинаний.',
    'Телец': 'Ваша выносливость будет испытана, но не унывайте, всё наладится.',
    'Близнецы': 'Вам стоит быть внимательнее к своему окружению, возможны сюрпризы.',
    'Рак': 'Эмоциональная стабильность поможет вам преодолеть все трудности сегодня.',
    'Лев': 'Сегодняшний день принесет вам новые возможности для самореализации.',
    'Дева': 'Не забывайте делегировать задачи, чтобы избежать излишнего стресса.',
    'Весы': 'Гармония в отношениях с окружающими будет ключом к успеху сегодня.',
    'Скорпион': 'Будьте готовы к неожиданным поворотам событий, они могут оказаться полезными.',
    'Стрелец': 'Ваш оптимизм поможет вам преодолеть любые препятствия на пути к цели.',
    'Козерог': 'Сосредоточьтесь на своих целях и не теряйте веру в свои возможности.',
    'Водолей': 'Будьте гибкими и открытыми к изменениям, это поможет вам добиться успеха.',
    'Рыбы': 'Сегодня ваша интуиция будет вашим лучшим советником, доверьтесь ей.'
}

# Картинки для каждого знака зодиака
sign_images = {
    'Овен': 'https://upload.wikimedia.org/wikipedia/commons/e/e6/RR5110-0049R.gif',
    'Телец': 'https://upload.wikimedia.org/wikipedia/commons/7/71/RR5110-0050R.gif',
    'Близнецы': 'https://upload.wikimedia.org/wikipedia/commons/1/10/RR5110-0051R.gif',
    'Рак': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/RR5110-0052R.gif',
    'Лев': 'https://upload.wikimedia.org/wikipedia/commons/f/f0/RR5110-0040R_%D0%9B%D0%B5%D0%B2.gif',
    'Дева': 'https://upload.wikimedia.org/wikipedia/commons/a/ac/RR5111-0115R.gif',
    'Весы': 'https://upload.wikimedia.org/wikipedia/commons/7/74/RR5110-0042R_%D0%92%D0%B5%D1%81%D1%8B.gif',
    'Скорпион': 'https://upload.wikimedia.org/wikipedia/commons/1/11/RR5110-0043R_%D0%A1%D0%BA%D0%BE%D1%80%D0%BF%D0%B8%D0%BE%D0%BD.gif',
    'Стрелец': 'https://upload.wikimedia.org/wikipedia/commons/b/b2/RR5111-0119R.gif',
    'Козерог': 'https://upload.wikimedia.org/wikipedia/commons/1/1a/RR5110-0045R_%D0%9A%D0%BE%D0%B7%D0%B5%D1%80%D0%BE%D0%B3.gif',
    'Водолей': 'https://upload.wikimedia.org/wikipedia/commons/4/44/RR5111-0122R.gif',
    'Рыбы': 'https://upload.wikimedia.org/wikipedia/commons/c/c7/RR5110-0048R.gif'
}

@app.route('/')
def index():
    random_sign = random.choice(list(horoscopes.keys()))
    horoscope = horoscopes[random_sign]
    image_url = sign_images[random_sign]
    return render_template('index.html', sign=random_sign, horoscope=horoscope, image_url=image_url, signs=horoscopes.keys())

@app.route('/update_sign', methods=['POST'])
def update_sign():
    selected_sign = request.json['sign']
    horoscope = horoscopes[selected_sign]
    image_url = sign_images[selected_sign]
    return jsonify({'sign': selected_sign, 'horoscope': horoscope, 'image_url': image_url})

if __name__ == "__main__":
    app.run(debug=True)
