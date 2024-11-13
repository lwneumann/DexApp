from flask import Flask, render_template, url_for, request, redirect
import rotom, calendar, abilities, moves


# Setup
app = Flask(__name__)


# Handle Requests First
@app.before_request
def handle_form_submission():
    if request.method == 'POST':  
        num = request.form.get('dexInput')
        if num:
            return redirect(f'/dex/{num}/')
        else:
            return redirect(f'/search/{num}')


# --- Pages ---
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
            return render_template(f'dex/{mon}.html')
    else:
        return render_template('error/404.html'), 404

@app.route('/ability/')
def ability_page():
    return render_template('abilities.html', ability_list=abilities.ability_list)


@app.route('/moves/')
def move_page():
    return render_template('moves.html', move_list=moves.move_list)


@app.route('/search/<string:search>')
def search_page(search):
    return render_template("search.html", search=search)

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
            (url_for('move_page'), "Move List"),
            (url_for('ability_page'), "Ability List"),
            (url_for('events'), 'Daily Events'),
            (url_for('view_book'), "View Book")
        ]
        return nav

    return dict(get_navigation=get_navigation, get_today=calendar.get_today)
