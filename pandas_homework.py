"""
Since I have not done much in Pandas, I'll run through my current assignment and explain what I know and don't know.

Here is a sample of the data set and the code courera provided to load it in, along with my comments. there are about 150 entries in this set. 
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
,? Summer,01 !,02 !,03 !,Total,? Winter,01 !,02 !,03 !,Total,? Games,01 !,02 !,03 !,Combined total
Afghanistan (AFG),13,0,0,2,2,0,0,0,0,0,13,0,0,2,2
Algeria (ALG),12,5,2,8,15,3,0,0,0,0,15,5,2,8,15
Argentina (ARG),23,18,24,28,70,18,0,0,0,0,41,18,24,28,70
Armenia (ARM),5,1,2,9,12,6,0,0,0,0,11,1,2,9,12
....
"""

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='?':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()
# my comments:
"""
first we read in the csv, ignoring the first row and using the first column as the index column, which is the country in this case
Next, the code loops through some matched columns and changes them; "inplace=True" means we are altering the original dataframe in-line
Names are set. The column 'Totals' is dropped. 
"""

###################################################################################################
"""
Question 1
Which country has won the most gold medals in summer games?
"""
df['Gold'].idxmax()  # returns the index value of the highest value found in the 'Gold' column
###################################################################################################
"""
Question 2
Which country had the biggest difference between their summer and winter gold medal counts?
"""
(df['Gold'] - df['Gold.1']).abs().idxmax()
"""
Not sure if this is the best way to do it, but it worked. I believe it works because you can do operations on the Series
in a dataframe and it will return the new data in a dataframe matched with the index intact. Then just call idxmax() to get
the index of the highest value after the operation
"""
###################################################################################################
"""
Question 3
Which country has the biggest difference between their summer gold medal counts and winter gold medal counts 
relative to their total gold medal count? Summer Gold − Winter Gold / Total Gold. Only include countries that 
have won at least 1 gold in both summer and winter.
"""
((df['Gold'] - df['Gold.1'])/df['Gold.2']).abs()[(df['Gold'] > 0) & (df['Gold.1'] > 0)].idxmax()
"""
First is the calulation we were asked to do. Then we filter out 'Gold' and 'Gold.1' values that are not greater 
than 0 as required. Lastly, we get the max as we have done before.
"""
###################################################################################################
"""
Question 4
Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) 
counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function
should return only the column (a Series object) which you created.
"""
s = df['Gold.2'] * 3 + df['Silver.2'] * 2 + df['Bronze']
s.name = 'Points'
###################################################################################################




# The next problems use a different dataset that has over 100 columns and thousands of rows. I will not include it for now 
###################################################################################################
"""
Question 5
Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for 
future questions too...)
"""
census_df[census_df['SUMLEV'] == 50].groupby('STNAME')['CTYNAME'].count().idxmax()
"""
first we make sure we do not include county values equal to the state, where a sum of all county populations 
are held. Next we group by 'STNAME', which will include all the counties for that state. Then we get the count 
of how many rows are in each group and return the index of the max. 
"""
###################################################################################################
"""
Question 6
Only looking at the three most populous counties for each state, what are the three most populous states
(in order of highest population to lowest population)? Use CENSUS2010POP.
"""
dfg = census_df[census_df['SUMLEV'] == 50].groupby('STNAME')['CENSUS2010POP']
dfg.apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()
"""
I had this figured out except for the apply function, which I had not know about yet and found this part of the solution on the internet.  
I think the apply() and nlargest() functions are self explanatory. Verry useful.
"""
###################################################################################################
"""
Question 7
Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
"""
cdf = census_df[census_df['SUMLEV'] == 50].set_index('CTYNAME').loc[:, 'POPESTIMATE2010': 'POPESTIMATE2015']
(cdf.max(axis=1) - cdf.min(axis=1)).idxmax()
###################################################################################################
"""
Question 8
In this datafile, the United States is broken up into four regions using the "REGION" column.
Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
"""
dff =  df[((df['REGION'] == 1) | (df['REGION'] == 2)) & (df['POPESTIMATE2015'] > df['POPESTIMATE2014'])]
dff[dff['CTYNAME'].str.startswith('Washington')][['STNAME', 'CTYNAME']]
