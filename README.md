Benford
=======
Fraud detection with Benford's law in election data

Was just going through a few awk examples when came across Benford law which states that:

In real-world data the most frequent leading digit is 1, then 2, and so on.

So tried it out on some random numeric datasets from recent state elections in India

Repo description:

`fabfile.py` - Code that can be run with `fab analyze`

Eg. 
'''
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
'''

The dictionaries tell the number of times vote margins start with 1, 2, .., 9 respectively.

So for Maharastra, the number of vote margins where the difference is either 1xx, 1xxx or 1xxx is 103. So Benford's law kind of holds true here. Similar observations can be observed for other states.


Data sources below:

Goa - http://en.wikipedia.org/wiki/Goa_legislative_assembly_election,_2012
Maharastra - http://en.wikipedia.org/wiki/Maharashtra_state_assembly_elections,_2009
Gujrat - http://en.wikipedia.org/wiki/Gujarat_legislative_assembly_election,_2012
Karnataka - http://en.wikipedia.org/wiki/Karnataka_Legislative_Assembly_election,_2013


Could not find the 2012 state election detailed report.

UP Lok Sabha 2009 - http://www.rediff.com/election/ls04up.htm
West Bengal Lok Sabha 2009 - http://www.rediff.com/election/ls04wb.htm
