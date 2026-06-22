# Smart AI Recommendation System

## Overview
This project is a simple AI recommendation system that suggests items based on a user's interests. The user enters their preferences, and the system finds and displays the most relevant recommendations.

## Features
- Takes user interests as input
- Matches interests with available items
- Shows recommendations with match scores
- Uses content-based filtering and cosine similarity

## Technologies Used
- Python
- Pandas
- Scikit-learn

## How It Works
1. Enter your interests (comma-separated).
2. The system compares your interests with item categories.
3. It calculates similarity scores.
4. The best matches are displayed as recommendations.

## Example

**Input**
```text
gardening, movies, reading books
```

**Output**
```text
Top Recommendations:
Book Lovers Club (57.73% match)
Top Movie Recommendations (40.82% match)
Gardening Guide (40.82% match)
```

## Run the Project
```bash
pip install pandas scikit-learn
python "AI Recommendation.py"
```

## Author
Fatima Hameed
