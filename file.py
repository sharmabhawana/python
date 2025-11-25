"""Stream-A stream is a simply a sequence of bytes that flows into or out of our program
It's an abstract representation of an input or output device
Type of Stream
!.Binary or Byte Streams
2.Character Stream
Working with file:-
Files are storage compartments on your computer that are managed by operating system
Python built-in open() function creates a Python file object,which serves as a link to a file residing on your machines.
Mode:-
r->Open for reading only.Start at beginning of file.
r+->Open for reading and writing.Starting at begining of file.
w->Open for writing only.Remove all previous content,if file doesn't exist,create it.
w+->open for writing mode.Truncates the file(effectively overwritting it).If the file doesn't exist,it will attempt tom create the file,it deletes all the informatin in the file when the file is opened.
a->open writing,but start at the end of current content.
a+->Open for reading and writing,starts at end and creates file if neccessary."""
