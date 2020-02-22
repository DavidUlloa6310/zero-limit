from sqlalchemy.exc import IntegrityError
from zero_limit.models import customer, location
from zero_limit.forms import reservation_form
from flask import redirect, render_template, flash
from zero_limit import app, db

@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html', title='Zer0-Limit')

@app.route('/store')
def store():
    return render_template('store.html', location = location)

@app.route('/reservation/<location_name>', methods=['GET','POST'])
def reservation(location_name):
    form = reservation_form()
    if form.validate_on_submit():
        new_customer = customer(parent_name = form.parent_name.data, child_name = form.child_name.data, email = form.email.data, location=location.query.filter(location.name=="The Citadel").first())
        db.session.add(new_customer)
        try:
            db.session.commit()
            flash(f"Thank you. Your reservation for {form.child_name.data} has been received and we've sent you a confirmation email at {form.email.data}. ")
        except IntegrityError:
            db.session.rollback()
            flash(f"{form.child_name.data} already has a reservation.", 'Error')
    return render_template('reservation.html', location_name=location_name, form=form)