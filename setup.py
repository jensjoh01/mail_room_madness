from setuptools import setup


setup(
    name='Mail Room Madness',
    py_modules=['mail_room_madness'],
    package_dir={'': 'src'},
    install_requires=['tabulate==0.8.1'],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    entry_points={
        'console_scripts': [
            'mailroom = mail_room_madness:main'
        ]
    }
)
