# -*- coding:utf-8 -*-
from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

setup(
    name = "word2belt",
    packages = ["word2belt", "word2belt.scripts"],
    version = "0.0.1",
    description = "Word2Belt",
    author = "Makoto P. Kato",
    author_email = "kato@dl.kuis.kyoto-u.ac.jp",
    license     = "MIT License",
    url = "https://github.com/mpkato/word2belt",
    setup_requires = [],
    install_requires = [
        'requests'
    ],
    entry_points = {
        'console_scripts': [
            "word2belt=word2belt.scripts.word2belt_script:main"
        ]
    },
    tests_require=['pytest'],
    cmdclass = {'test': PyTest}
)
