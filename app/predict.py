import numpy as np
import pandas as pd
import joblib

#######
## Get the model trained in the notebook
# `../nbs/1.0-asl-train_model.ipynb`
#######

model = joblib.load('models/second_model.joblib')


def preprocess(data):
    """
    Returns the features entered by the user in the web form.
    To simplify, we set a bunch of default values.
            For bools and ints, use the most frequent value
            For floats, use the median value
    Note that this represent some major assumptions that you'd
    not want to make in real life. If you want to use default
    values for some features then you'll have to think more
    carefully about what they should be.
    F.ex. if the user doesn't provide a value for BMI,
    then one could use a value that makes more sense than
    below. For example, the mean for the given gender would
    at least be a bit more correct.

    Having _dynamic defaults_ is important. And of course, if
    relevant, getting some of the features without asking the user.
    E.g. if the user is logged in and you can pull information
    form a user profile. Or if you can compute or obtain the information
    thorugh other means (e.g. user location if shared etc).
    """

    feature_values = {
        'budget' : 0,
        'popularity' : 0,
        'runtime' : 0,
        'part_of_series' : 0,
        'has_homepage' : 0,
        'num_genres' : 0,
        'num_casts' : 0,
        'num_crew' : 0,
        'is_english' : 0,
        'num_prod_comp' : 0,
        'num_production_countries' : 0,
        'release_month' : 5,
        'release_day' : 3,
        'release_year' : 0,
        'day_of_week': 3,
    }

    # Parse the form inputs and return the defaults updated with values entered.

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values


#######
## Now we can predict with the trained model:
#######


def predict(data):
    """
    If debug, print various useful info to the terminal.
    """

    # Store the data in an array in the correct order:

    column_order = ['budget', 'popularity', 'runtime', 'part_of_series', 'has_homepage', 'num_genres', 'num_casts',
                    'num_crew','is_english', 'num_prod_comp', 'num_production_countries', 'release_month',
                    'release_day', 'release_year', 'day_of_week']

    data = np.array([data[feature] for feature in column_order], dtype=object)

    # NB: In this case we didn't do any preprocessing of the data before
    # training our random forest model (see the notebool `nbs/1.0-asl-train_model.ipynb`).
    # If you plan to feed the training data through a preprocessing pipeline in your
    # own work, make sure you do the same to the data entered by the user before
    # predicting with the trained model. This can be achieved by saving an entire
    # sckikit-learn pipeline, for example using joblib as in the notebook.

    pred = model.predict(data.reshape(1, -1))

    #uncertainty = model.predict_proba(data.reshape(1, -1))

    return pred, #uncertainty


def postprocess(pred):
    """
    Apply postprocessing to the prediction. E.g. validate the output value, add
    additional information etc.
    """

    #pred, uncertainty = prediction

    # Validate. As an example, if the output is an int, check that it is positive.
    try:
        int(pred[0]) > 0
    except:
        pass

    # Make strings
    pred = str(pred[0])
   # uncertainty = str(uncertainty[0])

    # Return
    return_dict = {'pred': pred} #'uncertainty': uncertainty}

    return return_dict
