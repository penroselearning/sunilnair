from flask import Flask,render_template,request
from flask import session
from calculation import calc_square,convert_to_seconds,birthday_countdown,aspect_ratio_calculator
from word_cookies import find_words,find_vowels
from wild_cats import wild_cats
from guessing_game import guessing_game
from shopping_list import shopping_cart,shopping_cart_remove
from moon_phase_calculator import converttojulian,datetophase,specificdate,nextphasefm,nextphasenm

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Numbers
@app.route("/square",methods=["GET", "POST"])
def square():
    errors = ""
    result = ""
    number = None
    if request.method == "POST":
        if request.form["number"] is not None:
            try:
                number = float(request.form["number"])
            except:
                errors += f'Please Enter a Number'
            else:
                result = f'Square of {number} is {calc_square(number)}'
        else:
            errors += f'Please Enter a Number'
    return render_template("square.html",solution=result, error_msg=errors)

# For Loop
@app.route("/multiplication_table",methods=["GET","POST"])
def multiplicationtable():
    errors = ""
    number = None
    if request.method == "POST":
        if request.form["number"] is not None:
            try:
                number = int(request.form["number"])
            except:
                errors += f'Please Enter a Number'
        else:
            errors += f'Please Enter a Number'

    return render_template("multiplication_table.html",n=number, error_msg=errors)

@app.route("/guessing_game",methods=["GET","POST"])
def guessinggame():
    
    result =""
    errors =""
    guess = ""
    
    if request.method == "POST":
        try:
            guess=int(request.form["number"])
            result = guessing_game(guess)
        except:
            guess=0
    
    return render_template("guessing_game.html",game=result,error_msg=errors)

# List
@app.route("/shopping_list",methods=["GET","POST"])
def shoppinglist():
    
    result =""
    errors =""
    list=""
    remove=""
    
    if request.method == "POST":
        try:
            item = request.form["item"]
        except:
            remove = request.form["remove"]
        
        if remove == "":
            list = shopping_cart(item)
        else:
            list = shopping_cart_remove(remove)
        
    return render_template("shopping_list.html",cart=list,error_msg=errors)

# Dictionary
@app.route("/find_vowels",methods=["GET", "POST"])
def findvowels():
    errors = ""
    result = {}
    word = ""
    vowels={'a':0,'e':0,'i':0,'o':0,'u':0}

    with app.open_resource('static/engmix.txt') as file:
        wordlist = [x.strip().decode() for x in file.readlines()]
    
    if request.method == "POST":
        if request.form["text"] is not None:
            word = request.form["text"]
            if word in wordlist:
                result = find_vowels(word,vowels)
            else:
                errors += f'This Word does not exist in a dictionary'
        else:
            errors += f'Please Enter a Word'
    
    return render_template("find_vowels.html",solution=result, error_msg=errors)

# Combining Lists and Dictionaries
@app.route("/wild_cats",methods=["GET", "POST"])
def wildcats():
    errors = ""
    scat = ''
    
    wcats = wild_cats()

    if request.method == "POST":
        scat = request.form["cats"]
    
    #result = wild_cats(wild_cats)

    return render_template("wild_cats.html",cats=wcats,cat=scat, error_msg=errors)

# Date and Time
@app.route("/birthday_countdown",methods=["GET", "POST"])
def birthdaycountdown():
    errors=""
    result = None
    if request.method == "POST":
        if request.form["date"] is not None:
            try:
                birthdate = request.form["date"]
                year = int(birthdate[0:3])
            except:
                errors += f'Please select your correct birth date'
            else:
                print(type(birthdate))
                result = birthday_countdown(birthdate)
    
    return render_template("birthday_countdown.html",countdown=result,error_msg=errors)

@app.route("/convert_to_seconds",methods=["GET","POST"])
def converttoseconds():
    
    result=""
    errors=""
    y,mo,w,d,h,m = 0,0,0,0,0,0

    if request.method == "POST":
        try:
            y=int(request.form["years"])
        except:
            y=0
        try:
            mo=int(request.form["months"])
        except:
            mo=0
        try:
            w=int(request.form["weeks"])
        except:
            w=0
        try:
            d=int(request.form["days"])
        except:
            d=0
        try:
            h=int(request.form["hours"])
        except:
            h=0
        try:
            m=int(request.form["minutes"])
        except:
            m=0
    
    result = convert_to_seconds(y,mo,w,d,h,m)
    return render_template("convert_to_seconds.html",vals=(y,mo,w,d,h,m),solution=f'{result:,}', error_msg=errors)

# Build Functions
@app.route("/aspect_ratio_calculator",methods=["GET","POST"])
def aspectratiocalculator():
    d=""
    errors=""
    w,h,nw,nh = 0,0,0,0

    if request.method == "POST":
        if request.form["width"] is not None:
            try:
                w=int(request.form["width"])
            except:
                w=0
        if request.form["height"] is not None:
            try:
                h=int(request.form["height"])
            except:
                h=0
        if request.form["nwidth"] is not None:
            try:
                nw=int(request.form["nwidth"])
            except:
                nw=0
        if request.form["nheight"] is not None:
            try:
                nh=int(request.form["nheight"])
            except:
                nh=0
        
    d = aspect_ratio_calculator(w,h,nw,nh)
    return render_template("aspect_ratio_calculator.html",s=d, error_msg=errors)

@app.route("/moon_phase_calculator",methods=["GET", "POST"])
def moonphasecalculator():
    errors = ""
    result = ""
    next_full = ""
    next_new = ""

    next_full = nextphasefm()
    next_new = nextphasenm()

    if request.method == "POST":
        selecteddate = request.form["date"]
        
        if selecteddate !='':
            result = specificdate(selecteddate)
        else:
            errors += f'Please select a Date'
                
    return render_template("moon_phase_calculator.html",moonphase=result,nextfull=next_full, nextnew = next_new, error_msg=errors)

@app.route("/word_cookies_cheat",methods=["GET", "POST"])
def word_cookies_cheat():
    errors = ""
    result = ""
    letters = ""

    with app.open_resource('static/engmix.txt') as file:
        wordlist = [x.strip() for x in file.readlines()]

    if request.method == "POST":
        if request.form["letters"] is not None:
            letters = request.form["letters"]
            result = find_words(letters,wordlist)
        else:
            errors += f'Please Enter Letters'
    
    return render_template("word_cookies_cheat.html",solution=result, error_msg=errors)


if __name__ == '__main__':
    app.run(debug=True)
    session.clear()