from setuptools import setup, find_packages

setup(
    name='mypoc',
    packages=find_packages(),
    version='0.1',
    author='mutoulion',
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'pymysql',
    ],
)
