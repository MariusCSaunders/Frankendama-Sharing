from flask import redirect, url_for, request, render_template
from . import app
from . import db
from .models import Company, Frankendama
from .forms import FrankForm


@app.route('/')
@app.route('/home')
def home():

    franks = Frankendama.query.all()
    comps = Company.query.all()
    
    return render_template("home.html", franks=franks, comps=comps)


@app.route("/create", methods=["GET", "POST"]) 
def create():
    
    form = FrankForm()

    if request.method == 'POST':
        new_frank = Frankendama(
            title=form.title.data,
            description=form.description.data,
            tama=form.tama.data,
            sarado=form.sarado.data,
            sword=form.sword.data,
            string=form.string.data,
            bearing=form.bearing.data,
        )

        db.session.add(new_frank)
        db.session.commit()
    
        comps = form.companies.data
        comps_used = comps.split(",")

        

        for i in range(0, len(comps_used)):

            entry = comps_used[i]

            new_comp = Company(name=entry, frankendama_id=new_frank.id)

            db.session.add(new_comp)
            db.session.commit()


        return redirect(url_for("home"))
    
    else:

        return render_template("create.html", form=form)

@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):

    frank = Frankendama.query.get(id)
    form = FrankForm()

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

        comps = form.companies.data
        comps_used = comps.split(",")

        all_comps = Company.query.filter_by(frankendama_id = id).all()

        for entry in all_comps:
            
            db.session.delete(entry)

        for i in range(0, len(comps_used)):

            new_entry = comps_used[i]
            new_comp = Company(name=new_entry, frankendama_id=id)

            db.session.add(new_comp)
            db.session.commit()

        return redirect(url_for("home"))
    
    else:

        return render_template("create.html", form=form)


@app.route("/delete/<int:id>")
def delete(id):

    frank = Frankendama.query.get(id)
    comps = Company.query.all()

    db.session.delete(frank)
    
    for entry in comps:
        if entry.frankendama_id == id:
            db.session.delete(entry)

    db.session.commit()

    return redirect(url_for("home")) 

