from setuptools import setup
setup(
    name='doi2clip',
    version='1.0',
    entry_points={
        'console_scripts': [
            'doi2clip=doi2clip:main'
        ]
    }
)