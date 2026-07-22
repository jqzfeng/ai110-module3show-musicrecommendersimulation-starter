import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = []
        for song in self.songs:
            score, _ = score_song(
                {
                    "favorite_genre": user.favorite_genre,
                    "favorite_mood": user.favorite_mood,
                    "target_energy": user.target_energy,
                    "likes_acoustic": user.likes_acoustic,
                },
                {
                    "genre": song.genre,
                    "mood": song.mood,
                    "energy": song.energy,
                    "acousticness": song.acousticness,
                },
            )
            scored.append((score, song))

        scored.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = score_song(
            {
                "favorite_genre": user.favorite_genre,
                "favorite_mood": user.favorite_mood,
                "target_energy": user.target_energy,
                "likes_acoustic": user.likes_acoustic,
            },
            {
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
                "acousticness": song.acousticness,
            },
        )
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load song rows from a CSV file and convert numeric fields to floats."""
    with open(csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        songs = []
        for row in reader:
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against a user profile and return a numeric score with reasons."""
    score = 0.0
    reasons: List[str] = []

    favorite_genre = user_prefs.get("favorite_genre") or user_prefs.get("genre")
    favorite_mood = user_prefs.get("favorite_mood") or user_prefs.get("mood")
    target_energy = user_prefs.get("target_energy") or user_prefs.get("energy")
    likes_acoustic = user_prefs.get("likes_acoustic", False)

    if favorite_genre and song.get("genre") == favorite_genre:
        score += 1.0
        reasons.append("genre match (+1.0)")

    if favorite_mood and song.get("mood") == favorite_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    if target_energy is not None and song.get("energy") is not None:
        energy_value = float(song["energy"])
        target_value = float(target_energy)
        energy_diff = abs(energy_value - target_value)
        energy_similarity = max(0.0, 1.0 - energy_diff)
        weighted_energy = energy_similarity * 2.0
        score += weighted_energy
        reasons.append(f"energy similarity (+{weighted_energy:.2f})")

    if likes_acoustic is not None and song.get("acousticness") is not None:
        acousticness = float(song["acousticness"])
        if likes_acoustic and acousticness >= 0.6:
            score += 0.5
            reasons.append("acoustic preference (+0.5)")
        elif not likes_acoustic and acousticness <= 0.3:
            score += 0.5
            reasons.append("acoustic preference (+0.5)")

    return round(score, 2), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top-k recommendations with explanations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((score, song, "; ".join(reasons)))

    ranked_songs = sorted(scored_songs, key=lambda item: item[0], reverse=True)
    return [(song, score, explanation) for score, song, explanation in ranked_songs[:k]]
