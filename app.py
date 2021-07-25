from flask import Flask, request, render_template
from tradingview_ta import TA_Handler, Interval, Exchange


app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template('aa.html ')

@app.route('/', methods = ['POST'])
def my_form_post():
    text = request.form['m']
    handler = TA_Handler(
    symbol= text,           ###Stock Name Goes Here!!!!
    exchange="NSE", 
    screener="India",
    interval="1d",
    timeout=None
    )
    a = handler.get_analysis().summary
    if a['BUY'] > a['SELL']:
        return f"{a['BUY']*4}% buy "
    elif a['BUY'] < a['SELL']:
        return f"{a['SELL']*4}% sell "
    else:
        return "neutral"



    return processed_text 




if __name__ =='__main__':
    app.debug=True
    app.run(host='localhost', port=5000)
    
