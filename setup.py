from setuptools import setup, find_packages

setup(
    name="hokireceh_claimer",
    version="0.1.2",
    description="A package for automatically claiming airdrops.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Hokireceh",
    author_email="ads.hokireceh@gmail.com",
    url="https://github.com/hokireceh/hokireceh_claimer",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "requests",
        "brotli",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
