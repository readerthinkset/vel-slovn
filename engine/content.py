"""AI phrase generation with permanent no-repeat history."""

from __future__ import annotations

import json
import random
import time
from datetime import datetime

import requests

import config
from config import CATEGORIES, CATEGORIES_NATIVE, HISTORY_DIR, MAX_RECENT_CATEGORIES

PHRASE_HISTORY_FILE = HISTORY_DIR / "all_generated_phrases.json"
RECENT_CATEGORIES_FILE = HISTORY_DIR / "recent_categories.json"

PHRASE_KEY = config.LANGUAGE["history_key"]
LANGUAGE_NAME = config.LANGUAGE["name"]
NATIVE_NAME = config.LANGUAGE["native_name"]

# ==== FALLBACK PHRASES START ====
FALLBACK_PHRASES = [
    {"english": "Hello, nice to meet you.", "native": "Pozdravljeni, lepo vas je spoznati.", "transliteration": "Pozdravljeni, lepo vas je spoznati."},
    {"english": "Thank you very much.", "native": "Najlepša hvala.", "transliteration": "Najlepša hvala."},
    {"english": "Good morning, have a great day.", "native": "Dobro jutro, lep dan vam želim.", "transliteration": "Dobro jutro, lep dan vam želim."},
    {"english": "I love learning new languages.", "native": "Obožujem učenje novih jezikov.", "transliteration": "Obožujem učenje novih jezikov."},
    {"english": "Never give up on your dreams.", "native": "Nikoli ne obupajte nad svojimi sanjami.", "transliteration": "Nikoli ne obupajte nad svojimi sanjami."},
    {"english": "Every day is a fresh start.", "native": "Vsak dan je nov začetek.", "transliteration": "Vsak dan je nov začetek."},
    {"english": "Believe in yourself always.", "native": "Vedno verjemite vase.", "transliteration": "Vedno verjemite vase."},
    {"english": "Small steps lead to big changes.", "native": "Majhni koraki vodijo do velikih sprememb.", "transliteration": "Majhni koraki vodijo do velikih sprememb."},
    {"english": "You are stronger than you think.", "native": "Močnejši ste, kot si mislite.", "transliteration": "Močnejši ste, kot si mislite."},
    {"english": "Happiness is a choice, choose it.", "native": "Sreča je izbira, izberite jo.", "transliteration": "Sreča je izbira, izberite jo."},
    {"english": "What time is it please.", "native": "Koliko je ura, prosim.", "transliteration": "Koliko je ura, prosim."},
    {"english": "Where is the train station.", "native": "Kje je železniška postaja.", "transliteration": "Kje je železniška postaja."},
    {"english": "How much does this cost.", "native": "Koliko to stane.", "transliteration": "Koliko to stane."},
    {"english": "Can you help me please.", "native": "Mi lahko pomagate, prosim.", "transliteration": "Mi lahko pomagate, prosim."},
    {"english": "I would like a coffee please.", "native": "Rad bi kavo, prosim.", "transliteration": "Rad bi kavo, prosim."},
    {"english": "The food is delicious today.", "native": "Hrana je danes okusna.", "transliteration": "Hrana je danes okusna."},
    {"english": "Have a wonderful weekend.", "native": "Lep vikend vam želim.", "transliteration": "Lep vikend vam želim."},
    {"english": "Take care of yourself.", "native": "Skrbite zase.", "transliteration": "Skrbite zase."},
    {"english": "See you tomorrow my friend.", "native": "Se vidimo jutri, prijatelj.", "transliteration": "Se vidimo jutri, prijatelj."},
    {"english": "The weather is beautiful outside.", "native": "Zunaj je lepo vreme.", "transliteration": "Zunaj je lepo vreme."},
    {"english": "I am very happy today.", "native": "Danes sem zelo vesel/vesela.", "transliteration": "Danes sem zelo vesel/vesela."},
    {"english": "Learning a language opens new doors.", "native": "Učenje jezika odpira nova vrata.", "transliteration": "Učenje jezika odpira nova vrata."},
    {"english": "Keep practicing every single day.", "native": "Vadite vsak dan.", "transliteration": "Vadite vsak dan."},
    {"english": "You can achieve anything you want.", "native": "Lahko dosežete vse, kar si želite.", "transliteration": "Lahko dosežete vse, kar si želite."},
    {"english": "Rest when you are tired.", "native": "Počivajte, ko ste utrujeni.", "transliteration": "Počivajte, ko ste utrujeni."},
    {"english": "Focus on the positive things.", "native": "Osredotočite se na pozitivne stvari.", "transliteration": "Osredotočite se na pozitivne stvari."},
    {"english": "Learn from your mistakes.", "native": "Učite se iz svojih napak.", "transliteration": "Učite se iz svojih napak."},
    {"english": "Trust the process completely.", "native": "Popolnoma zaupajte procesu.", "transliteration": "Popolnoma zaupajte procesu."},
    {"english": "Breathe deeply and stay calm.", "native": "Globoko dihajte in ostanite mirni.", "transliteration": "Globoko dihajte in ostanite mirni."},
    {"english": "Enjoy the little moments in life.", "native": "Uživajte v malih trenutkih življenja.", "transliteration": "Uživajte v malih trenutkih življenja."},
    {"english": "Smile more, worry less.", "native": "Več se smejte, manj skrbite.", "transliteration": "Več se smejte, manj skrbite."},
    {"english": "Be kind to everyone you meet.", "native": "Bodite prijazni do vseh, ki jih srečate.", "transliteration": "Bodite prijazni do vseh, ki jih srečate."},
    {"english": "Help others without expecting anything back.", "native": "Pomagajte drugim, ne da bi pričakovali povračilo.", "transliteration": "Pomagajte drugim, ne da bi pričakovali povračilo."},
    {"english": "Forgive yourself and move forward.", "native": "Oprostite si in pojdite naprej.", "transliteration": "Oprostite si in pojdite naprej."},
    {"english": "Stay strong in difficult times.", "native": "Ostanite močni v težkih časih.", "transliteration": "Ostanite močni v težkih časih."},
    {"english": "Every moment is a new beginning.", "native": "Vsak trenutek je nov začetek.", "transliteration": "Vsak trenutek je nov začetek."},
    {"english": "Listen to your heart always.", "native": "Vedno poslušajte svoje srce.", "transliteration": "Vedno poslušajte svoje srce."},
    {"english": "Do what makes you happy.", "native": "Delajte tisto, kar vas osrečuje.", "transliteration": "Delajte tisto, kar vas osrečuje."},
    {"english": "Your potential is unlimited.", "native": "Vaš potencial je neomejen.", "transliteration": "Vaš potencial je neomejen."},
    {"english": "Be brave and take risks.", "native": "Bodite pogumni in tvegajte.", "transliteration": "Bodite pogumni in tvegajte."},
    {"english": "Celebrate your progress every day.", "native": "Vsak dan praznujte svoj napredek.", "transliteration": "Vsak dan praznujte svoj napredek."},
    {"english": "Surround yourself with good people.", "native": "Obkrožite se z dobrimi ljudmi.", "transliteration": "Obkrožite se z dobrimi ljudmi."},
    {"english": "Read books and grow your mind.", "native": "Berite knjige in razvijajte svoj um.", "transliteration": "Berite knjige in razvijajte svoj um."},
    {"english": "Travel and discover new places.", "native": "Potujte in odkrivajte nove kraje.", "transliteration": "Potujte in odkrivajte nove kraje."},
    {"english": "Appreciate what you already have.", "native": "Cenite tisto, kar že imate.", "transliteration": "Cenite tisto, kar že imate."},
    {"english": "Dance like nobody is watching.", "native": "Plešite, kot da vas nihče ne gleda.", "transliteration": "Plešite, kot da vas nihče ne gleda."},
    {"english": "Sing from your heart out loud.", "native": "Pojte iz srca na glas.", "transliteration": "Pojte iz srca na glas."},
    {"english": "Plant seeds of kindness everywhere.", "native": "Sadite seme prijaznosti povsod.", "transliteration": "Sadite seme prijaznosti povsod."},
    {"english": "Let go of what you cannot control.", "native": "Pustite tisto, česar ne morete nadzorovati.", "transliteration": "Pustite tisto, česar ne morete nadzorovati."},
    {"english": "Be present in the here and now.", "native": "Bodite prisotni v tukaj in zdaj.", "transliteration": "Bodite prisotni v tukaj in zdaj."},
]
# ==== FALLBACK PHRASES END ====


def _load_json(path, default):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return default


def _save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_phrase_history():
    data = _load_json(PHRASE_HISTORY_FILE, {"phrases": [], "last_updated": None})
    data.setdefault("phrases", [])
    return data


def save_phrase_history(data):
    data["last_updated"] = datetime.now().isoformat()
    _save_json(PHRASE_HISTORY_FILE, data)


def is_phrase_used(english):
    english_lower = english.lower().strip()
    for p in load_phrase_history()["phrases"]:
        if p.get("english", "").lower().strip() == english_lower:
            return True
    return False


def _history_native(p):
    for key in (PHRASE_KEY, "vietnamese", "native", "translation", "target"):
        value = p.get(key)
        if value:
            return str(value)
    return ""


def add_phrases_to_history(phrases, category):
    history = load_phrase_history()
    for phrase in phrases:
        history["phrases"].append({
            "english": phrase["english"],
            PHRASE_KEY: phrase["native"],
            "transliteration": phrase.get("transliteration", ""),
            "category": category,
            "generated_at": datetime.now().isoformat(),
        })
    save_phrase_history(history)
    print(f"[content] Saved {len(phrases)} phrases (history total: {len(history['phrases'])})")


def get_available_category():
    data = _load_json(RECENT_CATEGORIES_FILE, {"recent_categories": [], "last_updated": None})
    recent = data.get("recent_categories", [])
    available = [c for c in CATEGORIES if c not in recent]
    if not available:
        recent = recent[-5:]
        available = [c for c in CATEGORIES if c not in recent]
        print("[rotation] Reset recent categories")
    selected = random.choice(available)
    recent.append(selected)
    data["recent_categories"] = recent[-MAX_RECENT_CATEGORIES:]
    data["last_updated"] = datetime.now().isoformat()
    _save_json(RECENT_CATEGORIES_FILE, data)
    print(f"[rotation] Category: {selected} ({len(available)} available)")
    return selected


def _normalize_phrase(item):
    if not isinstance(item, dict):
        return None
    english = str(item.get("english", "")).strip()
    native = str(
        item.get(PHRASE_KEY)
        or item.get("native")
        or item.get("vietnamese")
        or item.get("translation")
        or ""
    ).strip()
    translit = str(item.get("transliteration") or item.get("romanization") or item.get("romaji") or "").strip()
    if not english or not native:
        return None
    if len(english.split()) > 16:
        return None
    if "/" in native or "|" in native:
        native = native.split("/")[0].split("|")[0].strip()
    return {
        "english": english.replace("  ", " ").strip(),
        "native": native.strip(),
        "transliteration": translit.strip().strip("[]"),
    }


def _history_keys(history):
    used_en = set()
    used_nat = set()
    for p in history.get("phrases", []):
        en = str(p.get("english", "")).lower().strip()
        nat = _history_native(p).lower().strip()
        if en:
            used_en.add(en)
        if nat:
            used_nat.add(nat)
    return used_en, used_nat


def generate_phrases(category_english: str, num_phrases: int = 5) -> list:
    category_native = CATEGORIES_NATIVE[category_english]
    history = load_phrase_history()
    used_en, used_nat = _history_keys(history)
    recent_english = [
        p["english"] for p in history["phrases"] if p.get("category") == category_english
    ][-30:]

    models = [config.AI_MODEL]
    if "gemini-fast" not in models:
        models.append("gemini-fast")

    if config.POLLINATIONS_API_KEY:
        for attempt in range(5):
            model = models[0] if attempt < 3 else models[-1]
            try:
                phrases = _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model)
                unique = []
                for item in phrases:
                    p = _normalize_phrase(item)
                    if not p:
                        continue
                    key_en = p["english"].lower().strip()
                    key_nat = p["native"].lower().strip()
                    if key_en in used_en or key_nat in used_nat:
                        continue
                    if any(key_en == u["english"].lower().strip() for u in unique):
                        continue
                    used_en.add(key_en)
                    used_nat.add(key_nat)
                    unique.append(p)
                    if len(unique) >= num_phrases:
                        break
                if len(unique) >= num_phrases:
                    add_phrases_to_history(unique[:num_phrases], category_english)
                    return unique[:num_phrases]
                print(f"[content] Attempt {attempt + 1}: only {len(unique)} fresh phrases (need {num_phrases})")
            except Exception as exc:  # noqa: BLE001 - network boundary
                print(f"[content] Attempt {attempt + 1} failed ({model}): {exc}")
            time.sleep(1.5 * (attempt + 1))
    else:
        print("[content] No POLLINATIONS_API_KEY, using fallback phrases")

    fresh_fallback = []
    for p in FALLBACK_PHRASES:
        if p["english"].lower().strip() in used_en or p["native"].lower().strip() in used_nat:
            continue
        fresh_fallback.append(p)
    if not fresh_fallback:
        raise RuntimeError("Phrase API unavailable and no unused fallback phrases left; refusing to reuse phrases")
    chosen = fresh_fallback[:num_phrases]
    if len(chosen) < num_phrases:
        print(f"[content] Only {len(chosen)} fresh fallback phrases; building a shorter lesson")
    add_phrases_to_history(chosen, category_english)
    return chosen


def _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model=None):
    avoid = ""
    if recent_english:
        avoid = "\nDo NOT reuse any of these phrases:\n" + "\n".join(f"- {p}" for p in recent_english)

    prompt = f"""Create {num_phrases * 6} unique {category_english} phrases for English speakers learning {LANGUAGE_NAME}.
{avoid}

Rules:
1. Keep every phrase short and natural (4-11 words in English).
2. Use natural commas for TTS breathing pauses.
3. Each phrase must be speakable in 2-4 seconds.
4. Write clean {LANGUAGE_NAME} in {NATIVE_NAME} with correct accents and orthography. One translation only, no slashes.
5. Transliteration is a friendly Roman-script pronunciation guide for English speakers (not IPA).
6. Vary the sentence patterns and emotions. No duplicates.
7. Phrases must feel like real everyday language, not textbook filler.

Return ONLY a JSON array:
[{{"english": "...", "native": "...", "transliteration": "..."}}]"""

    response = requests.post(
        "https://gen.pollinations.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {config.POLLINATIONS_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model or config.AI_MODEL,
            "messages": [
                {"role": "system", "content": f"You are a {LANGUAGE_NAME} teacher creating short, natural, varied bilingual phrases. Reply with JSON only."},
                {"role": "user", "content": prompt},
            ],
            "temperature": min(0.95 + attempt * 0.02, 1.0),
        },
        timeout=90,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"].strip()

    if "```json" in content:
        content = content.split("```json", 1)[1].split("```", 1)[0].strip()
    elif "```" in content:
        content = content.split("```", 1)[1].split("```", 1)[0].strip()

    start = content.find("[")
    end = content.rfind("]")
    if start >= 0 and end > start:
        content = content[start:end + 1]

    data = json.loads(content)
    if not isinstance(data, list):
        raise ValueError("AI did not return a JSON array")
    return data
