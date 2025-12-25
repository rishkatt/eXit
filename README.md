# eXit

![img0](images/eXit.png)

## Requirements

### OS

Works currently for Windows 11 and Linux-based operating systems.

### Software

- Python >=3.8

### Packages

- os
- sys
- time
- platform
- subprocess (Windows only)
- ascii-image-converter (Windows only)
- imgcat (WSL + Linux)
---
#### `ascii-image-converter`

For Windows, images cannot be displayed onto a terminal. This repository will rely on an [ascii-image-converter solution](https://github.com/TheZoraiz/ascii-image-converter) from another repository. The version/tag that reliably works for this solution will be [`v1.13.1`](https://github.com/TheZoraiz/ascii-image-converter/releases/tag/v1.13.1). 

First, create a `.bin/` directory in the root directory of this repository. Then, download the "amd64_64bit.zip" file into the .bin/ folder. Extract the executable file and place it in the `.bin/` directory. You may delete the remaining contents. 

#### `imgcat`

To install imgcat, run this command in your Linux terminal:
```
sudo snap install imgcat
```

Or if running on MacOS / Linux with Homebrew:
```
brew install danielgatis/imgcat/imgcat
```

## Usage

If you are operating in Linux, run this in your terminal:
```
python3 eXit.py
```

If you are operating in Windows, run this in your terminal:
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

