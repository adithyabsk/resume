# Adithya's Resume

Based on [yaml-resume](https://github.com/notsag/yaml-resume)

**Setup**

* [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html):
For "printing" the pdf, converts html files to pdf without a browser
* Fonts
  * You need to install the following Google Fonts locally for the pdf printing
  to work--drag the `.otf` files into FontBook
  * [Nunito Sans](https://fonts.google.com/specimen/Nunito+Sans)
  * [Cutive Mono](https://fonts.google.com/specimen/Cutive+Mono)

```shell
# WeasyPrint requirements
brew install python pango libffi
# local package
pip install -e .
```

**Usage**

```shell
./refresh.sh
```
