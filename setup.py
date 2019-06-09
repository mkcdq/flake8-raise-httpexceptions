# coding: utf-8

from __future__ import with_statement

from setuptools import setup

from flake8_raise_httpexceptions.metadata import CODE_STEM, NAME, VERSION


def get_readme() -> str:
    with open("README.md") as readme_handle:
        return readme_handle.read()


setup(
    name=NAME,
    version=VERSION,
    description="Report any HTTPExceptions that are returned instead of raised. Plugin for flake8.",  # noqa: X
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    keywords="flake8 plugin httpexceptions",
    author="mkcdq",
    author_email="mkcdq@users.noreply.github.com",
    url="https://github.com/mkcdq/flake8-raise-httpexceptions",
    license="MIT",
    packages=["flake8_raise_httpexceptions"],
    install_requires=[],
    zip_safe=False,
    entry_points={"flake8.extension": ["{} = flake8_raise_httpexceptions:check".format(CODE_STEM)]},
    classifiers=[
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
