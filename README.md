# Movie-Recommendation-ML
# 🎬 Movie Recommendation System using Machine Learning

## 📌 Project Overview

This project is a **Movie Recommendation System** that recommends similar movies based on the user's favorite movie.

The system uses **Content-Based Filtering** and calculates similarity between movies using:

- TF-IDF Vectorization
- Cosine Similarity


Project Workflow:

```
Movie Dataset

      ↓

Data Preprocessing

      ↓

Feature Selection

      ↓

Text Feature Extraction

      ↓

Cosine Similarity Calculation

      ↓

User Input Movie

      ↓

Recommended Movies
```

---

# 🎯 Objective

To build a recommendation system that suggests movies similar to the user's preferred movie.

Example:

Input:

```
Iron Man
```

Output:

```
Iron Man
Iron Man 2
Iron Man 3
Avengers: Age of Ultron
The Avengers
...
```

---

# 🛠️ Technologies Used

- Python 🐍
- Pandas
- NumPy
- Scikit-Learn


---

# 📂 Project Structure

```
Movie-Recommendation-System/

│
├── Movie Recommendation.py
│
├── movies.csv
│
├── README.md
│
└── requirements.txt

```

---

# 📊 Dataset Information

Dataset contains movie details including:

| Feature | Description |
|-|-|
| title | Movie name |
| genres | Movie genres |
| keywords | Important keywords |
| tagline | Movie tagline |
| cast | Actors |
| director | Movie director |


---

# 🔎 Data Preprocessing

Selected important features:

```
genres

keywords

tagline

cast

director
```


Missing values:

```
Replaced with empty string
```

---

# 🧠 Feature Extraction

Text data cannot directly be used by machine learning models.

Therefore:

## TF-IDF Vectorizer

converts movie information into numerical vectors.


Example:

```
Iron Man
      ↓
Numerical Feature Vector
```

---

# 📐 Similarity Calculation

Cosine Similarity is used to find similarity between movies.

Formula:

```
Similarity = A · B / ||A|| ||B||
```

Higher similarity score means movies are more related.

---

# 🤖 Recommendation System

Steps:

1. User enters movie name

2. System finds closest matching movie

3. Calculates similarity score

4. Sorts movies based on similarity

5. Displays top recommended movies


---

# 🚀 Example Output


Input:

```
Enter your favourite movie name:

Iron Man
```


Output:

```
Movies suggested for you:

1. Iron Man

2. Iron Man 2

3. Iron Man 3

4. Avengers: Age of Ultron

5. The Avengers

6. Captain America: Civil War

7. Ant-Man

8. X-Men
```

---

# ▶️ How to Run Project


Clone repository:

```bash
git clone <your-repository-link>
```


Install dependencies:

```bash
pip install -r requirements.txt
```


Run:

```bash
python "Movie Recommendation.py"
```

---

# 📦 Requirements

```
pandas
numpy
scikit-learn
```

---

# 📌 Machine Learning Workflow

```
Dataset

   ↓

Feature Selection

   ↓

TF-IDF Vectorization

   ↓

Cosine Similarity

   ↓

Recommendation Engine

   ↓

Movie Suggestions
```

---

# 👨‍💻 Author

**Allen Christian**

Machine Learning Project 🚀
