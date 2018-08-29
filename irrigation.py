from sklearn.cross_decomposition import PLSRegression
import pandas as pd

X = pd.read_csv("dataset/input.csv")
Y = pd.read_csv("dataset/output.csv")