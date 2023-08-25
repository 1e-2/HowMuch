
# HowMuch
![60% Works](https://img.shields.io/badge/60%25%20of%20the%20Time-It%20Works%20Every%20Time-green)

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Repo Size](https://img.shields.io/github/repo-size/1e-2/HowMuch)
![Last Commit](https://img.shields.io/github/last-commit/1e-2/HowMuch)
![Open Issues](https://img.shields.io/github/issues-raw/1e-2/HowMuch)
![Closed Issues](https://img.shields.io/github/issues-closed-raw/1e-2/HowMuch)
![Pull Requests](https://img.shields.io/github/issues-pr/1e-2/HowMuch)
![Stars](https://img.shields.io/github/stars/1e-2/HowMuch)
![Coffee Level](https://img.shields.io/badge/Coffee%20Level-110%25-brown)
![Stress Level](https://img.shields.io/badge/Stress%20Level-Endurable-green)

**Have you ever asked yourself, "How much space have I wasted on `*.ckpt` and `*.safetensors` checkpoints?"** 🤔
Say hello to HowMuch: Checking checkpoint wasted space since... well, now! 😄 Enjoy this somewhat unnecessary, yet "fun-for-the-whole-family" DiskSpaceAnalyzer tool. 😄
## Overview


`HowMuch` is a Python tool designed to scan your drives (or a specified directory) and report on the total space used by files with specific extensions, mainly `.ckpt` and `.safetensors`. 

It outputs:
- The total storage capacity of each scanned drive or directory.
- The space occupied by `.ckpt` and `.safetensors` files.
- The free space available.
- A neat bar chart visualizing the above data.

## Installation

### From PyPI

You can easily install `HowMuch` via pip:

```bash
pip install howmuch
```

### From Source

1. Clone the repository:

   ```bash
   git clone https://github.com/1e-2/HowMuch.git
   ```

2. Navigate to the cloned directory and install:

   ```bash
   cd HowMuch
   pip install .
   ```

## Usage


Run the tool without any arguments to scan all drives:

```bash
howmuch
```

Or, specify a particular directory or drive to scan:

```bash
howmuch --scan C:
```

The results will be displayed in the console, saved to a text file (`HowMuch_output.txt`), and visualized in a bar chart (`HowMuch_chart.png`).

## Contributing

Feel free to fork the repository, make changes, and open a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License. See [LICENSE](https://github.com/1e-2/HowMuch/blob/main/LICENSE) for details.

## Author

- **idlebg** - [GitHub](https://github.com/idlebg)

For any additional questions or comments, please [open an issue](https://github.com/1e-2/HowMuch/issues/new).
![image](https://github.com/1e-2/HowMuch/assets/50985923/71446a10-6652-48f7-a19a-157e3465966a)
![Screenshot_2083](https://github.com/1e-2/HowMuch/assets/50985923/d7e229e2-b45f-498b-bdf6-8a10ff7122bb)
