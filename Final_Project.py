
import requests
from bs4 import BeautifulSoup

import pickle
from nltk_helpers import get_sentiments

from imdb import IMDb
from imdb.helpers import sortedSeasons


ia=IMDb()


#tt  whole  0944947
#tt  title  5924366
#tt         6027908
#tt         6027912
#tt         6027914
#tt         6027916
#tt         6027920

series = ia.get_movie('0944947')


ia.update(series, 'episodes')
sumofRating=0
no_of_epsdes=0
rating_avg=[]

for season_nr in sorted(series['episodes']):
    for episode_nr in sorted(series['episodes'][season_nr]):
       episode = series['episodes'][season_nr][episode_nr]
       sumofRating=sumofRating+episode.get('rating')
       print(episode.get('rating'))
       no_of_epsdes=no_of_epsdes+1
    rating_avg.append(sumofRating/no_of_epsdes)
    sumofRating=0  
    no_of_epsdes=0
        
print(rating_avg)







#series = ia.get_movie('5770786')
#ia.update(series, 'episodes')
for season_nr in sorted(series['episodes']):
    for episode_nr in sorted(series['episodes'][season_nr]):
        episode = series['episodes'][season_nr][episode_nr]
        print('episode #%s.%s; rating: %s; votes: %s' %
              (season_nr, episode_nr, episode.get('rating'), episode.get('votes')))




count=0

Season8=['5924366','6027908','6027912','6027914','6027916','6027920']


RawReview=[]
counter=0

for season in Season8:
    movie=ia.get_episode(season)
    reviews=ia.get_movie_reviews(season)
    for review in reviews['data']['reviews']:
         count+=1
         #RawReview.insert(++counter,review['content'])
         RawReview.append(review['content'])
         
         #print(review['content'])
          
         
         
         
#created a pickle file
         
with open('season8.pkl', 'wb') as f:
    pickle.dump(RawReview,f)


#Reading the pickle file

with open('season8.pkl','rb') as f:
    sentis =pickle.load(f)


#sentiment of first one

#print('---------------------',get_sentiments(sentis[0]))
#print('---------------------',get_sentiments(sentis[1]))





#print(reviews['data']['reviews'][0]['content'])

s=0

for senti in sentis:
    s+=1
    print(get_sentiments(senti))

'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.style as style

#build our figure

style.use('seaborn-poster')


fig = plt.figure()

# build axis

ax=fig.add_subplot(111, projection='2d')

from nltk_helpers import split_sentiments

dataX, dataY, dataZ = split_sentiments([get_sentiments(tweet) for tweet in sentis])

#ax.scatter(dataX, dataY, dataZ, color='r',marker='d')

ax.scatter(dataX,  dataZ, color='r',marker='d')




ax.set_xlabel('Negative')
#ax.set_ylabel('Neutral')
ax.set_zlabel('Positive')







'''

'''
import matplotlib.style as style

import matplotlib.pyplot as plt

NUM_VALUES = 8

heights=list(rating_avg)
heights.sort(reverse=True)
print(heights)
style.use('seaborn-poster')
plt.bar(range(1,9), heights[:NUM_VALUES],color='b')
plt.title('GOT Season wise Rating')
plt.ylabel(' Rating')
plt.xlabel('Season Number')
plt.show()

plt.tight_layout()

plt.savefig('Histogram_Plot.png',transparent=True)


plt.show()



'''
import matplotlib.pyplot as plt
import matplotlib.style as style

#build our figure

style.use('seaborn-poster')
#fig = plt.figure()

from nltk_helpers import split_sentiments

dataX, dataY, dataZ = split_sentiments([get_sentiments(tweet) for tweet in sentis])


plt.scatter(dataX,dataZ,color='r',marker='*')

plt.xlabel('Negative')
plt.ylabel('Positive')

plt.title('Positive vs Negative Sentiments For Season 8')

#plt.legend(loc='upper right', shadow=True)

plt.tight_layout()

plt.savefig('Sentimental_2D_Plot.png', transparent=True)
plt.show()
