from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template('base.html')

@views.route("/kidney")
def kidney():
    return render_template(r'kidney_index.html')

@views.route("/kidney_form")
def kidney_form():
    return render_template(r'kidney.html')

@views.route("/liver")
def liver():
    return render_template(r'liver_index.html')

@views.route("/liver_form")
def liver_form():
    return render_template(r'liver.html')

@views.route("/heart")
def heart():
    return render_template(r'heart_index.html')

@views.route("/heart_form")
def heart_form():
    return render_template(r'heart.html')

@views.route("/stroke")
def stroke():
    return render_template(r'stroke_index.html')

@views.route("/stroke_form")
def stroke_form():
    return render_template(r'stroke.html')

@views.route("/diabete")
def diabete():
    return render_template(r'diabete_index.html')

@views.route("/diabete_form")
def diabete_form():
    return render_template(r'diabete.html')

@views.route("/pneumonia")
def pneumonia():
    return render_template(r'pneumonia_index.html')

@views.route("/pneumonia_form")
def pneumonia_form():
    return render_template(r'pneumonia.html')

@views.route("/maralia")
def maralia():
    return render_template(r'maralia_index.html')

@views.route("/maralia_form")
def maralia_form():
     return render_template(r'maralia.html')

@views.route("/skin")
def skin():
    return render_template(r'skin_index.html')

@views.route("/skin_form")
def skin_form():
    return render_template(r'skin.html')

@views.route("/oclur")
def oral():
    return render_template(r'oclur_index.html')

@views.route("/oclur_form")
def oral_form():
    return render_template(r'oclur.html')

@views.route("/DR")
def DR():
    return render_template(r'dr_index.html')

@views.route("/dr_form")
def dr_form():
    return render_template(r'dr.html')


@views.route("/octa")
def octa_index():
    return render_template(r'oct_index.html')

@views.route("/octa_form")
def octa_form():
    return render_template(r'oct.html')


@views.route("/oral")
def oral_index():
    return render_template(r'r_index.html')

@views.route("/oral_form")
def oral_form_view():
    return render_template(r'r.html')
















