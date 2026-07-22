# 🎵 Music Recommender Simulation

## Project Summary

This project simulates a lightweight music recommender that turns song attributes and a user taste profile into ranked suggestions. It is inspired by real systems such as Spotify and YouTube, which try to predict what a listener will enjoy next by combining signals from behavior and from the content itself. In this version, the recommender uses a simple weighted score based on features such as genre, mood, energy, and acousticness.

---

## How The System Works

Real-world recommendation systems look at both user behavior and the characteristics of the items being recommended. Platforms such as Spotify and YouTube use signals like likes, skips, playlist saves, watch time, and song attributes to estimate what someone is likely to enjoy next. This simulation uses a simpler content-based approach: it will score songs by how closely they match a user's preferred genre, mood, energy level, and acousticness, then rank the songs from strongest match to weakest.

The design will focus on a small set of features that are easy to interpret:

- Song features: genre, mood, energy, tempo_bpm, valence, danceability, and acousticness
- UserProfile features: favorite_genre, favorite_mood, target_energy, and likes_acoustic

The scoring rule will reward songs that align with the user's stated preferences, while the ranking rule will order the full list so the best matches appear first.

### Algorithm Recipe

For this version of the recommender, I plan to use a simple weighted content-based scoring recipe:

- +2.0 points for a genre match
- +1.0 point for a mood match
- +0.0 to +1.0 points for energy similarity, based on how close the song's energy is to the user's target energy
- +0.5 points when acousticness matches the user's preference, such as preferring lower acousticness for energetic songs or higher acousticness for calm songs

The system will score every song in the catalog, sort the results from highest to lowest, and return the top recommendations. This keeps the logic easy to explain while still giving a meaningful ranking.

### Planned User Profile

A sample user profile for this simulation could be a dictionary such as:

```python
user_profile = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.8,
    "likes_acoustic": False,
}
```

This profile is intentionally specific so the system can distinguish between upbeat, bright songs and more mellow or acoustic ones. It also reflects the current dataset well, since the catalog includes several pop, happy, and energetic tracks that should be easy to compare.

### Expected Biases

This design may over-prioritize obvious genre and mood matches, which could cause the system to miss strong songs that are a good fit for the user's energy or vibe but fall outside the preferred genre. It may also favor songs that are easy to label with the current features and could under-rank more nuanced tracks that are harder to describe with this small set of attributes.

---

## Research Summary: How Major Platforms Predict What Users Will Love Next

Real streaming platforms do not rely on one single rule. They usually combine several signals:

- Spotify: Spotify uses listening history, skips, saves, playlists, repeat behavior, and audio features such as tempo, danceability, and mood. It blends collaborative filtering with content-based signals so it can recommend both familiar artists and new music.
- YouTube: YouTube focuses heavily on behavior signals such as clicks, watch time, replays, likes, dislikes, and completion rate. It ranks videos by predicted satisfaction and watch duration, not just by topic labels.
- TikTok: TikTok uses rapid engagement signals such as watch time, rewatches, shares, follows, and completion to quickly identify what a user may enjoy next.

The main idea is the same across these platforms: they build a model that predicts future engagement from past behavior and from the characteristics of the item being recommended.

---

## Helpful Prompt for Comparing Recommendation Approaches

Here is a strong prompt you can use for the assignment or for a class discussion:

```text
Compare collaborative filtering and content-based filtering in a music recommender system.
Explain the difference in simple terms:
- Collaborative filtering uses other users' behavior, such as what similar listeners play, save, skip, or replay.
- Content-based filtering uses song attributes, such as genre, mood, energy, tempo, and acousticness.
Give one example of each approach, list one strength and one weakness for each, and explain one bias risk for each method.
```

This prompt is useful because it pushes the model to clearly separate behavior-based recommendations from attribute-based recommendations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Example output from the default pop/happy profile:

```text
Loaded songs: 17

Top recommendations:

1. Sunrise City
   Score: 4.48
   Why: genre match (+2.0); mood match (+1.0); energy similarity (+0.98); acoustic preference (+0.5)

2. Gym Hero
   Score: 3.37
   Why: genre match (+2.0); energy similarity (+0.87); acoustic preference (+0.5)

3. Rooftop Lights
   Score: 1.96
   Why: mood match (+1.0); energy similarity (+0.96)

4. Night Drive Loop
   Score: 1.45
   Why: energy similarity (+0.95); acoustic preference (+0.5)

5. Velvet Skyline
   Score: 1.42
   Why: energy similarity (+0.92); acoustic preference (+0.5)
```

---

## Experiments You Tried

You can document experiments such as:

- Changing the weight on genre versus mood
- Adding or removing features such as tempo or valence
- Testing different user profiles, such as calm listeners versus energetic listeners

---

## Stress Test: Diverse Profiles

The recommender was run with three distinct user preference profiles to surface how the scoring behaves across different listener types.

### High-Energy Pop

```text
Loaded songs: 17

=== Profile: High-Energy Pop ===
1. Sunrise City
   Score: 4.42
   Why: genre match (+2.0); mood match (+1.0); energy similarity (+0.92); acoustic preference (+0.5)
2. Gym Hero
   Score: 3.47
   Why: genre match (+2.0); energy similarity (+0.97); acoustic preference (+0.5)
3. Rooftop Lights
   Score: 1.86
   Why: mood match (+1.0); energy similarity (+0.86)
4. Neon District
   Score: 1.50
   Why: energy similarity (+1.00); acoustic preference (+0.5)
5. Storm Runner
   Score: 1.49
   Why: energy similarity (+0.99); acoustic preference (+0.5)
```

### Chill Lofi

```text
=== Profile: Chill Lofi ===
1. Library Rain
   Score: 4.50
   Why: genre match (+2.0); mood match (+1.0); energy similarity (+1.00); acoustic preference (+0.5)
2. Midnight Coding
   Score: 4.43
   Why: genre match (+2.0); mood match (+1.0); energy similarity (+0.93); acoustic preference (+0.5)
3. Focus Flow
   Score: 3.45
   Why: genre match (+2.0); energy similarity (+0.95); acoustic preference (+0.5)
4. Spacewalk Thoughts
   Score: 2.43
   Why: mood match (+1.0); energy similarity (+0.93); acoustic preference (+0.5)
5. Coffee Shop Stories
   Score: 1.48
   Why: energy similarity (+0.98); acoustic preference (+0.5)
```

### Deep Intense Rock

```text
=== Profile: Deep Intense Rock ===
1. Storm Runner
   Score: 4.49
   Why: genre match (+2.0); mood match (+1.0); energy similarity (+0.99); acoustic preference (+0.5)
2. Gym Hero
   Score: 2.47
   Why: mood match (+1.0); energy similarity (+0.97); acoustic preference (+0.5)
3. Neon District
   Score: 1.50
   Why: energy similarity (+1.00); acoustic preference (+0.5)
4. Velvet Skyline
   Score: 1.48
   Why: energy similarity (+0.98); acoustic preference (+0.5)
5. Sunrise City
   Score: 1.42
   Why: energy similarity (+0.92); acoustic preference (+0.5)
```

---

## Limitations and Risks

This system is intentionally small and simplified. It does not understand lyrics, cultural context, or the deeper meaning behind a song. It may also over-favor a single genre or mood if the scoring rules are too narrow.

---

## Reflection

Read and complete [model_card.md](model_card.md) for a deeper explanation of the system's purpose, strengths, limitations, and bias. This project helped me understand that recommenders turn data into predictions by looking for patterns in user behavior and item features, and that those systems can accidentally create filter bubbles if they over-rely on a narrow set of signals.



