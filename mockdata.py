import random

import numpy as np
import pandas as pd

demographicSegments = pd.DataFrame(
    {
        "Name": ["age_21-24", "age_25-29", "age_30-34", "age_35-39", "age_40-44", "gender_male"],
        "Description": ["Age Range 21-24", "Age Range 25-29", "Age Range 30-34", "Age Range 35-39", "Age Range 40-44", "Gender Male"],
        "1st Party": [True, True, True, True, False, False],
        "Users": [[random.randint(0, 5000) for _ in range(30)] for _ in range(6)],
        "Total": [10000, 20000, 15000, 20000, 20000, 25000]
    }
)

interestSegments = pd.DataFrame(
    {
        "Name": ["interest_sports_baseball", "interest_sports_basketball", "interest_sports_cricket"],
        "Description": ["Interest - Sports - Baseball", "Interest - Sports - Basketball", "Interest	- Sports - Cricket"],
        "1st Party": [True, True, True],
        "Users": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
        "Total": [10000, 20000, 15000]
    }
)

def generateInsightsDf(segments):
    segmentsInsightsDf = pd.DataFrame(np.random.randn(20, len(segments)), columns=segments)
    return segmentsInsightsDf

def getUsersForSegments(segments):
    return dict((segment, random.randint(0, 5000)) for segment in segments)