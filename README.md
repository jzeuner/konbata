<div align="center">
  <h1>Konbata</h1>
</div>

<div align="center">
  <strong>Python File Converter for hierarchical data</strong>
</div>

<div align="center">
  A Python file converter for hierarchical data delivering simple, flexible and dynamic experiences.
</div>

<br>

<div align="left">
  <a href="https://travis-ci.org/jzeuner/konbata">
    <img src="https://travis-matrix-badges.herokuapp.com/repos/jzeuner/konbata/branches/master/1" alt="Flake8 status" />
  </a>
   <strong> Flake8</strong>
  <br>
  <a href="https://travis-ci.org/jzeuner/konbata">
    <img src="https://travis-matrix-badges.herokuapp.com/repos/jzeuner/konbata/branches/master/2" alt="Unittest status" />
  </a>
  <strong> Unittest</strong>
  <br>
  <a href="https://travis-ci.org/jzeuner/konbata">
    <img src="https://travis-matrix-badges.herokuapp.com/repos/jzeuner/konbata/branches/master/3" alt="Code-coverage status" />
  </a>
  <strong> Code-Coverage</strong>
</div>

<br>

#### What is it?
Konbata is a python libary, that allows you to covert a file.
It formats the content of the input file into the output format, by using an internal data structure.

At least, this is the goal of the project.
It can also be used as an tool in the terminal.

#### Why does the world need this?
Simple, there are just too many file formats (see some file formats below).
And almost every tool needs its data in another file format.
This is where konbata comes in place, it serves as interface between tools and file formats.


Just a list of some file formats:
xml, csv, json, html, txt, ...

## Usage
```
konbata.py [-h] [-sh] [-g] [-del DELIMITER] [-opt OPTIONS]
                input_file output_file

positional arguments:
  input_file            Path of input file
  output_file           Path of output file

optional arguments:
  -h, --help            show this help message and exit
  -sh, --show           Show output file
  -g, --get             Get output file
  -del DELIMITER, --delimiter DELIMITER
                        Set input delimiter: -del ';'
  -opt OPTIONS, --options OPTIONS
                        Additional Options
```

## License
[MIT License](https://github.com/jzeuner/konbata/blob/master/LICENSE)

## Documentation
To be added.

[Wiki](https://github.com/jzeuner/konbata/wiki)

## Discussions and Development
Feel free to contact me (e.g via Github) or to contribute in the project.

## Contribute to Konbata
All kind of contributions are welcome!

[Contribution Guideline](https://github.com/jzeuner/konbata/wiki/Contribution-Guideline)

A detailed guide, has to be added.

## Example
```python
# TODO
```

```console
foo@bar:~$ python konbata.py /test/inputfile.csv /test/outputfile.xlsx
```

## Supported Formats
| Format | Status | Basic Convert | Extended Convert  |
|--------|--------|---------------|-------------------|
| txt    | Active | True          | False             |
| csv    | Active | True          | False             |
| xlsx   | Active | True          | False             |
| xml    | -      | -             | -                 |
| json   | -      | -             | -                 |
| YAML   | -      | -             | -                 |
| ...    | -      | -             | -                 |
