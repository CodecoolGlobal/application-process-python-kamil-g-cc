from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/add-applicant')
def add_applicant():
    if request.method == "POST":
        applicant_first_name = request.form.get("applicant-first-name")
        applicant_last_name = request.form.get("applicant-last-name")
        applicant_phone = request.form.get("applicant-phone")
        applicant_email = request.form.get("applicant-email")
        data_manager.add_applicant(applicant_first_name, applicant_last_name, applicant_phone, applicant_email)
        return redirect("/applicants")
    return render_template("add_applicant.html")

@app.route('/applicants-phone')
def applicant_phone():
    applicant_name = request.args.get('applicant-name')
    applicants = data_manager.get_applicants_by_name(applicant_name)
    return render_template("applicants.html", applicants = applicants)

@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    city_name = request.args.get('city-name')
    cities = data_manager.get_distinc_cities()
    if city_name == "-1":
        city_name = None
    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    else:
        if city_name:
            mentor_details = data_manager.get_mentors_by_city_name(city_name)
        else:
            mentor_details = data_manager.get_mentors()



    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('mentors.html', mentors=mentor_details, cities=cities, city_name=city_name, mentor_name=mentor_name)


if __name__ == '__main__':
    app.run(debug=True)
