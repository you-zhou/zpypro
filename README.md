# zpypro

A brief description of your project goes here.  
(Example: zpypro is a Python project for ...)

## Features

- **Flat project structure** for simplicity and quick prototyping
- **Modern dependency management** via `pyproject.toml`
- **Dynamic logging**: Outputs logs to both the terminal and a log file, with log file location determined using `appdirs` for portability
- **YAML-based logging configuration** for easy customization

## Installation

```bash
git clone https://github.com/yourusername/zpypro.git
cd zpypro
```

To install dependencies using [uv](https://github.com/astral-sh/uv):

1. **Compile dependencies from `pyproject.toml` to a requirements file:**
   ```bash
   uv pip compile pyproject.toml > requirements.txt
   ```
2. **Install dependencies from the generated requirements file:**
   ```bash
   uv pip install -r requirements.txt
   ```

## Usage

```bash
# Example usage command
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
