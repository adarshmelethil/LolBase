#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="LolBase",
    version="0.1",
    description="Get jokes off the internet",
    url="https://github.com/adarshmelethil/LolBase",
    download_url="",
    license="MIT",
    keywords=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    author="Adarsh Melethil",
    author_email="adarshmelethil@gmail.com",
    install_requires=["docopts"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["lolbase=lolbase.cli:main"]},
)
