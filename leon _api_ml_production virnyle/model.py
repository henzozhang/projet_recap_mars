import pickle
import pandas as pd
import xgboost as xgb

model = pickle.load(open('pipe_xg_classifier.pkl', 'rb'))


# # cols = ['state', 'bankstate', 'term', 'noemp', 'newexist', 'createjob',
#        'retainedjob', 'franchisecode', 'urbanrural', 'revlinecr', 'lowdoc', 'grappv']

# value = [18, 'female', 4, 'no', 'northeast', 'obesity']
cols =['album_type', 'track_duration', 'nombre_artist', 'track_release_month',
       'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'time_signature', 'pays_du_producteur']

def predict(list_values=None):
    to_predict = dict(zip(cols, list_values))
    to_predict = pd.DataFrame(to_predict, index=[0])
    return model.predict(to_predict)[0]