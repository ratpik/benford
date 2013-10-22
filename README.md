Benford
=======
Fraud detection with Benford's law in election data

Was just going through a few awk examples when came across Benford law which states that:

**In real-world data the most frequent leading digit is 1, then 2, and so on.**

So tried it out on some random numeric datasets from recent state elections in India

Repo description:

`fabfile.py` - Code that can be run with `fab analyze --hide=running`

Eg. 

```
westbengal_ls2009
{1: 11, 2: 8, 3: 4, 4: 3, 5: 3, 6: 0, 7: 0, 8: 1, 9: 2}
karnataka
{1: 75, 2: 42, 3: 34, 4: 25, 5: 11, 6: 10, 7: 10, 8: 10, 9: 6}
gujrat
{1: 53, 2: 39, 3: 27, 4: 18, 5: 13, 6: 14, 7: 6, 8: 8, 9: 4}
goa
{1: 8, 2: 11, 3: 3, 4: 7, 5: 2, 6: 3, 7: 1, 8: 2, 9: 3}
uttarpradesh_ls2009
{1: 17, 2: 23, 3: 10, 4: 4, 5: 14, 6: 8, 7: 0, 8: 5, 9: 0}
maharastra
{1: 103, 2: 55, 3: 43, 4: 15, 5: 20, 6: 17, 7: 14, 8: 11, 9: 11}
```

The dictionaries tell the number of times vote margins start with 1, 2, .., 9 respectively.

So for Maharastra, the number of vote margins where the difference is either 1xx, 1xxx or 1xxx is 103. So Benford's law kind of holds true here. Similar observations can be made for other states.

The one liner that does all this analysis is

`cat <file> |awk '{print $NF}'|tr -sc [0-9] '\n'|sort -rn|grep ^<i>|wc -l`

Note that all the data sources have the number of interest (i.e vote margins) as the last number on each line of the respective files.

Explanation:
* `cat <file>` - Prints the file to the standard output
* `awk '{print $NF}'` - Pipes the output of `cat` to `awk` which prints the last token specified by `$NF` for every line
* `tr -sc [0-9] '\n'` - Pipes output of `awk` which is the last token in the file to `tr` which
compresses (i.e elimintates repetition) and retains only the tokens that match `[0-9]` i.e numbers or `\n` i.e the newline character
* `sort -rn` - Reverse, numeric sort
* `grep ^i` - Matches all tokens that start with the character `i`. 
* `wc -l` - Count of all lines that have matched `i`
* 

The fabfile is a python fabric utility to avoid writing more bash.

`random.txt` is a piece of random text from [http://randomtextgenerator.com/]

`plots` hold the plotted data with/without logarithmic scale on one axes. 

Generally it can be observed that 1 has the highest frequency, folowed by 2 and so on. In some cases a rise-fall pattern is observed which is also another derivative of this same law. So if Benford's law is to be held as the sole criteria for election fraud detection, than one can say **that the elections analyzed had no fraud as far as the votes were concerned**.


Data sources below:

Goa - http://en.wikipedia.org/wiki/Goa_legislative_assembly_election,_2012
Maharastra - http://en.wikipedia.org/wiki/Maharashtra_state_assembly_elections,_2009
Gujrat - http://en.wikipedia.org/wiki/Gujarat_legislative_assembly_election,_2012
Karnataka - http://en.wikipedia.org/wiki/Karnataka_Legislative_Assembly_election,_2013


Could not find the 2012 state election detailed report.

UP Lok Sabha 2009 - http://www.rediff.com/election/ls04up.htm
West Bengal Lok Sabha 2009 - http://www.rediff.com/election/ls04wb.htm
