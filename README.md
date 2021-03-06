# pyttenberg

## What is this?
This is a little tool for generating pictures that are inspired by Battenberg cakes.
I was inspired by an excellent [talk](https://www.youtube.com/watch?v=j7BArZJxL9M) on abstract Mathematics by Dr Eugenia
Cheng, where she, among other things, talks about Battenberg cakes, iterated Battenberg cakes, and representing said
Battenberg cakes with a Tree datastructure.

## Dependencies

Tested with python3.

Requires matplotlib. `pip install matplotlib` should work. A `requirements.txt` file is also provided for installing via
`pip install -r requirements.txt`

## Usage
###From the command line:

```bash
git clone https://github.com/casperkoning/pyttenberg.git
cd pyttenberg
python3 pyttenberg.py %NumberOfColors% [options]
```

#### Options:
Parameter   | Flag | Description
------------|------|------------
Output path | `-o` | Path of output file. Defaults to `output.png`.
Help        | `-h` | Display a help message.

## Examples

Using only two colors, as in a typical Battenberg cake:

```bash
python3 pyttenberg.py 2
```

<img src="/examples/output_2_colors.png" width="400">

Using eight colors, as you would have with a Battenberg cake of Battenberg cakes of Battenberg cakes:

```bash
python3 pyttenberg.py 8
```

<img src="/examples/output_8_colors.png" width="400">


Using 256 colors:

```bash
python3 pyttenberg.py 256
```

<img src="/examples/output_256_colors.png" width="400">

Using 1024 colors:

```bash
python3 pyttenberg.py 1024
```

<img src="/examples/output_1024_colors.png" width="400">
