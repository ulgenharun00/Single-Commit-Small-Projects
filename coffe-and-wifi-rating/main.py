from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Location (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time (e.g., 9:00 AM)', validators=[DataRequired()])
    close_time = StringField('Closing Time (e.g., 9:00 PM)', validators=[DataRequired()])
    wifi = IntegerField('WiFi Rating (1-5)', validators=[NumberRange(min=1, max=5)])
    power = IntegerField('Power Rating (1-5)', validators=[NumberRange(min=1, max=5)])
    coffee_rating = IntegerField('Coffee Rating (1-5)', validators=[NumberRange(min=1, max=5)])
    submit = SubmitField('Add Cafe')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # Collect the form data
        cafe_name = form.cafe.data
        location = form.location.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        wifi = form.wifi.data
        power = form.power.data
        coffee_rating = form.coffee_rating.data

        # Save the data to your CSV file
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([cafe_name, location, open_time, close_time, wifi, power, coffee_rating])  # Add all fields here

        return redirect('/cafes')  # Redirect to the list of cafes page after submitting

    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    cafes_list = []
    # Reading data from the CSV file
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        next(csv_data)  # Skip the header
        for row in csv_data:
            cafes_list.append({
                "name": row[0],
                "location": row[1],
                "open": row[2],
                "close": row[3],
                "coffee": row[4],
                "wifi": row[5],
                "power": row[6]
            })
    return render_template('cafes.html', cafes=cafes_list)

if __name__ == '__main__':
    app.run(debug=True)
