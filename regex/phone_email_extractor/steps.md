# steps:
1. Get the text off the clipboard.
2. Find all phone numbers and email in the text. 
3. Copy them onto the clipboard. 

## step1:
* Use the ```pyperclip``` module to copy and paste string. 
* Write a regex for phone number extractor.
* Write a regex for email address extractor.
* Find all matches, not just the first match, of both regexes.
* Neatly format the matched strings into a single string to paste.
* Display some kind of message if no matches were found in the text.