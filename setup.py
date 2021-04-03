import setuptools

setuptools.setup(
    name='pyrule-compendium',
    version='2.3.0',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='The official python wrapper for the Hyrule Compendium API',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gadhagod/pyrule-compendium',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests']
)
