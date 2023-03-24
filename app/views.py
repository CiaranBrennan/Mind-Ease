from flask import render_template, flash, redirect
from app import app
from app import db, models
import md5
from forms import signIn, bookApp, editApp
#Declares and assigns the variable used to track the logged in user
currentUser = ""

#Calls this function when on the root page of the system
@app.route('/', methods=['GET', 'POST'])
def logIn():
    #Checks whether the user is logged in already
        #& directs them to the module page if so
    global currentUser
    if currentUser != "":
        return redirect('/modules')

    #Allows the data entered into the form to be accessed
    form = signIn()
    #Once the user has tapped sign in,
        #the entered data is retrieved
    if form.validate_on_submit():
        enteredPass = md5.new()
        user = form.username.data
        #The password is stored as a hash, hence why the
            #entered password is hashed before being compared
        enteredPass.update(form.password.data)
        #The database of students is searched to see whether
            #the entered details match any of the records
        for users in models.Users.query.all():
            if users.username == user\
                and users.password == enteredPass.hexdigest():
                #If there is a match, currentUser is updated
                    #and the user is redirected to modules
                currentUser = users.username
                return redirect('/modules')
        #If a match can't be found, an error is shown
        flash("Username or password incorrect. Please try again.")
    #This displays the contents of singIn.html
    return render_template('signIn.html',\
        title='Sign In', form=form, username=currentUser)

@app.route('/logOut')
def logOut():
    global currentUser
    currentUser = ""
    return redirect("/")

@app.route('/modules')
def showModules():
    global currentUser
    if currentUser == "":
        return redirect('/')
    modules=[]
    students=models.Users.query.filter_by(username=currentUser).all()
    modules = students[0].modules
    return render_template('modules.html', title='Your Modules', moduleList=modules, username=currentUser)

@app.route('/appointments')
def showAppointment():
    global currentUser
    if currentUser == "":
        return redirect('/')

    upcomingAppoint = []
    for appointment in models.Appointments.query.all():
        if appointment.student == currentUser:
            upcomingAppoint = appointment
            break

    return render_template('appointments.html', title='Your Appointments', appointment=upcomingAppoint, username=currentUser)

@app.route('/bookAppointment', methods=['GET', 'POST'])
def bookAppointment():
    global currentUser
    if currentUser == "":
        return redirect('/')

    form = bookApp()
    if form.validate_on_submit():
        #Takes the user's chosen date and time when they tap book
        appDate = form.appDate.data
        appTime = form.appTime.data
        #Adds the appointment to the database
        command = models.Appointments(student=currentUser,\
            date=appDate, time=appTime)
        try:
            db.session.add(command)
            db.session.commit()
            return redirect('/appointments')
        except:
            flash("Booking failed. Please try again")
    return render_template('bookAppointment.html',\
        title='Book an Appointment', form=form, username=currentUser)

@app.route('/editAppointment', methods=['GET', 'POST'])
def editAppointment():
    global currentUser
    if currentUser == "":
        return redirect('/')

    form = editApp()
    if form.validate_on_submit():
        appDate = form.appDate.data
        appTime = form.appTime.data
        try:
            for appointment in models.Appointments.query.all():
                if appointment.student == currentUser:
                    appointment.date=appDate
                    appointment.time=appTime
                    db.session.commit()
                    break
            return redirect('/appointments')
        except:
            flash("Booking failed. Please try again")
    return render_template('editAppointment.html',\
        title='Edit an Appointment', form=form, username=currentUser)
