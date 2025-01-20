from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quantum-simulator",
    version="0.1.0",
    author="Mridul Singhal",
    author_email="res.mridul@gmail.com",
    description="A quantum circuit simulator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mridul299792458/quantum-simulator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Quantum Computing",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.19.0",
        "matplotlib>=3.3.0",
    ],
)



