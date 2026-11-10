"""VELOCITY SLOVENIAN - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY SLOVENIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "SLOVENIAN"
HANDLE = "@velocityslovenian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "sl",
    "name": "Slovenian",
    "native_name": "Slovenščina",
    "history_key": "slovenian",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "sl-SI-RokNeural",
    "native_fallback_voice": "sl-SI-PetraNeural",
    "native_engine": "edge",
    "native_lang_code": "sl",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "SLOVENŠČINA",
    "translit_label": "SAY IT LIKE",
    "greeting": "Živjo!",
    "encouragement": "Odlično!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Pozdravi", "hand", "#1CB0F6"),
    ("Basic Phrases", "Osnovne Fraze", "chat", "#58CC02"),
    ("Common Expressions", "Pogosti Izrazi", "chat", "#1CB0F6"),
    ("Travel", "Potovanje", "plane", "#1CB0F6"),
    ("Restaurant", "Restavracija", "fork", "#FF7A00"),
    ("Shopping", "Nakupovanje", "bag", "#E056A0"),
    ("Emergency", "Nujno", "siren", "#FF4B4B"),
    ("Family Terms", "Družinski Izrazi", "heart", "#E056A0"),
    ("Numbers", "Številke", "hash", "#A560E8"),
    ("Time", "Čas", "clock", "#00A889"),
    ("Motivation", "Motivacija", "rocket", "#A560E8"),
    ("Love", "Ljubezen", "heart", "#FF4B4B"),
    ("Success", "Uspeh", "trophy", "#F5A700"),
    ("Wisdom", "Modrost", "book", "#A560E8"),
    ("Happiness", "Sreča", "smile", "#F5A700"),
    ("Self Improvement", "Samoizboljšanje", "leaf", "#58CC02"),
    ("Gratitude", "Hvaležnost", "heart", "#FF7A00"),
    ("Friendship", "Prijateljstvo", "users", "#00A889"),
    ("Hope", "Upanje", "sun", "#FF7A00"),
    ("Creativity", "Ustvarjalnost", "palette", "#E056A0"),
    ("Inner Peace", "Notranji Mir", "lotus", "#00A889"),
    ("Confidence", "Samozavest", "shield", "#1CB0F6"),
    ("Perseverance", "Vztrajnost", "mountain", "#FF7A00"),
    ("Inspiration", "Navdih", "sparkles", "#A560E8"),
    ("Positive Life", "Pozitivno Življenje", "sun", "#58CC02"),
    ("Courage", "Pogum", "shield", "#FF4B4B"),
    ("Kindness", "Prijaznost", "heart", "#E056A0"),
    ("Patience", "Potrpežljivost", "hourglass", "#00A889"),
    ("Forgiveness", "Odpuščanje", "hands", "#FF7A00"),
    ("Strength", "Moč", "dumbbell", "#FF4B4B"),
    ("Joy", "Veselje", "smile", "#F5A700"),
    ("Balance", "Ravnovesje", "scale", "#00A889"),
    ("Growth", "Rast", "sprout", "#58CC02"),
    ("Purpose", "Namen", "target", "#A560E8"),
    ("Mindfulness", "Čuječnost", "lotus", "#00A889"),
    ("Daily Routine", "Dnevna rutina", "calendar", "#1CB0F6"),
    ("Weather", "Vreme", "cloud", "#1CB0F6"),
    ("Feelings", "Občutki", "smile", "#E056A0"),
    ("Food", "Hrana", "fork", "#FF7A00"),
    ("Health", "Zdravje", "heart", "#58CC02"),
    ("Work", "Delo", "briefcase", "#1CB0F6"),
    ("Technology", "Tehnologija", "chip", "#A560E8"),
    ("Nature", "Narava", "leaf", "#58CC02"),
    ("Animals", "Živali", "paw", "#FF7A00"),
    ("Colors", "Barve", "palette", "#E056A0"),
    ("Directions", "Smeri", "compass", "#1CB0F6"),
    ("Body Parts", "Deli telesa", "hand", "#00A889"),
    ("Clothes", "Oblačila", "shirt", "#E056A0"),
    ("Music", "Glasba", "music", "#A560E8"),
    ("Sports", "Šport", "ball", "#FF7A00"),
    ("Holidays", "Prazniki", "gift", "#FF4B4B"),
    ("Education", "Izobraževanje", "book", "#1CB0F6"),
    ("Culture", "Kultura", "globe", "#00A889"),
    ("Finance", "Finance", "coin", "#58CC02"),
    ("Relationships", "Odnosi", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnslovenian",
    "#slovenianlessons",
    "#slovenianforbeginners",
    "#languagelearning",
    "#slovenianvocabulary",
    "#velocityslovenian",
    "#dailyslovenian",
    "#slovenian",
    "#learnlanguages",
    "#speakslovenian",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
