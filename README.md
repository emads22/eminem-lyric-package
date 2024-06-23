# Eminem Lyric

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Eminem Lyric** is a Python package designed for all Eminem stans out there. I have been an Eminem stan since the early 2000s, so if you've been a fan of Eminem's music since "The Slim Shady LP" or if you've recently discovered his talent, this package is for you. With **Eminem Lyric**, you can easily access the lyrics of your favorite Eminem tracks, from his early hits to his latest releases.

## Features
- **Easy to Use**: Retrieve lyrics with just a few lines of Python code.
- **Comprehensive**: Access lyrics for a wide range of Eminem songs.
- **Flexible**: Retrieve lyrics as plain text or in raw JSON format.

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

For more detailed usage instructions and examples, please refer to the [examples](./examples) directory.

## Documentation
For more detailed documentation, including API references and usage examples, please visit the [documentation](./docs/index.md).

## Examples
Check out the [examples](./examples) directory for usage examples of the Eminem Lyric package.

## Tests
The tests for the package can be found in the [tests](./tests) directory. You can run the tests using your preferred testing framework.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.
