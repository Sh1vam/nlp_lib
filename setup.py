from setuptools import setup, find_packages

setup(
    name="nlp_lib", 
    version="0.1.0",  
    author="Shivam Patel",
    author_email="shivampatel2552003@gmail.com",
    description="A custom NLP library for Text Pre-processing",
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",
    url="https://github.com/Sh1vam/nlp_lib",  
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",  
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
)
