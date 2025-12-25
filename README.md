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

##### ascii_magic

For ascii_magic, run this command in Windows:
```
pip install pillow ascii_magic
```

For Linux, utilize a virtual environment. Start with running:
```
sudo apt install -y python3-venv
```

This will install venv support. Now, create a virtual environment within the repo. Run:
```
python3 -m venv .venv
```

This creates:
```
.venv/
```

Activate the virtual environment by running:
```
source .venv/bin/activate
```

You should see:

```
(.venv)
```

before your terminal username.

We can then install pillow and ascii_magic with running:
```
pip install pillow ascii_magic
```

##### imgcat

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

At any point during the game, if you would like to quit, use:
- q
- q()
- quit
- exit

## Disclaimer

This repository has no affiliation with the Mr. Robot brand. 
