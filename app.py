from flask import Flask, render_template, url_for, request, redirect
import rotom, calendar, abilities, moves


# Setup
app = Flask(__name__)


# Handle Requests First
@app.before_request
def handle_form_submission():
    if request.method == 'POST':  
        query = request.form.get('dexInput')
        
        # Just a number
        if str(query).isdigit() and 0 < int(query) < 494:
            return redirect(url_for('mon_page', mon=query))

        # Otherwise actually look into the search        
        result, single = rotom.search(query)

        if single:
            area = list(result.keys())[0]
            if area == "dex":
                return redirect(url_for('mon_page', mon=result['dex'][0][0]))
            elif area == "moves":
                # f'/moves/#{result['moves'][0]}'
                return redirect(url_for('move_page', _anchor=result['moves'][0]))
            elif area == "ability":
                # f'/ability/#{result['ability'][0]}'
                return redirect(url_for('ability_page', _anchor=result['ability'][0]))
        else:
            return redirect(url_for('search_page', searched=str(query), result=result))


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

@app.route('/search/')
def search_page():
    searched = request.args['searched']
    result = rotom.pretty_search(eval(request.args['result']))
    return render_template("search.html", searched=searched, result=result)


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
