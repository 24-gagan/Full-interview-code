import string


class TestMyStuff:
    def test_type(self):
        assert type(1) == int

    def tesr_strs(self):
        assert str.upper("python") == "PYTHON"
        assert string.capwords() == "Python"
