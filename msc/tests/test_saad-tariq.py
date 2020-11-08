from msc.rot13 import rot13
from msc.rot13 import rot13_char

def test_rot13_char_a():
    assert "n" == rot13_char("a"), "Unexpected character"

def test_rot13_char_z():
    assert "m" == rot13_char("z"), "Unexpected character"

def test_rot13_char_alpha():
    assert "a123" == rot13_char("a123"), "Unexpected character"
