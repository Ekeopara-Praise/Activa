from setuptools import setup

with open(r"C:\Users\Sir_Praise\Documents\Package\Readme.md", 'r') as f:
    long_description = f.read()

setup(name="Activa",
      version="1.0.5",
      author = "Praise Ekeopara",
      author_email="ekeoparapraise@gmail.com",
      description="Activation Function Package",
      long_description=long_description,
      long_description_content_type = "text/markdown",
      url="https://github.com/Ekeopara-Praise/Activa",
      project_urls={
            "Bug Tracker": "https://github.com/Ekeopara-Praise/Activa/issues"},

      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"],
      python_requires=">=3.6")
