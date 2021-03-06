import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="the_video_editaneitor",
    version="0.0.3",
    author="Demian Bolivar",
    author_email="demian054m@gmail.com",
    description="This is a small video clips editor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requiered=[
        "pygame",
        "pygame_gui",
        "pyAudioAnalysis",
        "eyed3",
        "pydub",
        "eyed3",
        "pydub",
        "matplotlib",
        "moviepy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)