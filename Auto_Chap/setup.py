from setuptools import setup

setup(
    name='Auto_Chap',
    version='4.2',
    install_requires=[
        'requests==2.31.0',
        'numpy==1.26.2',
        'scipy==1.11.4',
        'matplotlib==3.8.2',
        'librosa==0.10.1',
    ],
    entry_points={
        'console_scripts': [
            'auto_chap=Auto_Chap:main',
        ],
    },
)
