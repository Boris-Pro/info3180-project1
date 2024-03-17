"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app.models import Property
from app.forms import PropertyForm
from .models import db
from flask import send_from_directory

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

# @app.route('/properties/create/', methods=['GET'])
# def create_property_form():
#     form = PropertyForm()
#     return render_template('create_property.html', form=form)


@app.route('/properties/create/', methods=['GET', 'POST'])
def create_property():
    form = PropertyForm()

    if request.method == 'POST':

        if form.validate_on_submit():
        # Retrieve data from the form
            property_title = form.property_title.data
            description = form.description.data
            no_of_rooms = form.no_of_rooms.data
            no_of_bathrooms = form.no_of_bathrooms.data
            price = form.price.data
            property_type = form.property_type.data
            location = form.location.data
            #image_filename = None  # Handle image upload if necessary
            image = form.image.data
            # image_filename = secure_filename(image.image_filename)
            image_filename = secure_filename(form.image.data.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
            flash('Property added successfully!', 'success')
            # Create a new Property object
            new_property = Property(property_title=property_title,
                                    description=description,
                                    no_of_rooms=no_of_rooms,
                                    no_of_bathrooms=no_of_bathrooms,
                                    price=price,
                                    property_type=property_type,
                                    location=location,
                                    image_filename=image_filename)

            # Add the new property to the database session
            db.session.add(new_property)
            db.session.commit()
            return redirect(url_for('properties'))
        flash_errors(form)
        
        # Redirect to the properties page or any other page
        

    return render_template('create_property.html', form=form)

# @app.route('/properties2')
# def list_properties():
#     properties = Property.query.all()
#     for prop in properties:
#         prop.image_url = url_for('send_image', filename=prop.image_filename)
#     return render_template('properties2.html', properties=properties)

@app.route('/properties')
def properties():
    # Logic to fetch all properties from the database
    properties = Property.query.all()
    for prop in properties:
        prop.image_url = url_for('send_image', filename=prop.image_filename)
    return render_template('properties.html', properties=properties)

@app.route('/property/<int:property_id>')
def property(property_id):
    # Logic to fetch the property with the given ID from the database
    property = Property.query.get_or_404(property_id)
    property.image_url = url_for('send_image', filename=property.image_filename)
    return render_template('property.html', property=property)

def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

@app.route('/uploads/<filename>')
def send_image(filename):
    # return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    uploads_dir = os.path.join(os.getcwd(), 'uploads')
    return send_from_directory(uploads_dir, filename)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
