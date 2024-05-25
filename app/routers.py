from flask import Blueprint, render_template, request,  redirect, url_for, flash
from werkzeug.utils import secure_filename
from config import Config
from app import db
from app.forms import UploadForm
from app.models import UploadFile
import os


main_dp = Blueprint("main", __name__)


@main_dp.route("/upload", methods=["GET", "POST"])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(file_path)

        upload_file = UploadFile(filename = filename, filepath = file_path)
        db.session.add(upload_file)
        db.session.commit()

        flash("File successfully uploaded!", "success")
        raise redirect(url_for("main.upload"))
    return render_template("upload.html", form = form)