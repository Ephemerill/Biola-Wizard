from flask import Flask, render_template
from datetime import datetime
from scrape_menu import scrape_menu
from scrape_weather import get_weather

# Function to determine the current meal period based on time of day
def get_meal_period():
    current_time = datetime.now()
    hour = current_time.hour

    if 7 <= hour < 11:
        return 'breakfast'
    elif 11 <= hour < 16:
        return 'lunch'
    elif 16 <= hour < 20:
        return 'dinner'
    else:
        return 'late_night'

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    weather_data = get_weather()
    meal_period = get_meal_period()
    menu_data = scrape_menu()  # Get the full menu data
    
    # Extract the menu for the current meal period
    filtered_menu = menu_data.get(meal_period, [])

    return render_template('index.html', weather=weather_data, meal_period=meal_period, menu=filtered_menu)

@app.route('/scrape')
def scrape():
    menu_data = scrape_menu()
    return render_template('menu.html', menu=menu_data)
if __name__ == '__main__':


    app.run(debug=True)