# -*- coding: utf-8 -*-
from word2belt import Word2Belt
import pytest
import requests
import os

class TestWord2Belt(object):

    def test_get(self, w2b):
        v = w2b.get("大阪")
        assert v == [-3.6505529999999999, 6.2583789999999997,
        -1.2383459999999999, -3.8381949999999998, -5.5424810000000004,
        0.41331200000000001, 2.7852809999999999, 5.3537429999999997]

    def test_get_with_no_auth(self):
        w2b = Word2Belt(os.environ["W2B_URL"], "", "", "ohshima.txt")
        with pytest.raises(requests.exceptions.HTTPError):
            v = w2b.get("大阪")

    def test_get_with_out_voc(self, w2b):
        v = w2b.get("AJFOSJF+OSF")
        assert v is None

    def test_get_with_invalid_filename(self):
        w2b = Word2Belt(os.environ["W2B_URL"],
            os.environ["W2B_USER"], os.environ["W2B_PASS"], "O.txt")
        with pytest.raises(Exception):
            v = w2b.get("大阪")

    @pytest.fixture
    def w2b(self):
        return Word2Belt(os.environ["W2B_URL"],
            os.environ["W2B_USER"], os.environ["W2B_PASS"],
            "ohshima.txt")
