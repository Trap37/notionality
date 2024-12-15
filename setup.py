from setuptools import find_packages, setup

with open('README.md', 'r') as fp:
    readme = fp.read()

requirements = ['notion-client>=0.5']

setup(
    name='notionality',
    version='0.0.1',
    author='Patrick Farrell',
    author_email='patrickthethree@gmail.com',
    description='Datamodels for the Notion API SDK',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/Trap37/notionality/',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
