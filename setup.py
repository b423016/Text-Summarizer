import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer"
SRC_REPO = "Text_Summarizer"  # This should be a string, not a tuple
AUTHOR_NAME = "Ayush Jha"
AUTHOR_EMAIL = "ayushjha4277@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,  # The author's name should be separate from the email
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/b423016/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/b423016/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Mapping root ('') to 'src' directory
    packages=setuptools.find_packages(where="src"),  # Look for packages inside the 'src' directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
