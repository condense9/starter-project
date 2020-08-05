from python_bits import __version__, frequencies


def test_version():
    assert __version__ == '0.1.0'


def test_frequencies():
    essay = "the quick brown fox jumps over the lazy dog"
    freqs = frequencies(essay)
    assert freqs["the"] == 2
