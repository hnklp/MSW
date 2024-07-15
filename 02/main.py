import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("thecure_discography.csv")

#preformatovani z yyyy-mm-dd na yyyy
data['album_release_year'] = pd.to_datetime(data['album_release_year']).dt.year
#ziskani unikatnich roku
years = data['album_release_year'].unique()

print(data.album_release_year)

#Popularita vs tonina
plt.bar(data['key'], data['track_popularity'])
plt.title('Vztah mezi tóninou a popularitou')
plt.xlabel('Tónina')
plt.ylabel('Popularita v %')
plt.show()

#Histogram delky skladeb
plt.hist(data['duration_ms'] / (1000 * 60), bins=15, edgecolor='black')
plt.title('Histogram délky skladeb')
plt.xlabel('Délka (minuty)')
plt.ylabel('Počet skladeb')
plt.show()

#Podil instrumentalu
instrumental_count = data[data['instrumentalness'] > 0.5].shape[0]
vocal_count = data.shape[0] - instrumental_count

labels = ['Instrumentální', 'S vokály']
sizes = [instrumental_count, vocal_count]
colors = ['lightblue', 'lightcoral']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Podíl instrumentálních skladeb')
plt.axis('equal')
plt.show()

#hlasitost x rok vydani
inverted_loudness = -data['loudness']
plt.bar(data['album_release_year'], inverted_loudness, width=0.8)
plt.title('Vztah mezi hlasitostí a rokem vydání')
plt.xlabel('Rok vydání')
plt.ylabel('Hlasitost v dB')
plt.xticks(years, rotation=45)
plt.show()

#popularita vs tanecnost
plt.scatter(data['danceability'], data['track_popularity'], alpha=0.7)
plt.title('Vztah mezi tanečností a popularitou')
plt.xlabel('Tanečnost')
plt.ylabel('Popularita')
plt.show()
