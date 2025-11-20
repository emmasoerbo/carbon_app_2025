from flask import render_template, Blueprint, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, ScooterForm, BybanenForm, TrainForm, WalkForm
import json

carbon_app = Blueprint('carbon_app', __name__)

# Emissions factor per transport in kg per passenger km
efco2 = {
    'Bus': {'Diesel': 0.030, 'Biodiesel': 0.014, 'Electric': 0.013},
    'Car': {'Gasoline Small': 0.25, 'Diesel Campervan': 0.745, 'Diesel Big': 0.505,
            'Diesel Medium': 0.380, 'Electric Big': 0.130, 'Electric Medium': 0.1,
            'Electric Small': 0.075},
    'Train': {'Diesel': 0.091, 'Electric Nordic': 0.007},
    'Plane': {'Business': 0.284, 'Economy Premium': 0.155, 'Economy': 0.127},
    'Ferry': {'Diesel': 0.186, 'Electric': 0},
    'Bybanen': {'Electric': 0.004},
    'Scooter': {'Electric': 0},
    'Bicycle': {'No Fossil Fuel': 0},
    'Walk': {'No Fossil Fuel': 0}
}
efch4 = {
    'Bus': {'Diesel': 0, 'CNG': 0, 'Petrol': 0, 'No Fossil Fuel': 0},
    'Car': {'Gasoline Small': 0, 'Diesel Campervan': 0, 'Diesel Big': 0,
            'Diesel Medium': 0, 'Electric Big': 0, 'Electric Medium': 0,
            'Electric Small': 0},
    'Train': {'Diesel': 0, 'Electric Europe': 0, 'Electric Nordic': 0},
    'Plane': {'Business': 0, 'Economy Premium': 0, 'Economy': 0},
    'Ferry': {'Diesel': 0, 'Electric': 0},
    'Bybanen': {'Electric': 0},
    'Scooter': {'Electric': 0},
    'Bicycle': {'No Fossil Fuel': 0},
    'Walk': {'No Fossil Fuel': 0}
}

#Carbon app
@carbon_app.route('/carbon_app')
@login_required
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')

@carbon_app.route('/carbon_app/new_entry')
def new_entry():
    return render_template('carbon_app/new_entry.html', title='new_entry')

# New entry bus
@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET', 'POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel,
                              co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bus.html', title='new entry bus', form=form)

#New entry car
@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        passengers = form.passengers.data
        transport = 'Car'
        
        # total utslipp for kjøretøyet 
        co2_total = float(kms) * efco2[transport][fuel]
        # utslipp per person
        co2 = co2_total / passengers

        co2 = float("{:.2f}".format(co2))
        co2_total = float("{:.2f}".format(co2_total))
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, passengers=passengers, co2=co2, total=co2_total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_car.html', title='new entry car', form=form)

# New entry train
@carbon_app.route('/carbon_app/new_entry_train', methods=['GET', 'POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel,
                              co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))

    return render_template('carbon_app/new_entry_train.html', title='new entry train', form=form)

# New entry bybanen
@carbon_app.route('/carbon_app/new_entry_bybanen', methods=['GET', 'POST'])
@login_required
def new_entry_bybanen():
    form = BybanenForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bybanen'

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel,
                              co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bybanen.html', title='new entry bybanen', form=form)

# New entry scooter
@carbon_app.route('/carbon_app/new_entry_scooter', methods=['GET', 'POST'])
@login_required
def new_entry_scooter():
    form = ScooterForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Scooter'

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel,
                              co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_scooter.html', title='new entry scooter', form=form)

# New entry ferry
@carbon_app.route('/carbon_app/new_entry_ferry', methods=['GET', 'POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel,
                              co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_ferry.html', title='new entry ferry', form=form)

# New entry plane
@carbon_app.route('/carbon_app/new_entry_plane', methods=['GET', 'POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel,
                              co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_plane.html', title='new entry plane', form=form)

# NEW: New entry walk – 0 utslipp, ingen fuel_type nødvendig
@carbon_app.route('/carbon_app/new_entry_walk', methods=['GET', 'POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        transport = 'Walk'
        fuel = 'No Fossil Fuel'

        co2 = 0.0
        total = 0.0

        emissions = Transport(
            kms=kms,
            transport=transport,
            fuel=fuel,
            co2=co2,
            total=total,
            author=current_user
        )
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_walk.html', title='new entry walk', form=form)

# Your data
@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    # Table
    seven_days_ago = datetime.now() - timedelta(days=7)
    entries = (Transport.query
               .filter_by(author=current_user)
               .filter(Transport.date > seven_days_ago)
               .order_by(Transport.date.desc(), Transport.transport.asc())
               .all())

    # Felles rekkefølge for grafer:
    transport_order = ['Bus', 'Car', 'Train', 'Bybanen', 'Scooter', 'Ferry', 'Plane', 'Walk']

    # Emissions by category
    emissions_by_transport = (db.session.query(db.func.sum(Transport.co2), Transport.transport)
                              .filter(Transport.date > seven_days_ago)
                              .filter_by(author=current_user)
                              .group_by(Transport.transport)
                              .all())

    emissions_map = {t: float(total) for total, t in emissions_by_transport}
    emission_transport = [emissions_map.get(t, 0) for t in transport_order]

    # Kilometers by category
    kms_by_transport = (db.session.query(db.func.sum(Transport.kms), Transport.transport)
                        .filter(Transport.date > seven_days_ago)
                        .filter_by(author=current_user)
                        .group_by(Transport.transport)
                        .all())

    kms_map = {t: float(kms) for kms, t in kms_by_transport}
    kms_transport = [kms_map.get(t, 0) for t in transport_order]

    # Emissions by date (individual)
    emissions_by_date = (db.session.query(db.func.sum(Transport.co2), Transport.date)
                         .filter(Transport.date > seven_days_ago)
                         .filter_by(author=current_user)
                         .group_by(Transport.date)
                         .order_by(Transport.date.asc())
                         .all())

    over_time_emissions = []
    dates_label = []

    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(float(total))

    # Kms by date (individual)
    kms_by_date = (db.session.query(db.func.sum(Transport.kms), Transport.date)
                   .filter(Transport.date > seven_days_ago)
                   .filter_by(author=current_user)
                   .group_by(Transport.date)
                   .order_by(Transport.date.asc())
                   .all())

    over_time_kms = []
    dates_label = []

    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(float(total))
        
    return render_template(
        'carbon_app/your_data.html', title='your_data', entries=entries,
        emissions_by_transport=emission_transport,
        kms_by_transport=kms_transport,
        over_time_emissions=over_time_emissions,
        over_time_kms=over_time_kms,
        dates_label=dates_label,
        transport_order=transport_order 
    )

# Delete emission
@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))
