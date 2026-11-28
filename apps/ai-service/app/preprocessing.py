import re

# Satu fungsi ini dipakai saat training DAN saat API berjalan,
# supaya pipeline teksnya identik.
_NOMINAL = re.compile(r"\b\d+(?:[.,]\d+)*\s*(?:rb|ribu|k|jt|juta)?\b")
_NON_WORD = re.compile(r"[^a-z\s]")
_SPACES = re.compile(r"\s+")


def normalize_text(text: str) -> str:
    text = text.lower().strip()
    text = _NOMINAL.sub(" nominal ", text)  # "20rb", "17.000", "15k" -> "nominal"
    text = _NON_WORD.sub(" ", text)
    return _SPACES.sub(" ", text).strip()