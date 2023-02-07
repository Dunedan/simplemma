import re

from typing import Optional

RUSSIAN_PREFIXES = {
    "гидро",
    "за",
    "контр",
    "много",
    "микро",
    "недо",
    "пере",
    "под",
    "пред",
    "при",
    "про",
    "радио",
    "раз",
    "рас",
    "само",
    "экстра",
    "электро",
}

DEFAULT_RULES = {
    re.compile(r"(?:ости|остью|остей|остям|остями|остях)$"): "ость",
    re.compile(r"(?:ства|ств|ству|ствам|ством|ствами|стве|ствах)$"): "ство",
}


def fix_known_prefix_ru(token: str):
    return next((p for p in RUSSIAN_PREFIXES if token.startswith(p)), None)


def apply_ru(token: str, greedy: bool = False) -> Optional[str]:
    "Apply pre-defined rules for Russian."
    if token.endswith("ё"):
        return token.replace("ё", "е")

    if len(token) < 10 or token[0].isupper() or "-" in token:
        return None

    for rule, substitution in DEFAULT_RULES.items():
        if rule.search(token):
            return rule.sub(substitution, token)
    # token = token.replace("а́", "a")
    # token = token.replace("о́", "o")
    # token = token.replace("и́", "и")
    # if RUSSIAN_ENDINGS_OCTB.search(token):
    #     return RUSSIAN_ENDINGS_OCTB.sub("ость", token)
    # if RUSSIAN_ENDINGS_CTBO.search(token):
    #     return RUSSIAN_ENDINGS_CTBO.sub("ство", token)
    return None