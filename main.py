import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv("movies.csv")

# Clean genres
df["genres"] = df["genres"].str.replace("|", " ", regex=False)

# TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df["genres"])

# Similarity
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)


# ---------- RECOMMEND FUNCTION ----------
def recommend(movie_name):
    movie_name = movie_name.lower()

    # Find matches
    matches = df[df["title"].str.lower().str.contains(movie_name)]

    if matches.empty:
        return ["Movie not found 😢"]

    # 👉 Pick first match automatically (no input())
    index = matches.index[0]

    # Get similarity scores
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Top 10 recommendations
    top_movies = scores[1:11]

    results = []
    for i in top_movies:
        title = df.iloc[i[0]]["title"]
        score = round(i[1], 2)
        results.append(f"{title} (Score: {score})")

    return results