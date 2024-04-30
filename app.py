from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_sftp_score(days, updates_per_day, ratio, percent_not_delivered, percent_oos_fail):
    score_a = 10 if days <= 2 else 7.5 if days <= 4 else 5 if days <= 6 else 2.5 if days <= 8 else 0
    score_b = 10 if updates_per_day >= 3 else 7.5 if updates_per_day >= 2 else 5 if updates_per_day >= 1 else 2.5 if updates_per_day >= 0.5 else 0
    score_c = 10 if ratio >= 5.0 else 7.5 if ratio >= 4.0 else 5 if ratio >= 2.0 else 2.5 if ratio >= 1.0 else 0
    score_d = 10 if percent_not_delivered <= 1 else 7.5 if percent_not_delivered <= 2 else 5 if percent_not_delivered <= 5 else 2.5 if percent_not_delivered <= 10 else 0
    score_e = 10 if percent_oos_fail <= 1 else 7.5 if percent_oos_fail <= 2 else 5 if percent_oos_fail <= 5 else 2.5 if percent_oos_fail <= 10 else 0
    total_score = ((score_a + score_b + score_c + score_d + score_e) / 5) * 10
    return total_score

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        days = float(request.form.get("days"))
        updates_per_day = float(request.form.get("updates_per_day"))
        ratio = float(request.form.get("ratio"))
        percent_not_delivered = float(request.form.get("percent_not_delivered"))
        percent_oos_fail = float(request.form.get("percent_oos_fail"))
        
        total_sftp_score = calculate_sftp_score(days, updates_per_day, ratio, percent_not_delivered, percent_oos_fail)
        return render_template("index.html", total_sftp_score=total_sftp_score)
    else:
        # Initial load or no data posted yet
        return render_template("index.html", total_sftp_score="Enter the values to calculate the SFTP score")

if __name__ == "__main__":
    app.run(debug=True)

