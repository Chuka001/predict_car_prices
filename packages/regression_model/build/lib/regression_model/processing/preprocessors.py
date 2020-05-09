import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class retainFields(BaseEstimator, TransformerMixin):
    def __init__(self, variables):
        self.variables = variables
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X[self.variables]
        return X
    
        
class handleNulls(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables= variables
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X = X.fillna(method='ffill')
        X = X.fillna(method='bfill')   
        return X

class fillOdom(BaseEstimator, TransformerMixin):
    def __init__(self, variable=None):
        self.variable = variable
    
    def fit(self, X,y=None):
        self.odom_mode = X[self.variable].mode()[0]
        return self
    
    def transform(self, X):
        X=X.copy()
        
        X[self.variable] = X[self.variable].fillna(self.odom_mode)
        return X
    
class Manu_Encoder(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables= variables
        
    def fit(self, X,y=None):
        self.man_dict = {}
        self.a = X[self.variables].unique()
        for i in range(len(self.a)):
            self.man_dict[self.a[i]]=i 
               
        return self
    
    def transform(self, X):
        X = X.copy()
        
        X[self.variables] = X[self.variables].replace(self.man_dict)     
        return X

class Trans_Encoder(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables= variables
        
    def fit(self, X,y=None):
        self.trans_dict = {}
        self.a = X[self.variables].unique()
        for i in range(len(self.a)):
            self.trans_dict[self.a[i]]=i 
               
        return self
    
    def transform(self, X):
        X = X.copy()
        
        X[self.variables] = X[self.variables].replace(self.trans_dict)     
        return X

class Type_Encoder(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables= variables
        
    def fit(self, X,y=None):
        self.type_dict = {}
        self.a = X[self.variables].unique()
        for i in range(len(self.a)):
            self.type_dict[self.a[i]]=i 
              
        return self
    
    def transform(self, X):
        X = X.copy()
         
        X[self.variables] = X[self.variables].replace(self.type_dict)     
        return X
    