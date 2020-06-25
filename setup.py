from setuptools import setup

setup(
    name = 'GammaRec',
    version = '1.0.3',
    description = 'Video capture recording and preview.',
    url = 'http://github.com/3snow_p7im/GammaRec',
    author = 'Wild Mouse',
    author_email = '3snowp7im@gmail.com',
    license = 'MIT',
    install_requires=['pygobject'],
    scripts = ['bin/gammarec'],
    data_files = [
        ('share/applications', ['data/gammarec.desktop']),
        ('share/icons', ['data/gammarec.png']),
    ]
)
