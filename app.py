import random

from flask import Flask, render_template, request, redirect, url_for
from data import teachers, goals, goal_icons, days_of_week

from handler import update_data
from forms import RequestForm, BookingForm

app = Flask(__name__)
app.secret_key = 'REPLACE_ME'


@app.route('/')
def render_index():
    teachers_ = teachers.copy()
    random.shuffle(teachers_)

    teachers_ = teachers_[:6]

    return render_template('index.html',
                           teachers=teachers_,
                           goals=goals,
                           goal_icons=goal_icons
                           )


@app.route('/all/')
def render_all():
    teachers_ = teachers.copy()
    random.shuffle(teachers_)

    return render_template('index.html',
                           teachers=teachers_,
                           goals=goals,
                           goal_icons=goal_icons
                           )


@app.route('/goals/<goal>/')
def render_goal(goal):
    return render_template('goal.html',
                           goal=goal,
                           goals=goals,
                           goal_icons=goal_icons,
                           teachers=[teacher for teacher in teachers
                                     if goal in set(teacher.get('goals'))]

                           )


@app.route('/profiles/<int:profile_id>/')
def render_profile(profile_id):
    return render_template('profile.html',
                           profile=teachers[profile_id],
                           goals=goals,
                           days_of_week=days_of_week)


@app.route('/request/')
def render_request():
    return render_template('request.html',
                           goals=goals,
                           form=RequestForm())


@app.route('/request_done/', methods=['GET', 'POST'])
def render_request_done():
    if request.method != "POST":
        return redirect(url_for('render_request'))

    goal = request.form.get('goal')
    time = request.form.get('time')

    form = RequestForm()
    name = form.name.data
    phone = form.phone.data

    data = {'goal': goal,
            'time': time,
            'name': name,
            'phone': phone
            }
    update_data('request.json', data)

    return render_template('request_done.html',
                           goal=goals[goal],
                           time=time,
                           name=name,
                           phone=phone)


@app.route('/booking/<int:profile_id>/<day>/<time>/')
def render_booking(profile_id, day, time):
    return render_template('booking.html',

                           form=BookingForm(),
                           profile=teachers[profile_id],
                           day=day,
                           time=time,
                           days_of_week=days_of_week
                           )


@app.route('/booking_done/', methods=['GET', 'POST'])
def render_booking_done():
    if request.method != "POST":
        return redirect(url_for('render_index'))

    form = BookingForm()
    name = form.name.data
    phone = form.phone.data

    day = request.form.get('clientWeekday')
    time = request.form.get('clientTime')
    profile_id = request.form.get('clientTeacher')

    data = {'name': name,
            'profile_id': profile_id,
            'phone': phone,
            'day': day,
            'time': time
            }
    update_data('booking.json', data)

    return render_template('booking_done.html',
                           name=name,
                           phone=phone,
                           day=days_of_week[day],
                           time=time)


if __name__ == '__main__':
    app.run(debug=True)
