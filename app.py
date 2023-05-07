from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def change(by):
	visitors_count=visitors_count+by

def visitors():
	counter_read_file=open("count.txt", "r")
	visitors_count=int(counter_read_file.read())
	counter_read_file.close()

	change(1)

	counter_write_file=open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

	return render_template("index.html", count=visitors_count)

@app.route('/', methods=['POST'])
def covid_stats():
	counter_read_file.open("count.txt", "r")
	visitors_count=int(counter_read_file.read())
	counter_read_file.close()

	text=request.form['text']

	corona_data='https://covidstats-sdbd.onrender.com/?country='+text
	print(corona_data)
	return render_template("index.html", image(corona_data), count=visitors_count)

	if __name__ == "__main__":
		app.run()