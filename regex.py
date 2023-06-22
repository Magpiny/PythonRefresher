"""
REGULAR EXPRESSIONS
A regular expression is a special sequence of characters that helps you match or find other 
strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions 
are widely used in UNIX world.

The Python module re provides full support for Perl-like regular expressions in Python.

import re

findall ->	Returns a list containing all matches
search ->	Returns a Match object if there is a match anywhere in the string
split  ->	Returns a list where the string has been split at each match
sub	   ->   Replaces one or many matches with a string

meta characters -> Characters with special meaning in regex

[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group

Special sequences: A special sequence is a \ followed by one of the characters in the list below, and has 
                   a special meaning:

\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string "r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of 
a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"


Sets: A set is a set of characters inside a pair of square brackets [] with a special meaning:

[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character 
    in the string

"""

import re

txt = "hello world"

# Regex functions
"""
The findall() function returns a list containing all matches.
The list contains the matches in the order they are found.
If no matches are found, an empty list is returned:
"""
rtxt = re.findall('^hello', txt)
print(rtxt)


# The search function
"""
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned
If no matches are found, the value None is returned
"""
rtxt1 = re.search("\w", txt) # /-> h
print(rtxt1)

# The split() function
stxt = "Good evening world!"
rtxt2 = re.split("\s", stxt) # Split the sentense at every space
print(rtxt2)
# You can control the number of occurrences by specifying the maxsplit parameter:
rsplit = re.split("\s", stxt, 1)
print(rsplit)

# The sub() function replaces the matches with the text of your choice:
rtxt3 = re.sub("Good", "Awesome", stxt)
print(rtxt3)
# You can control the number of replacements by specifying the count parameter:
rsub = re.sub("o", "u", stxt, 2)
print(rsub)

# Match Object
# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.
"""
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""
rtxt4 = re.search(r"\bG\w+", stxt)
print(rtxt4.span()) # -> (0, 4)
print(rtxt4.string) # -> Good evening world
print(rtxt4.group()) # -> Good

# compile() function

phone_number_pattern = re.compile("^\+[254]{3}[0-9]{9}$")
print(phone_number_pattern.search("254701987730"))

email_pattern = re.compile("^[a-zA-Z0-9_]+@{1}[a-z]{0,8}\.{1}[a-z]{3}$")
print(email_pattern.search("samuelwanjare@gmail.com"))


# THE END

