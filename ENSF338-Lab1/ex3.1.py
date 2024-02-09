import matplotlib.pyplot as plt
import json


file_path = 'ENSF338-Lab1/songdata.json'

with open(file_path, 'r') as file:
    song_data = json.load(file)

#Next 2 lines are from ChatGPT
group1 = [song['tempo'] for song in song_data if song['loudness'] < -8]
group2 = [song['tempo'] for song in song_data if song['loudness'] >= -8]

#Histogram 1
plt.figure(figsize=(10, 6))
plt.hist(group1, bins=30, color='blue', alpha=0.7)
plt.title('Tempo Distribution for Songs with Loudness Below -8')
plt.xlabel('Tempo (BPM)')
plt.ylabel('Number of Songs')
hist1_path = 'ENSF338-Lab1/hist1.png'
plt.savefig(hist1_path)
plt.close()

#Histogram 2
plt.figure(figsize=(10, 6))
plt.hist(group2, bins=30, color='red', alpha=0.7)
plt.title('Tempo Distribution for Songs with Loudness At or Above -8')
plt.xlabel('Tempo (BPM)')
plt.ylabel('Number of Songs')
hist2_path = 'ENSF338-Lab1/hist2.png'
plt.savefig(hist2_path)
plt.close()

hist1_path, hist2_path