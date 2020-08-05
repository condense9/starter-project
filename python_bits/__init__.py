
from typing import Dict
from collections import Counter


def frequencies(essay: str) -> Dict[str, int]:
    counter = Counter(essay.lower().split())
    return dict(counter)


__version__ = '0.1.0'
