from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="howmuch", 
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        'psutil',
        'tqdm',
        'matplotlib'
    ],
    author="idlebg",
    author_email="di@ffusion.ai",
    description="A simple disk space analyzer for *.ckpt & *.safetensors file extensions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/1e-2/HowMuch",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'howmuch=howmuch.HowMuch:main',
        ],
    }
)
