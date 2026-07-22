# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

Give your model a short, descriptive name.
Example: **VibeFinder 1.0**

---

## 2. Intended Use

Describe what your recommender is designed to do and who it is for.

Prompts:

- What kind of recommendations does it generate
- What assumptions does it make about the user
- Is this for real users or classroom exploration

---

## 3. How the Model Works

Explain your scoring approach in simple language.

Prompts:

- What features of each song are used (genre, energy, mood, etc.)
- What user preferences are considered
- How does the model turn those into a score
- What changes did you make from the starter logic

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data

Describe the dataset the model uses.

Prompts:

- How many songs are in the catalog
- What genres or moods are represented
- Did you add or remove data
- Are there parts of musical taste missing in the dataset

---

## 5. Strengths

Where does your system seem to work well

Prompts:

- User types for which it gives reasonable results
- Any patterns you think your scoring captures correctly
- Cases where the recommendations matched your intuition

---

## 6. Limitations and Bias

Where the system struggles or behaves unfairly.

Prompts:

- Features it does not consider
- Genres or moods that are underrepresented
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users

This system currently favors strong genre and energy signals in a small catalog. Because the dataset is limited, a song like "Gym Hero" can score highly across multiple profiles when it has high energy and low acousticness, even if the genre or mood is not a perfect match. The model also ignores artist familiarity, tempo, valence, and lyrics, so it may miss why a listener prefers a specific style. The energy gap is treated symmetrically, which can still reward songs with similar energy even when they do not match the user’s desired mood. Users who want niche or mixed-genre playlists are likely under-served by this simple scoring function.

---

## 7. Evaluation

I tested three user profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock. I looked for whether the top results matched the profile labels and whether the explanations reflected the current weights in `recommender.py`.

- High-Energy Pop returned bright, fast songs like "Sunrise City" and "Gym Hero," which feels right because both have strong energy and at least one matching user preference.
- Chill Lofi shifted toward mellow, acoustic tracks such as "Library Rain" and "Midnight Coding," showing that the system can move toward low-energy, high-acousticness songs when requested.
- Deep Intense Rock ranked "Storm Runner" first because it matches both rock genre and intense mood, while "Gym Hero" still appeared high because its energy and acoustic footprint also align with the profile.

Compared to the pop profile, the chill profile selected softer lofi songs instead of upbeat pop, which makes sense because the mood and acousticness preferences changed. The Deep Intense Rock profile kept high energy but also required a more aggressive mood, so it favored a true rock track rather than a generic high-energy pop song.

---

## 8. Future Work

Ideas for how you would improve the model next.

Prompts:

- Additional features or preferences
- Better ways to explain recommendations
- Improving diversity among the top results
- Handling more complex user tastes

---

## 9. Personal Reflection

A few sentences about your experience.

Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps
