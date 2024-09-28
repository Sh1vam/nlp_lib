from setuptools import setup, find_packages
def reqdmnt():
    with open('requirement.txt') as req:
        return req.read().splitlines()
setup(
    name="nlp_lib", 
    version="0.1.0",  
    author="Shivam Patel",
    author_email="",
    description="A custom NLP library for Text Pre-processing",
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",
    url="https://github.com/Sh1vam/nlp_lib",  
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
    install_requires=reqdmnt(), 
)
