# Reading and Writing Files:

## Files and File Paths:
A file has to key properties: a filename(usually written as one word) and a path. The path specifies the location of a file on the computer. The part of the filename after the last period is called the file’s extension and tells us a file’s type. folder names and fi lenames are not case-sensitive on Windows and macOS, they are case-sensitive on Linux.

## Backslash on Windows and Forward Slash on macOS and Linux: 
On Windows, paths are written using backslashes **(\)** as the separator between folder names. The macOS and Linux operating systems, however, use the forward slash **(/)** as their path separator. To solve this we will use Path() from pathlib. If we pass it the string values of individual file and folder names in our path, Path() will return a string which is a file path cosists of the correct path separators.
```bash
>>> from pathlib import Path
>>> Path('spam', 'bacon', 'eggs')
PosixPath('spam/bacon/eggs')
>>> str(Path('spam', 'bacon', 'eggs'))
'spam/bacon/eggs'

# in case of windows
>>> Path('spam', 'bacon', 'eggs') 
WindowsPath('spam/bacon/eggs')
>>> str(Path('spam', 'bacon', 'eggs')) 
'spam\\bacon\\eggs'
```
On Windows, Path('spam', 'bacon', 'eggs') returned a WindowsPath object for the joined path, represented as WindowsPath('spam/bacon/eggs'). Even though Windows uses backslashes, the WindowsPath representation in the interactive shell dis-plays them using forward slashes. Notice that the backslashes are doubled in string representation of windows path because each backslash needs to be escaped by another backslash character.
    On Windows, the backslash separates directories, so we can’t use it in filenames. However, we can use backslashes in filenames on macOS and Linux. So while Path(r'spam\eggs') refers to two separate folders (or a fi le eggs in a folder spam) on Windows, the same command would refer to a single folder (or fi le) named spam\eggs on macOS and Linux. For this reason, it’s usually a good idea to always use forward slashes in our Python code.

## Using the / operator to join paths:
One of the first two operand must be a path object. Other wise there will be an type error. This **/** operator is better than **+** and **join()**. And will work with all OS.
```bash
>>> 'b' / Path('C')
PosixPath('b/C')
>>> Path('spam')/'bacon'/'eggs'
PosixPath('spam/bacon/eggs')
```

## Current working directory:
Every program that runs on our computer has a current working directory, or cwd. Any filenames or paths that do not begin with the root folder are assumed to be under the current working directory.
    We can get the CWD as a string value with the ```Path.cwd()``` function and change it using ```os.chdir()```.
```bash
>>> from pathlib import Path
>>> import os
>>> Path.cwd()
PosixPath('/data/data/com.termux/files/home/workspace/automate_boring_stuff_with_python')
>>> os.chdir('/data')
>>> Path.cwd()
PosixPath('/data')
```
In case we try to change to a directory that doesn,t exist we will get an ```FileNotFoundError```
```bash
>>> os.chdir('/roast')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/roast
```

## The Home Directory:
All users have a folder for their own files on the computer called the ```home directory```. One can get a Path object of the home folder by calling ```Path.home()```.
```bash
>>> Path.home()
PosixPath('/data/data/com.termux/files/home')
```
The home directories are located in a set place depending on your operating system:
* On Windows, home directories are under C:\Users.
* On Mac, home directories are under /Users.
* On Linux, home directories are often under /home.
Your scripts will almost certainly have permissions to read and write the files under your home directory, so it’s an ideal place to put the files that your Python programs will work with.

## Absolute vsc Relarive Paths:
There are two ways to specify a file path:
* Absolute path, which always begins with the root folder.
* Relative path, which is relative to the program's current working directory.
```.``` and ```..``` denotes present directory and parent directory respectively.

## Creating new folders using the os.makedirs() function:
This will create directory and subdirectories.
```bash
>>> os.makedirs(Path('hover', 'board', 'soup'))
>>> Path.cwd()
PosixPath('/data/data/com.termux/files/home')
>>> os.chdir('hover/board')
>>> Path.cwd()
PosixPath('/data/data/com.termux/files/home/hover/board')
```
To make a directory from a Path object, call the mkdir() method.
```bash
>>> (Path.cwd() / 'drum').mkdir()
>>> Path.cwd()
PosixPath('/data/data/com.termux/files/home/hover/board')
>>> os.chdir('drum')
>>> Path.cwd()
PosixPath('/data/data/com.termux/files/home/hover/board/drum')
```
Note that mkdir() can only make one directory at a time; it won’t make several subdirectories at once like os.makedirs().

## Handling Absolute and Relative Paths:
The ```pathlib``` module provides methods for checking whether a given path is an absolute path and returning the absolute path of a relative path.
* is_absolute() method called on a path object and it will return true if it represents an ansolute path or false if it represents a reltive path.
```bash
>>> Path('/drum').is_absolute()
True
>>> Path('/dune').is_absolute()
True
>>> Path('dune').is_absolute()
False
```
To get absolute path from relative path, which is relative to another path you just place that another path infront of relative path.
```bash
>>> Path.home() / Path('hill')
PosixPath('/data/data/com.termux/files/home/hill')
>>> Path.cwd() / Path('hill')
PosixPath('/data/data/com.termux/files/home/hover/board/drum/hill')
```
The os.path module also has some useful functions related to absolute and relative paths:
• Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.
• Calling os.path.isabs(path) will return True if the argument is an abso-lute path and False if it is a relative path.
• Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.

## Getting parts of file Path:
The parts of a fi le path include the following:
* The anchor, which is the root folder of the fi lesystem 
* On Windows, the drive, which is the single letter that often denotes a physical hard drive or other storage device 
* The parent, which is the folder that contains the file 
* The name of the file, made up of the stem (or base name) and the suffix (or extension)
```bash
>>> p = Path('/home/bold/date.txt')
>>> p.anchor
'/'
>>> p.parent
PosixPath('/home/bold')
>>> p.stem
'date'
>>> p.suffix
'.txt'
>>> p.parents[0]
PosixPath('/home/bold')
>>> p.parents[1]
PosixPath('/home')
```

## Finding File Sizes and Folder Contents:
* Calling os.path.getsize(path) will return the size in bytes of the fi le in the path argument.
* Calling os.listdir(path) will return a list of fi lename strings for each fi le in the path argument.
```bash
>>> os.listdir(str(Path.cwd()))
['.git', '.gitignore', 'LICENSE', 'regex', 'input_validation', '.venv', 'reading_writing_files']
>>> os.path.getsize('.gitignore')
6
```

## Using Glob patterns:
If we want to work with specific files we use ```glob()``` of Path object. Glob pattern is simplified version of regular expression. The glob() returns a genarator object.
```bash
>>> list(Path.cwd().glob('*'))
[PosixPath('/data/data/com.termux/files/home/.termux'), PosixPath('/data/data/com.termux/files/home/.bash_history')
    --snip--
PosixPath('/data/data/com.termux/files/home/hover')]
```
The glob pattern '*.txt' will return fi les that start with any combina-tion of characters as long as it ends with the string '.txt'. In contrast with the asterisk, the question mark (?) stands for any single character.

## Checking Path Validity:
if P is a path object then:
* Calling p.exists() returns True if the path exists or returns False if it doesn’t exist.
* Calling p.is_file() returns True if the path exists and is a fi le, or returns False otherwise.
* Calling p.is_dir() returns True if the path exists and is a directory, or returns False otherwise.
* P.exist() we can check for whether usb drive or dvd is attached. Ofcourse this P is path object of the usb drive or dvd path.  

## The file Reading/Writing process:
