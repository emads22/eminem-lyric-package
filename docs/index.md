# eminem_lyric

## Overview
Welcome to the documentation for the **eminem_lyric** Python package! This document provides an overview of the package, installation instructions, usage examples, and other relevant information. The package is based on the [lyrics.ovh API](https://lyrics.ovh/), ensuring reliable access to accurate eminem_lyric.

## Installation
You can install the eminem_lyric package via pip:

```bash
pip install eminem_lyric
```

For more information and usage instructions, visit the [PyPI page](https://pypi.org/project/eminem_lyric/).

## Usage
To use the eminem_lyric package, follow these steps:

1. Import the `EminemLyric` class from the package.
2. Create an instance of the `EminemLyric` class, providing the title of the Eminem song.
3. Access the lyrics using the `lyric` property.

```python
from eminem_lyric import EminemLyric

# Create an instance of EminemLyric
lyric_object = EminemLyric(song_title='Lose Yourself')

# Access the lyrics
song_lyric = lyric_object.lyric
print(song_lyric)
```

For more detailed usage instructions and examples, please refer to the [examples](../examples) directory.

## Tests
The tests for the package can be found in the [tests](../tests) directory. 
To run the tests for the package, you can use one of the following commands:

```bash
python -m unittest discover -s tests
```

or alternatively:

```bash
python -m unittest tests.test_eminem_lyric
```

The first command runs all tests in the tests directory, while the second command runs a specific test file (`test_eminem_lyric.py`). Make sure you are in the root directory of the project when running these commands.

## License
This project is licensed under the **MIT License**, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.
