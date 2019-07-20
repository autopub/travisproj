#!/usr/bin/env python
from os.path import join
from setuptools import find_packages, setup


version = "0.1.8"

entry_points = {
    "console_scripts": [
        "say-hello = travisproj.hello:hello"
    ]
}

README = open("README.md", encoding="utf-8").read()
CHANGELOG = open("CHANGELOG.md", encoding="utf-8").read()

description = "\n".join([README, CHANGELOG])

setup(
    name="travisproj",
    version=version,
    url="https://github.com/autopub/travisproj",
    author="Travis Project",
    author_email="travisproj@example.com",
    description="This is a test project",
    long_description=description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points=entry_points,
    test_suite="travisproj.tests",
)
