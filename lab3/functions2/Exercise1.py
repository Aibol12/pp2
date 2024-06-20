movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
def imdb(movie):
    if(movie["imdb"] > 5.5):
        return True
    else: return False
#2
def subImdb(movie):
    if(imdb(movie)):
        print(movie["name"])
        print(movie["imdb"])
        print(movie["category"])
        print()
#3
def isCategory(movie, category):
    if(movie["category"] == category):
        print(movie["name"])
#4
def averageImdb(movies):
    average = 0
    cnt = len(movies)
    for movie in movies:
        average += movie["imdb"]
    return average / cnt
#5
def averageByCategory(movies, category):
    cnt = 0
    average = 0
    for movie in movies:
        if(movie["category"] == category):
            average += movie["imdb"]
            cnt += 1
    return average / cnt