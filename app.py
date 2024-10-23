from flask import Flask, render_template, url_for, request, redirect
import calendar, rotomJr


# Setup
app = Flask(__name__)


# Handle Requests First
@app.before_request
def handle_form_submission():
    if request.method == 'POST':  
        num = request.form.get('dexInput')
        if num:
            return redirect(f'/dex/{num}/')


# Pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/viewbook/')
def view_book():
    # Render the HTML template to embed the PDF with a back button
    return render_template('viewbook.html')

@app.route('/events/')
def events():
    return render_template('events.html')

@app.route('/dex/', methods=['GET', 'POST'])
def dex_home():
    return render_template('dex_home.html')

@app.route('/dex/<int:mon>/')
@app.route('/dex/<string:mon>/')
def mon_page(mon):
    if str(mon).isdigit() and 0 < int(mon) < 494:
        if mon == 19:
            return render_template('dex/19.html')
        entry = rotomJr.get_mon(mon)
        img_path = f'img/sprites/front/{mon}.png'
        return render_template('dexpage.html', img_path=img_path, mon=mon, entry=entry)
    else:
        return render_template('error/404.html'), 404


# Errors --
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('error/500.html'), 500


# Built Ins
@app.context_processor
def utility_processor():
    def get_navigation():
        nav = [
            (url_for('dex_home'), "Pokedex Home"),
            (url_for('events'), 'Daily Events'),
            (url_for('view_book'), "View Book")
        ]
        return nav

    return dict(get_navigation=get_navigation, get_today=calendar.get_today)
