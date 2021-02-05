# pyvcfconverter
![Alt text](https://github.com/evlanoff/pyvcfconverter/raw/main/file.ico "Logo")

pyvcfconverter - it's a small utility which converts exported contacts from Android OS to a suitable contact format for Apple iOS.

### Platforms

The script was tested on

* Windows 1809 & 2004
* macOS Catalina 10.15.7
* GNU/Linux debian

### Requirements
* python3

### How it works?

* The script change a version of contacts from 2.1 to 3.0.
* Removes unexpected line breaks inside encoded line e.g. =\r\n
* Decode encoded quoted-printable strings to UTF-8 human readable text and save as copy file.

### Usage
The script can be used in two ways: drag & drop or called from Terminal.

**Windows 10**

:warning: :warning: :warning: 

The executable version compiled by pyinstaller. False alarm by Windows Defender detected as [Trojan:Win32/Wacatac.DE!ml](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:Win32/Wacatac.DE!ml&ThreatID=2147757793). A browser may to block downloading file. To solve issue you'll just need to add trusted exception into Windows Defender and try to download file again. If you don't trust just see compiling section below.

Drag & drop your contacts file on executable file and a few seconds later near with contacts will appear a converted copy. The script require only 1 file to drag & drop per a time.

Another way from powershell/CMD.exe call script like this
```
python.exe pyvcfconverter.py contacts.vcf
```

### Compiling
For the manual compiling under Windows you should to install:

1. [python3](https://www.python.org/)
2. [pyinstaller](https://pypi.org/project/pyinstaller/)

After installation ```python3``` use ```pip3``` package manager for installation pyinstaller.
```
pip3 install pyinstaller
```
After installation you should to compile it like this:
```
pyinstaller.exe --onefile --icon=file.ico* .\path\to\pyvcfconverter.py
```
\* — optionally, if you are omit this step will be used standard python icon

---

Небольшая утилита для преобразования файла контактов в формате VCF.

Скрипт написан на python3 и служит для того, чтобы переносить контакты с Android OS на Apple iOS. Скрипт конвертирует файл контактов для удобного импорта в контакты Apple iOS через Apple iCloud.

### Как работает скрипт

* Скрипт меняет версию контактов с 2.1 на 3.0
* удаляет из закодированных quoted-printable строк ошибочные переносы строк, такие как =\r\n.
* Декодирует закодированные строки в человекочитаемый текст в UTF-8 и сохраняет в отдельный файл.

### Использование

**Windows 10**

:warning: :warning: :warning: 

Для удобства, чтобы не устанавливать python3 на компьютер, файл был скомпилирован - необходимые для запуска файлы собраны в 1 исполняемый файл.  Windows Defender детектирует его как [Trojan:Win32/Wacatac.DE!ml](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:Win32/Wacatac.DE!ml&ThreatID=2147757793), но это ложное срабатывание. Чтобы файл удалось сохранить на компьютер просто добавьте разрешительное исключение в антивирус и повторите загрузку. Если вы не доверяете данной программе, то смотрите раздел Компиляция ниже.

Перетащите на скрипт или приложение Windows файл с контактами, подождите некоторое время, рядом с оригинальным файлом контактов появится конвертированная версия. За раз перетаскивайте только 1 файл.

Либо воспользуйтесь коммандной строкой для запуска скрипта

```
python.exe pyvcfconverter.py contacts.vcf
```

### Компиляция
Для самостоятельной компиляции скрипта для Windows вам необходимо установить:
1. [python3](https://www.python.org/)
2. [pyinstaller](https://pypi.org/project/pyinstaller/)

После установки ```python3``` воспользуйтесь менеджером пакетов ```pip3``` для установки пакета pyinstaller.
```
pip3 install pyinstaller
```

Команда для компиляции должна выглядеть следующим образом

```
pyinstaller.exe --onefile --icon=file.ico*  .\path\to\pyvcfconverter.py
```
\* — необязательно, если не указывать, то будет использована стандартная иконка python

---

Thanks for the awesome icon [Icons made by **iconixar** from Flaticon](https://www.flaticon.com)
