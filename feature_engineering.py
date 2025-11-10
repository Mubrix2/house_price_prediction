from sklearn.base import BaseEstimator, TransformerMixin
from datetime import datetime

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        current_year = datetime.now().year
        X['House_Age'] = current_year - X['Year_Built']
        X['Lot_per_SqFt'] = X['Lot_Area'] / X['SqFt']

        return X[["House_Age", "Lot_per_SqFt", "Type", "Garage", "Total_rooms"]]