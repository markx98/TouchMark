Aqui está o README.md atualizado com o novo nome:

# TouchMark

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Notes](#notes)
- [License](#license)

## Introduction
The TouchMark tool allows users to mark specific coordinates on their screen. This tool is particularly useful for developers, designers, and anyone who needs to keep track of exact screen positions.

## Installation

### Setting up the Virtual Environment
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install the necessary packages:
   ```bash
   pip install pyautogui tkinter
   ```

### Creating an Executable
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Generate the executable:
   ```bash
   pyinstaller --onefile -w script.py
   ```

3. Find the executable:
   The executable file will be located in the `dist` folder as `script.exe`.

## Usage
1. Run the script:
   ```bash
   python script.py
   ```
   Alternatively, you can click the executable file located in the `dist` folder.

2. Mark coordinates:
   Click the "Touch" button. After 5 seconds, the coordinates of the current mouse cursor position will be displayed.

## Project Structure
```bash
TouchMark/
├── script/             # Script-related files
│   ├── .venv/          # Virtual environment
│   ├── .gitattributes  # Git attributes file
│   ├── .gitignore      # Git ignore file
│   ├── script.exe      # Executable file
│   └── script.py       # Main script file
├── LICENSE.txt         # License file
└── README.md           # Documentation file
```

## Notes
- Ensure you have Python installed on your system.
- Always activate the virtual environment before running the script to ensure all dependencies are properly managed.

## License
This project is licensed under the MIT License. See the LICENSE.txt file for more details.