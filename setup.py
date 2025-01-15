from setuptools import setup, find_packages

setup(
    name='wind_extraction',
    version='1.0.0',
    author='Amine Khedim',
    author_email='aminekhedim10@gmail.com',
    description='Bibliothèque pour extraire et écrire les données u10 et v10 à partir de fichiers NetCDF',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'netCDF4'
    ],
)

