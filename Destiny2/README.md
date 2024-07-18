# Destiny 2 Macros


## Requirements

A valid Python3 installation is required to run these scripts. Enter the following command to install the package requirnments.

`python3 -m pip install -r requirements.txt`


## Lament Fly

The lament flying macro requires you to be on a titan class using the catapult lift jump and the lion rampant exotic boots. The Lament sword should be the active weapon. The macro handles all movment actions, all you have to do is hold the key the macro is bound to and look in the direction you want to fly.

### Usage
`python3 lament-fly.py '<macro key bind>' '<stop macro key bind>'`

An example where the macro keybind is bound to the '~' (tilde) key and the keybind to stop the macro script is bound to the escape key: 

`python3 lament-fly.py '~' 'esc'`


## Quick Draw (Patched)

The quick draw macro allows you to easily perform the quick draw glitch, commonly used with two slug shotguns for close range boss dps situations like Taniks in DSC or Templar in VOG. The macro handles all the required actions except for aiming. All you have to do is hold the key the macro is bound to and aim at the target. This macro also has an option to quick swap with the heavy slot as seen [here](https://www.youtube.com/watch?v=MikvUt78IH0).

### Usage
`python3 quick-draw.py <option> '<macro key bind>' '<stop macro key bind>'`

An example where option 1 is selected for double slugging with the macro keybind bound to the '~' (tilde) key and the keybind to stop the macro script bound to the escape key: 
`python3 quick-draw.py 1 '~' 'esc'`

#### Options
1. Double Slug
2.  Xeno + Double Slug


