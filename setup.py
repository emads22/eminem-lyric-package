from setuptools import setup, find_packages

setup(
    name='eminem_lyric',
    version='1.0.0',
    packages=find_packages(),
    description='A Python package for fetching Eminem song lyrics.',
    long_description='''This package provides a convenient interface for fetching and accessing lyrics of Eminem songs using an external lyrics API.
                        It offers methods to retrieve both processed lyrics and raw lyric data, allowing users flexibility in accessing the lyrics.''',
    author='Emads',
    author_email='ems22.dev@gmail.com',
    url='https://github.com/emads22/eminem_lyric',
    license='MIT',
    install_requires=[
        'requests',
    ],
    keywords=['eminem', 'lyric', 'lyrics', 'api'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers, Eminem Stans',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
