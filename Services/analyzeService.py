import pandas as pd
from pandas.core.frame import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# увеличение максимальной глубины рекурсии

#тренировка модели
def train(df: DataFrame) -> tuple:    
    df = df.fillna(0)

    data = df.drop(['condition'], axis=1)

    # кластеризация
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data.iloc[:, :-1])
    clusters = kmeans.predict(data.iloc[:, :-1])

    # выбор значимых признаков (нахидим ключевые параметры)
    cumulative_variance_ratio = 0
    n_components = 0
    while cumulative_variance_ratio < 0.9:
        n_components += 1
        lda = LDA(n_components=n_components)
        lda.fit(data.iloc[:, :-1], clusters)
        #lda.fit(data.iloc[:, :-1], clusters)
        cumulative_variance_ratio = lda.explained_variance_ratio_.cumsum()[-1]
    influential_features = data.columns[:-1][np.abs(lda.coef_[0]).argsort()[-5:][::-1]]

    # линейные дискриминантные уравнения
    n_components = min(len(influential_features), len(set(clusters)) - 1)
    lda = LDA(n_components=n_components)
    lda.fit(data[influential_features], clusters)
    coefficients = pd.DataFrame(lda.coef_, columns=influential_features)
    bias = lda.intercept_

    return influential_features, coefficients, bias



def get_train_data(df:DataFrame) -> tuple:
    sys.setrecursionlimit(1000000)

    influential_features, coefficients, bias = train(df)
    dict_ = {"columns":influential_features.to_list(), "coefficients":coefficients.to_dict(), "bias": bias.tolist()}
    
        #это вводные
    cooperation = df['condition']
    stable = np.where((coefficients.loc[0] * df[influential_features]).sum(axis=1) + bias[0] > cooperation, 1, 0)
    medium = np.where((coefficients.loc[1] * df[influential_features]).sum(axis=1) + bias[1] > cooperation, 1, 0)
    severe = np.where((coefficients.loc[2] * df[influential_features]).sum(axis=1) + bias[2] > cooperation, 1, 0)

    # сравнение с фактическими значениями - запись в бд:

    df['predicted_state'] = np.where(stable == 1, 'stable',
                                np.where(medium == 1, 'medium', 'severe'))
    actual = np.where(df['condition'] == 0, 'stable',
                                np.where(df['condition'] == 1, 'medium', 'severe'))

    accuracy = (df['predicted_state'] == actual).sum() / len(df)
    
    return dict_, accuracy

def make_analyze(pat, coefficients, bias) -> int:
    if ((coefficients.loc['0'] * pat).sum() + bias[0]) < ((coefficients.loc['2'] * pat).sum() + bias[2]) and ((coefficients.loc['0'] * pat).sum() + bias[0]) < ((coefficients.loc['1'] * pat).sum() + bias[1]):
        return 0
    elif ((coefficients.loc['2'] * pat).sum() + bias[2]) > ((coefficients.loc['1'] * pat).sum() + bias[1]):
        return 1
    else:
        return 2