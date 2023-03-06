import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time



def find_track_id(albums):
    
    time.sleep(0.3)

    df = pd.DataFrame(columns=['track_id', 'album_type', 'track_name','track_duration', 'track_release_date', 'nombre_artist'])

    for album in albums['albums']:
        for item in album['tracks']['items']:
            
            album_type = album['album_type']
            track_ids =item['id'] 
            track_names = item['name']
            track_durations = item['duration_ms']
            nombre_artist = len(item['artists'])
            release_date = album['release_date']
            new_row = {'track_id': track_ids,
                            'album_type': album_type,
                            'track_name': track_names,
                            'track_duration': track_durations,
                            'track_release_date': release_date,
                            'nombre_artist': nombre_artist}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    return df


def division_liste(liste_a_diviser,nombre_element):

    sous_listes = []
    sous_liste_temporaire = []

    for element in liste_a_diviser:
        sous_liste_temporaire.append(element)
        
        if len(sous_liste_temporaire) == nombre_element:
            sous_listes.append(sous_liste_temporaire)
            sous_liste_temporaire = []
            
    if len(sous_liste_temporaire) > 0:
        sous_listes.append(sous_liste_temporaire)

    return sous_listes
