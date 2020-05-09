from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from regression_model.processing import preprocessors as pp
from regression_model.config import config

import logging


_logger = logging.getLogger(__name__)


price_pipe = Pipeline([
        ("retainFields", pp.retainFields(config.vars_to_retain)),
        ("fillOdom", pp.fillOdom('odometer')),
        ("handleNulls", pp.handleNulls()),
        ("Manu_Encoder", pp.Manu_Encoder('manufacturer')),
        ("Type_Encoder", pp.Type_Encoder('type')),
        ("Trans_Encoder", pp.Trans_Encoder('transmission')),
        ("scaler", StandardScaler()),
        ("Linear_model", LogisticRegression())
    ])
