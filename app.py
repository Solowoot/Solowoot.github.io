from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey_macbook_guide_2025'

@app.route('/')
def home():
    """Главная страница — гид по MacBook"""
    return render_template('index.html')

@app.route('/consult', methods=['POST'])
def consult():
    """Обработка заявки на консультацию"""
    name = request.form.get('name')
    phone = request.form.get('phone')
    
    if phone:
        # Вывод заявки в консоль
        print("=" * 40)
        print("📞 НОВАЯ ЗАЯВКА НА КОНСУЛЬТАЦИЮ")
        print(f"👤 Имя: {name if name else 'Не указано'}")
        print(f"📱 Телефон: {phone}")
        print("=" * 40)
        
        flash(f'{name if name else "Спасибо"}, ваша заявка принята! Эксперт перезвонит вам в течение 15 минут.', 'success')
    else:
        flash('Пожалуйста, укажите номер телефона.', 'error')
    
    return redirect(url_for('home', _anchor='consult'))

if __name__ == '__main__':
    app.run(debug=True, port=8800)
