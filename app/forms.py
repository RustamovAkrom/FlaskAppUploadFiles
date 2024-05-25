from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from config import Config
import os


def file_allowed(form, field):
    if field.data:
        filename = field.data.filename
        ext = str(filename).rsplit('.', 1)[1].lower()
        if ext not in Config.ALLOWED_EXTENSIONS:
            raise ValidationError("File type not allowed.")
        
    
class UploadForm(FlaskForm):
    file = FileField("Upload File", validators=[DataRequired(), file_allowed])
    submit = SubmitField("Upload")
    