import matplotlib.pyplot as plt 
import pandas as pd 
df = pd.read_csv('job_market.csv')

# Importing all the files to avoid the repetative computations : 
top_title = pd.read_csv('top_title.csv', index_col= 0)
monthly_posts = pd.read_csv('monthly_posts.csv', index_col= 0)
job_location = pd.read_csv('job_location.csv', index_col= 0)
demanded_skills = pd.read_csv('demanded_skills.csv', index_col= 0)

#Creating Subplots to visualize all the data in differents type of graphs/ charts.
fig , plots = plt.subplots(2,2 , figsize = (12, 7))
plt.suptitle("Job Market Trend Dashboard", fontweight = 'bold')

# Location having higher job opportunities (Top 5):
top_loc = job_location.index[0]
top_value = job_location.values[0]
plots[0,0].bar(job_location.index , job_location.values.flatten() , color = 'teal')
plots[0,0].annotate(
    f"Top : {top_loc}",
    xy = (top_loc , top_value),
     xytext= (top_loc, top_value + 1.3),
    arrowprops = dict(arrowstyle = '->'),
    ha = 'center'
)
plots[0,0].set_title("Jobs Per Location", style = 'italic', family = 'serif')
plots[0,0].set_ylabel("City")
plots[0,0].tick_params(axis = 'x', rotation = 35)

# Job Title having higher opportunities (Top 5):
plots[0,1].pie(top_title.values.flatten() , 
               labels = top_title.index ,
               autopct = "%1.1f%%",
               shadow = True ,
               startangle = 130,
               labeldistance = 1.1)

plots[0,1].set_title('Jobs Per Title', style = 'italic', family = 'serif')

# Monthly Jobs postings :
plots[1,0].plot(monthly_posts.index , monthly_posts.values,
                marker = 'o', color = 'green')
plots[1,0].set_title("Monthly Job Postings", style = 'italic', family = 'serif')
plots[1,0].set_xlabel("Month")
plots[1,0].set_ylabel("No of jobs")
plots[1,0].grid(axis ='y', linestyle = '--')

# Top skills (Top 5):
top_skills = demanded_skills[::-1]
plots[1,1].barh(top_skills.index , top_skills.values.flatten() ,
                color = 'steelblue')
plots[1,1].set_title('The Most Demanding Skills', style = 'italic', family = 'serif')
plots[1,1].set_xlabel('No of Companies asks')

plots[1,1].grid(axis = 'x', linestyle = '--', alpha = 0.5)

# Displays all the plots in a single plot :
plt.tight_layout() # To Make Sure that all the subplots lies inside the figure , none of them crosses the figure's boundary.
plt.show()