# eXit

![img0](images/eXit.png)

## Requirements

### Software

- Python 3.8 or greater

### Packages

- os
- sys
- time
- platform
- ascii_magic (Windows)
- imgcat (WSL + Linux)
---
#### `ascii-image-converter`

For Windows, images cannot be displayed onto a terminal. This repository will rely on an [ascii-image-converter solution](https://github.com/TheZoraiz/ascii-image-converter) from another repository. The version that reliably works for this solution will be [v1.13.1](https://github.com/TheZoraiz/ascii-image-converter/releases/tag/v1.13.1). 

First, create a `.bin/` directory in the root directory of this repository. Then, download the "amd64_64bit.zip" file into the .bin/ folder. Extract the executable file and place it in the `.bin/` directory. You may delete the remaining contents. 

#### `imgcat`

To install imgcat, run this command:
```
sudo snap install imgcat
```

Or if running on MacOS / Linux with Homebrew:
```
brew install imgcat
```

## Usage

If you are operating in Linux:
```
python3 eXit.py
```

If you are operating in Windows:
```
python eXit.py
```

At any point during the game, if you would like to quit, run:
- `q`
- `q()`
- `quit`
- `exit`

## Disclaimer

This repository has no affiliation with the Mr. Robot brand. 

