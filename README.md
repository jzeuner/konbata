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

<div align="center">
  <a href="https://github.com/jzeuner/konbata/actions">
    <img src="https://github.com/jzeuner/konbata/workflows/Flake8/badge.svg" alt="Flake8 status" />
  </a>
  <a href="https://github.com/jzeuner/konbata/actions">
    <img src="https://github.com/jzeuner/konbata/workflows/TestCases/badge.svg" alt="Unittest status" />
  </a>
  <a href="https://github.com/jzeuner/konbata/actions">
    <img src="https://github.com/jzeuner/konbata/workflows/CodeCoverage/badge.svg" alt="Code-coverage status" />
  </a>
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

## Where to get it?
The source code is available on GitHub: [https://github.com/jzeuner/konbata](https://github.com/jzeuner/konbata)

You can install the latest version with pip.
```console
foo@bar:~$ pip install konbata
```


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
