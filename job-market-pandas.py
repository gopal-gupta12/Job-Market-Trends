import pandas as pd 
from collections import Counter
df = pd.read_csv('job_market.csv')
df['Date-Posted'] = pd.to_datetime(df['Date-Posted'])

# Data Cleaning :-
df.isnull() # Detects rows with null values
df = df.dropna() # Drops rows having null values
df.loc[df['Job-Title'] == 'Data Analyst/Scientist','Skills'] = 'Python; Tableu; R; MachineLearing'

# Data Selection / Data Filtering:-
# Top Niches 
top_title = df['Job-Title'].value_counts()
top_title = top_title.sort_values(ascending= False).head()
top_title.to_csv('top_title.csv') #Saves the top titles in a csv file to ensure that we won't have to calcuate it again.

# Companies offering higher salaries
top_salary = df.groupby(['Company-Name','Job-Title','Skills'])['Salary'].sum()
top_salary = top_salary.head().sort_values(ascending= False)
top_salary.to_csv('top_salary.csv') #Saves the top Salaries in a csv file to ensure that we won't have to calcuate it again.

# Top 5 cities with job opportunities
job_location = df['Location'].value_counts()
job_location = job_location.sort_values(ascending= False).head()
job_location.to_csv('job_location.csv') #Saves the locations having higher jobs in a csv file to ensure that we won't have to calcuate it again.

#Months with higher Postings
df['Month'] = df['Date-Posted'].dt.strftime("%b") # Converting '2025-01' into 'jan'
monthly_posts = df.groupby('Month').size()
monthly_posts = monthly_posts.sort_values(ascending= False)
monthly_posts.to_csv('monthly_posts.csv') #Saves the monthly postings in a csv file to ensure that we won't have to calcuate it again.
print(monthly_posts)

#Most Common skills among all the postings
all_skills = df['Skills'].dropna().apply(lambda x :[skill for skill in x.split(';')])
flat_skills = [skill for sublist in all_skills for skill in sublist ]
demanded_skills = pd.Series(Counter(flat_skills)).sort_values(ascending= False).head()
demanded_skills.to_csv('demanded_skills.csv') #Saves the demanded skills in a csv file to ensure that we won't have to calcuate it again.
