from setuptools import setup, find_packages

setup(
    name="make_question_interface",
    version="1.8.0",
    packages=find_packages(
        include=["make_question_interface", "make_question_interface.*"]
    ),
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    description="Drives client and server code to implement a functionality that makes question to a IA",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/danilocgsilva/make_question_interface",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
