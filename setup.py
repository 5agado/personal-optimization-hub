from setuptools import setup, find_packages

REQUIREMENTS = [
    'numpy',
    'pandas',
    'matplotlib',
    'seaborn',
    # spaced_repetition specific
    'genanki',
    'xlrd',
]

setup(
    name="personal_optimization_hub",
    version="0.0.1",
    description="Set of utilities related to personal development and optimization",
    license="Apache 2.0",
    author="Alex Martinelli",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['anki-gen=spaced_repetition.anki_utils:main'],
    },
    install_requires=REQUIREMENTS,
)
