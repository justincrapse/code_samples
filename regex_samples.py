# just including the regex part of the solution as most of the coding part of the solutions are quite basic

###################################################################################################
"""
strip the links and the text name from the html pages
input: 
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>   
output:
http://www.quackit.com/html/tutorial/html_links.cfm,Example Link
http://www.quackit.com/html/examples/html_links_examples.cfm,More Link Examples...
"""
re.findall(r'<a href="(.+?)".+?(?<=>)(.+?)(?=<)', s, re.DOTALL)
###################################################################################################
"""
Print a single line containing all of the unique tag names found in the input. Your output tags should be semicolon-separated
and ordered lexicographically (i.e.: alphabetically). Do not print the same tag name more than once.
input: 
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
output: a;div;p
"""
re.findall(r'</?(\w+)/?[> ]', html)
###################################################################################################
"""
determin how man instances of a substring (passed in as sub_s) is found in a string.
substring must be surrounded by letters (not allowed at beggining or end of word)
input: string: existing pessimist optimist this is substring: is
output: 3
"""
regex = r'\B({})\B'.format(sub_s)
    print(len(re.findall(regex, text)))
###################################################################################################
"""
detect if the text contained in each of the lines represents an (a)IPv4 address (b)IPv6 address or (c)None of these.
input: 
2r01:0dr8:0000:0000:0g00:ff00:0042:8329  
121.18.19.20 
101.148.19.256 
2001:0db8:0000:0000:0000:ff00:0042:8329  
output:
Neither
IPv4
Neither
IPv6

* I chose to do a pure regex solution for IPv4, though I think it is a much more elegant solution to use python
for the logic of checking the value range. 
"""
ipv4_num = r'(25[1-5]|2[1-4]\d|1\d{2}|\d{1,2})'
regex = r'^({0}\.){{3}}{0}$'.format(ipv4_num)
for i in range(int(input())):
    entry = input()
    if ':' in entry and re.match(r'^([\da-f]{1,4}:){7}[\da-f]{1,4}$', entry):
        print('IPv6')
    elif re.match(regex, entry):
        print('IPv4')
    else:
        print('Neither')
###################################################################################################
"""
Your task is to write a program, which accepts as input, a C or C++ or Java program and outputs only the 
comments from those programs.

input:
// my  program in C++

#include <iostream>
/** playing around in
a new programming language **/
using namespace std;

int main ()
{
  cout << "Hello World";
  cout << "I'm a C++ program"; //use cout
  return 0;
}

output: 
// my  program in C++
/** playing around in
a new programming language **/
//use cout
"""
for i in re.findall(r'\/\*.*?\*\/|\/\/.*?$', text, re.DOTALL|re.M):
    clean = re.sub(r'(?<=\n)\s+', '', i)
    print(clean)
###################################################################################################
"""
verify weather a pair of coordinate is valid or invalid. May or may not have a plus or minus sign preceding the number
Numbers may be decimal or integer values. No preceeding zeros alowed. Must contain one comma and one space after x value. 
No space between numbers and brackets. 
For a valid (latitude, longitude) pair: 
-90<=X<=+90 and -180<=Y<=180. 

* In this solution, I chose to break out part of the contstaints out of the regex as it would have become unruly. 
"""
pair_values = re.findall(r'\([+\-]?(?!0)(\d{1,3}(?:\.\d+)?)\, [+\-]?(?!0)(\d{1,3}(?:\.\d+)?)\)', pair_raw)
    if pair_values and 0 <= float(pair_values[0][0]) <= 90 and 0 <= float(pair_values[0][1]) <= 180:
        print('Valid')
    else:
        print('Invalid')
###################################################################################################
re.match(r'^([\dA-F]{2}-){5}[\dA-F]{2}$', s)  # matches a general Mac Address format
