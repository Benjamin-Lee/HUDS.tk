from flask import Flask, redirect
import pendulum

app = Flask(__name__)
@app.route("/")
def home():
	# get the current time
	now = pendulum.now('America/New_York')
	print(pendulum.Date.today().day_of_week)
	# handle Sunday schedule
	if pendulum.Date.today().day_of_week == 0:
		if now.time() <  pendulum.time(14, 30, 00):
			meal = 0
		else:
			meal = 1

	# every other day of the week
	else:
		if now.time() < pendulum.time(10, 15, 00):
			meal = 0
		elif now.time() < pendulum.time(14, 15, 00):
			meal = 1
		else:
			meal = 2

	return redirect(f"http://www.foodpro.huds.harvard.edu/foodpro/menu_items.asp?date={now.month}-{now.day}-{now.year}&type=05&meal={meal}")