# Eminem Lyric

## Overview
Welcome to the documentation for the **Eminem Lyric** Python package! This document provides an overview of the package, installation instructions, usage examples, and other relevant information. The package is based on the [lyrics.ovh API](https://lyrics.ovh/), ensuring reliable access to accurate Eminem lyrics.

## Installation
You can install the Eminem Lyric package via pip:

```bash
pip install eminem_lyric
```

For more information and usage instructions, visit the [PyPI page](https://pypi.org/project/eminem_lyric/).

## Usage
To use the Eminem Lyric package, follow these steps:

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
The tests for the package can be found in the [tests](../tests) directory. You can run the tests using your preferred testing framework.

## License
This project is licensed under the **MIT License**, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.
