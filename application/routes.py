#Marius Saunders
#QA Project 1
#Frankendama Sharing

#Imports the needed modules 
from flask import redirect, url_for, request, render_template
from . import app
from . import db
from .models import Company, Frankendama
from .forms import FrankForm


#Home route, is the main page.
#Displays all Frankendama entries with thier companies
@app.route('/')
@app.route('/home')
def home():

    franks = Frankendama.query.all()
    comps = Company.query.all()
    
    return render_template("home.html", franks=franks, comps=comps)


#Create route, is the page for creating a new homepage entry
@app.route("/create", methods=["GET", "POST"]) 
def create():
    
    #Accesses the form to create a new frankendama
    form = FrankForm()

    if request.method == 'POST':
        new_frank = Frankendama(
            title=form.title.data,
            description=form.description.data,
            tama=form.tama.data,
            sarado=form.sarado.data,
            sword=form.sword.data,
            string=form.string.data,
            bearing=form.bearing.data.lower().title()
        )

        db.session.add(new_frank)
        db.session.commit()
    
        #Takes the data from the form and splits it via commas
        comps = form.companies.data
        comps_used = comps.split(",")

        #Adds all companies seperated into the Company table
        for i in range(0, len(comps_used)):

            entry = comps_used[i]

            new_comp = Company(name=entry, frankendama_id=new_frank.id)

            db.session.add(new_comp)
            db.session.commit()

        #Upon completion, returns to home page to view new entry
        return redirect(url_for("home"))
    
    else:

        return render_template("create.html", form=form)


#Update route, used to change the contents of an entry on the home page.
@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):

    #Accesses the form to update the required entry
    frank = Frankendama.query.get(id)
    form = FrankForm()


    #Updates table row contents
    if form.validate_on_submit():
        
        frank.title=form.title.data
        frank.description=form.description.data
        frank.tama=form.tama.data
        frank.sarado=form.sarado.data
        frank.sword=form.sword.data
        frank.string=form.string.data
        frank.bearing=form.bearing.data
                
        db.session.add(frank)  
        db.session.commit()

        #Splits companies with commas
        comps = form.companies.data
        comps_used = comps.split(",")

        #Query to find all companies with a specific frank id
        all_comps = Company.query.filter_by(frankendama_id = id).all()

        #Deletes all of the found entries
        for entry in all_comps:
            db.session.delete(entry)

        #Creates new entries
        for i in range(0, len(comps_used)):

            new_entry = comps_used[i]
            new_comp = Company(name=new_entry, frankendama_id=id)

            db.session.add(new_comp)
            db.session.commit()

        #Upon completion, returns to home page to view updated entry
        return redirect(url_for("home"))
    
    else:

        return render_template("create.html", form=form)


#Delete route, used to delete a home page table entry
@app.route("/delete/<int:id>")
def delete(id):

    #Creates the two needed table queries
    frank = Frankendama.query.get(id)
    comps = Company.query.all()

    #Deletes the single frank entry
    db.session.delete(frank)
    
    #Iterates through Company table to removes all entries with specific foreign key id
    for entry in comps:
        if entry.frankendama_id == id:
            db.session.delete(entry)

    db.session.commit()

    #Returns to homepage to view updated table
    return redirect(url_for("home")) 

