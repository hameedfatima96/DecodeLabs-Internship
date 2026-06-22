import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dataset
data = {
    "Course": [
        "Python for Beginners",
        "Machine Learning Masterclass",
        "Deep Learning Fundamentals",
        "Data Science Bootcamp",
        "Web Development",
        "Generative AI Course"
    ],
    "Skills": [
        "python programming",
        "python machine learning ai",
        "ai neural networks",
        "python data science",
        "html css javascript",
        "ai llm prompt engineering"
    ],
    "Item": [
        "Python for Beginners",
        "Gardening Guide",
        "Movie Club",
        "Book Club",
        "Travel Guide",
        "Fitness Program"
    ],
    "Tags": [
        "technology coding python programming",
        "gardening plants nature",
        "movies cinema entertainment",
        "books reading literature",
        "travel adventure tourism",
        "fitness health gym"
    ]

}

df = pd.DataFrame(data)

# User input
interests = input(
    "Enter your interests (comma separated): "
).lower()

user_profile = " ".join(
    [x.strip() for x in interests.split(",")]
)

# Add user profile
new_row = pd.DataFrame({
    "Course": ["User"],
    "Skills": [user_profile]
})

df = pd.concat([df, new_row], ignore_index=True)

# Convert text into vectors
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(df["Skills"])

# Calculate similarity
similarity = cosine_similarity(vectors)

# Similarity scores with user profile
scores = similarity[-1][:-1]

recommendations = sorted(
    zip(df["Course"][:-1], scores),
    key=lambda x: x[1],
    reverse=True
)

# Display recommendations
print("\nTop Recommendations:\n")

for course, score in recommendations:
    if score > 0:
        print(
            f"{course} "
            f"({round(score * 100, 2)}% match)"
        )