from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    budget = IntegerField('Budget', validators=[DataRequired()])
    runtime = IntegerField('Runtime', validators=[DataRequired()])
    release_year = IntegerField('Release year', validators=[DataRequired()])
    part_of_series = IntegerField('Is the movie a part of a series? If yes, enter 1. If no, enter 0.', validators=[DataRequired(), NumberRange(min=0, max=1)])
    has_homepage = IntegerField('Does the movie have a homepage? If yes, enter 1. If no, enter 0.', validators=[DataRequired(), NumberRange(min=0, max=1)])
    num_genres = IntegerField('How many different genres would you say that the film represents?', validators=[DataRequired(), NumberRange(min=0, max=1)])
    num_casts = IntegerField('How many actors were casted for this movie?', validators=[DataRequired(), NumberRange(min=1)])
    num_crew = IntegerField("How many people was part of the film's crew?", validators=[DataRequired(), NumberRange(min=1)])
    is_english = IntegerField('Is the original language of the film English? If yes, enter 1. If no, enter 0.', validators=[DataRequired(), NumberRange(min=0, max=1)])
    num_prod_comp = IntegerField('How many production companies were involved in making the film?', validators=[DataRequired(), NumberRange(min=1)])
    num_production_countries = IntegerField('How many countries were the film produced in?', validators=[DataRequired(), NumberRange(min=1)])

    submit = SubmitField('Submit')
