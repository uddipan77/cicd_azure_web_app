import unittest, re, pathlib

class TestIndexHTML(unittest.TestCase):
    def test_index_exists(self):
        p = pathlib.Path("index.html")
        self.assertTrue(p.exists(), "index.html should exist at repo root")

    def test_has_h1_with_text(self):
        html = pathlib.Path("index.html").read_text(encoding="utf-8")
        # check there is at least one <h1>...</h1> with some non-empty text
        m = re.search(r"<h1[^>]*>(.*?)</h1>", html, flags=re.IGNORECASE | re.DOTALL)
        self.assertIsNotNone(m, "index.html should contain an <h1>...</h1>")
        # inner text should not be empty/whitespace
        inner = re.sub(r"<.*?>", "", m.group(1)).strip()
        self.assertTrue(len(inner) >= 3, "H1 text should be non-empty")

if __name__ == "__main__":
    unittest.main()
