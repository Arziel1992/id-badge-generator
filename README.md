# ID badge Generator

## System Enviroment

Using WSL2 Ubuntu 20.04

## System Enviroment Setup

With (default) latest Python 3.8.x

```bash
sudo apt update
sudo apt upgrade
```

## Update Path

To find installed pip packages afterwards

To find where it is installed
`which python3`

Which should be
`/home/<user>/.local/bin`

To display the path and check if the python3 binaries are listed
`echo $PATH`

To add to Path

`nano ~./bashrc`

Add at the end:

`export PATH=$PATH:/home/<user>/.local/bin`

To apply now:
`source ~/.profile`

Or open a new Terminal

## Local User Enviroment Setup

`pip install pandas qrcode notebook cairosvg`

You will need to reload your Editor to have it see the recent installs and changes.

## Finnicky behaviour

When opening the notebook, up right you can choose the python kernel you want to use, which should be the one in `/home/<user>/.local/bin`
And to have the editor in sync with it, on the bottom left choose the default python version to use to the same as previously mentioned.

For some reason, at least for me, I have to recheck once in a while (in VS Code) if the selected kernel is still the correct one on both places.

## TODO

- Improve the Readme.
- Improve the code comments.
- Refactor the SVG generation and pasting.
