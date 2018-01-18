from flask import render_template, request, flash
from cgbeacon_UI import app
from cgbeacon_UI.db_models import Datasets, Variants
from flask_sqlalchemy import SQLAlchemy
import os

@app.route('/', methods=['GET', 'POST'])
def main():

    #Get info from beacon database to populate query form:
    datasets = Datasets.query.all()

    chroms = list(range(1,22))
    chroms.append('X')
    chroms.append('Y')

    method = request.method
    q_datasets = []
    if method == "POST":

        # collect data from form submision:
        qdsets = request.form.getlist('datasetselect')
        qchrom = request.form.get('chromosomeselect')
        qstart = request.form.get('start')
        qallele = request.form.get('var')

        # Optimize query by first checko for chromosomal position, then chromosome, then allele, then dataset
        isInBeacon = Variants.query.filter_by(position=qstart).filter_by(chromosome=qchrom).filter_by(alternate=qallele).filter(Variants.dataset_id.in_(qdsets)).first()

        if isInBeacon:
            return render_template('queryform.html', dsets = datasets, chromosomes = chroms, display_result=(True, 'Variant "'+qallele+'" (chr'+qchrom+':'+qstart+') was found in this Beacon'), selected_dataset= str(qdsets))

        else:
            return render_template('queryform.html', dsets = datasets, chromosomes = chroms, display_result=(False,'Variant "'+qallele+'" (chr'+qchrom+':'+qstart+') was NOT found in this Beacon') , selected_dataset= str(qdsets))
    else:

        return render_template('queryform.html', dsets = datasets, chromosomes = chroms, display_result=(False, ''), selected_dataset= str(q_datasets))


@app.route('/contacts/')
def contacts():
    return render_template("contacts.html")
