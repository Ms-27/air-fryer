from flask import Flask, render_template_string, request

from page_template import PAGE


app = Flask(__name__)


def convert_for_airfryer(temperature: float, time_minutes: float) -> dict:
    """Conversion simple et pratique (estimation)."""
    return {
        "temperature": max(80, round(temperature - 15)),
        "time": max(1, round(time_minutes * 0.8)),
    }


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    values = {"temperature": "", "time": ""}

    if request.method == "POST":
        temperature = float(request.form["temperature"])
        time_minutes = float(request.form["time"])

        values = {
            "temperature": request.form["temperature"],
            "time": request.form["time"],
        }
        result = convert_for_airfryer(temperature, time_minutes)

    return render_template_string(PAGE, result=result, values=values)


if __name__ == "__main__":
    app.run(debug=True)
