# Purpose

Convert a multicolor image to multiple unique color images

## Example:

**Original image:**

![](imgs/example_0.png)

**Output images:**

![](imgs/example_1.png)
![](imgs/example_2.png)
![](imgs/example_3.png)
![](imgs/example_4.png)

*Note that only the 4 images are shown above, in reality the original image yield 14 different colors*

# Install for devs

Will clone the repository and install the python module as a dev to your current python env.

```bash
git clone https://github.com/TheRaphael0000/wplace_helper
cd wplace_helper
python -m venv venv
source venv/Script/activate # windows: venv\Script\activate.bat
python -m pip install -e .
```

## Update

Not needed if you just installed the script.

```bash
cd wplace_helper
git pull
python -m pip install -e .
```

# Usage

## Standard usage

Will palettise your image to Wplace's 63 colors and create an image file for each color on input image.

```bash
python -m wplace_helper "mypixelart.png"
```

## Other commands

```bash
# list all commands
python -m wplace_helper --help

# be careful with the --no-reduction argument
# if you didn't palettise your image first you'll end up with a lot of images
# only use it if you know what you are doing
python -m wplace_helper "mypixelart.png" --no-reduction 
```

## GUI

```bash
python -m wplace_helper.gui # wip
```

# Todo

- [ ] Create a small GUI, for non-devs
- [ ] Add CI/CD with PyInstaller build