# Building a Streamlit Application for my Data Analysis with Python Programming Project.
# Importing the necessary libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time
import requests
import plotly as pt
import plotly.express as px
import streamlit as st
from PIL import Image

# Setting the page layout configurations.
st.set_page_config(page_title="The Ultimate Career Decision-Making Guide:- Data Jobs", page_icon=":bar_chart:", layout="centered")
# The App title and tagline.
st.title("The Ultimate Career Decision-Making Guide:- Data Jobs")
st.write("Navigating the Data-Driven Career Landscape: A Deep Dive into Artificisl Intelligence, Machine Learning, and Data Science Salaries. \n"
         "Enabling you to make the most informed career decisions on AI, ML, and Data Science spaces.")

# Creating an expandable box about this App.
with st.expander("About This App"):
    st.write("This app uses global salaries dataset provied by professionals in the AI, ML, and Data Science spaces. \n"
             "It is updated weekly, therefore, whenever this App is launched, it automatically picks the updated data and \n"
             "reflects the changes in the insights visualizations. The updates do not affect or change the interpretations \n"
             "and descriptions of the insights offered.\n The salary in Kenyan shillings was calculated by requesting \n"
             "the current exchange rate from the internet and multiplied the salaries in the 'salary_in_usd' column with \n"
             "the exchange rate. A new column named 'Salary_in_KES was added to the dataset. Similarly, since the employee_residence and company_location \n"
             "columns contained the same country code, a function was defined to create a new column named 'employee_company_location' \n"
             "that combines both the employee_residence and company_location columns into a single column. \n"
             "The 'salary' and 'salary_currency' columns were dropped from the dataset. \n")
    # Loading an image from a local file.
    image_path = r"C:\Users\succe\OneDrive\Desktop\ADS-Final-Project\Image_Title.PNG" 
    image = Image.open(image_path)
    st.image(image, caption='Figure 1', use_column_width=True)
    st.write("Believe It!! These are just but examples of the available spaces to take Advantage of \n"
         "and Realize Your Dreams in no time.")

# Creating an expandable box about the App's Targeted audience.
with st.expander("The Targeted Audience"):
    st.write("Everyone who is looking for a career transition into the world of advancing technologies. \n" 
    "Whether you are a newbie, intermediate, or professional we got you covered to make the right decisions. \n"
    "The Data Jobs Guide will help you make the most informed career decisions.")

@st.cache_data
def load_engineered_data():
    url = 'https://ai-jobs.net/salaries/download/salaries.csv'
    data = pd.read_csv(url)
    #df= pd.DataFrame(data)
    data = data.drop(['salary', 'salary_currency'], axis=1)
    data['experience_level'] = data['experience_level'].replace ({'EN': 'Entry-level/Junior (EN)', 
                                                                  'MI': 'Mid-level/Intermediate (MI)',
                                                                  'SE': 'Senior-level/Expert (SE)',
                                                                  'EX': 'Executive-level/Director (EX)'})
    data['employment_type'] = data['employment_type'].replace ({'PT': 'Part-time (PT)',
                                                                'FT': 'Full-time (FT)',
                                                                'CT': 'Contract (CT)',
                                                                'FL': 'Freelance (FL)'})
    data['remote_ratio'] = data['remote_ratio'].replace ({0: 'No Remote Work (<20%)', 
                                                          50: 'Partially Remote/Hybrid (==50%)',
                                                          100: 'Fully Remote (>80%)'})
   
    data['company_size'] = data['company_size'].replace ({'S': 'Small (<50 Employees)',
                                                          'M': 'Medium(50-250 Employess)',
                                                          'L': 'Large(>250 Employees)'})
    
    #Create a function that:
        #1. Gets the current market exchange rate from the internet.
        #2. Convert salary_in_usd into Shillings by multiplying it by the exchange rate.
        #3. And then add the new column to the DataFrame with the new salary in Kenya Shillings.""" 
        # Import the requests library for processing HTTP requests that are sent and received from the exchange rate website.
    api_key = "YOUR_API_KEY"
    base_url = 'https://open.er-api.com/v6/latest/USD'
    def get_exchange_rate():
        try:
            response = requests.get(base_url, params={'apikey': api_key})
            data = response.json()
            exchange_rate = data['rates']['KES']
            return exchange_rate
        except Exception as e:
            print(f"Error fetching exchange rate: {e}")
        return None
    exchange_rate = get_exchange_rate()
    data['Salary_in_KES'] = data['salary_in_usd'] * exchange_rate
    data['employee_company_location'] = data.apply(lambda row: "same country" if row['employee_residence'] == row['company_location'] else 'different country', axis=1)
    return data

data = load_engineered_data()

if st.checkbox("The Salaries Raw Dataset. \n"
               "Check the Box to the Left by Clicking Inside It Once."):
    st.subheader("The Modified Raw Data")
    st.write(data.columns.tolist())
    st.write(data)
    # Write a warning notice to the user about the normal use case of the Application.
with st.expander("WARNING: User Usecases"):
    st.write("No guarantee you will be successful in any of the spaces you may choose to take advantage of.\n"
    "This is simply a guide to help you make the most informed career decisions on the available spaces \n"
    "to help you realize your dreams. Since the data analyzed is continously updated unanonymously without bias,\n"
    "contributed by professionals in this fields, there are high chances of success with our guide.")

# Data Visualization
st.title("The Ultimate and Well Curated Career Insights Visualizations.")
st.write("Check out the impressing & impactiful knowledge based visuals to make the ultimate career decisions.")

# The first visualization is a bar chart showing the average salary paid per work_year.
def Insight_1():
    st.title("1. Average Salary Paid Per Employment_Type")
    SalaryinKES_EmploymentType = data.groupby('employment_type')['Salary_in_KES'].mean().reset_index()
    fig_SalaryinKES_EmploymentType = px.bar(SalaryinKES_EmploymentType, x='employment_type', y='Salary_in_KES')
    st.plotly_chart(fig_SalaryinKES_EmploymentType)
    st.write("Figure 1: The chart shows that those who were employed permanent earned more followed by those on contract.\n "
    "The chart also shows that those who were employed as part-time earned less than those on full-time.\n"
    "The chart also shows that those who worked as freelancers earned less than those on contract.\n"
    "Therefore, consider going for those employment types that are highly paid such as Full-Time positions.")

# Pie-Chart Visualization.
def Insight_2():
    st.title("2. Salary Distribution Over Each Work_Year")
    # Generating value counts for categorical variables
    vis1_work_year = data['work_year'].value_counts()
    # Creating a pie chart for Work Year distribution
    plt.figure(figsize=(8, 8))
    plt.pie(vis1_work_year.values, labels=None, autopct='%1.2f%%', startangle=40, colors=sns.color_palette('Set1'), pctdistance=0.7)
    #plt.title('The Salaries Paid in Each Work_Year', fontsize=16)
    plt.legend(vis1_work_year.index, title="Work_Year", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(plt)
    st.write("Figure 2: The pie chart shows the distribution of the salary paid by each work_year.\n"
             "More salaries were paid in 2023 as compared to other work_years.\n"
    " This shows that the opportunities in these spaces are increasing by the day. \n"
    "It is essential to be part of the growth by starting or transitioning your career into one of the technology spaces. \n"
    "To persue and actualize your dreams you can join data science related courses in institutions such as Africa Data School or Moringa.")

def Insight_3():
    st.title("3. Salary Distribution Over Remote_Ratios")
    # Generating value counts for categorical variables
    vis2_remote_ratio = data['remote_ratio'].value_counts()
    # Creating a pie chart for Remote Ratio distribution
    plt.figure(figsize=(8, 8))
    plt.pie(vis2_remote_ratio.values, labels=None, autopct='%1.2f%%', startangle=40, colors=sns.color_palette('Set1'))
    #plt.title('Salary Distribution Based on the Different Remote_Ratios', fontsize=16)
    plt.legend(vis2_remote_ratio.index, title="Remote_Ratio", loc="lower center", bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(plt)
    st.write("Figure 3: The chart shows that most of the salary across the fields was paid to employees under the 'No Remote Work (<20%)' model\n"
             "indicating that most of the hiring companies represented on the dataset value physical presence of employees.\n"
             "This trend may not be favorable for people located in different countries with the companies they are seeking to be employeed in. \n"
             "The chart also shows that the 'Fully Remote (>80%)' model had the second highest salaries paid followed by the 'Partially Remote/Hybrid (==50%)' model. \n"
             "Therefore, it is easy for a Kenyan to train and get hired remotelly or partially remote by global companies.")

def Insight_4():
    st.title("4. Salary Distribution by Company_Size")
    # Generating value counts for categorical variables
    vis3_company_size = data['company_size'].value_counts()
    # Creating a pie chart for Company Size distribution
    plt.figure(figsize=(8, 8))
    plt.pie(vis3_company_size.values, labels=None, autopct='%1.2f%%', startangle=40, colors=sns.color_palette('Set1'))
    #plt.title('Salary Distribution by Company Size', fontsize=16)
    plt.legend(vis3_company_size.index, title="Company_Size", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(plt)
    st.write("Figure 4: The pie chart shows the distribution of the salary paid by company size.\n"
    "The 'Medium' company size has the highest salaries paid out to employees. The 'Large' company size has the second highest salaries paid.\n"
    "The 'Small' company size has the third highest salaries paid.\n This means that small and medium enterprises should be the prime target since the salary \n"
    "distributions indicates their appeciation and adoption of these technologies and people with relevant skills. This is attributed to their fast\n"
    "growth rates and value for innovation to fuel strategic and competitive development. There are high chances of career growth or \n"
    "even startups success because AI, ML, & Data Science adoption is high in the small and medium companies.")

def Insight_5():
    st.title('5. Salary Distribution by Experience_Level')
    # Generating value counts for categorical variables
    vis4_experience_level = data['experience_level'].value_counts()
    # Creating a pie chart for Experience Level distribution
    plt.figure(figsize=(8, 8))
    plt.pie(vis4_experience_level.values, labels=None, autopct='%1.2f%%', startangle=40, colors=sns.color_palette('Set1'))
    #plt.title('Salary Distribution by Experience_Level', fontsize=16)
    plt.legend(vis4_experience_level.index, title="Experience_Level", loc="lower center", bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(plt)
    st.write("Figure 5: The pie chart shows the distribution of the salary by experience level.\n"
    "The 'Entry-level/Junior (EN)' experience level has the lowest salaries paid. The 'Mid-level/Intermediate (MI)' experience level \n"
    "has the medium or second lowest salaries paid. The 'Senior-level/Expert (SE)' experience level has the highest salaries paid.\n"
    "The 'Executive-level/Director (EX)' experience level has the fourth highest salaries paid.\n"
    "There is a clear indication that as experience level increases, the salaries paid increases. \n"
    "Therefore, career advancement or transition into these spaces is worthy considereation as experience comes with excellent rewards.")

# Creating a bar graph to visualize and rank the highest paid or top 30 job categories.
def Insight_6():
    st.title("6. The Top 30 Highest Paid Job Categories by Salary_in_KES")
    # Group by job_title, calculate the count, and sort by count in descending order
    job_counts = data['job_title'].value_counts().sort_values(ascending=False)
    # Select the top 20 job categories
    top_30_jobs = job_counts.head(30)
    # Reset index to create a DataFrame with job_title and count columns
    top_30_jobs_df = top_30_jobs.reset_index()
    # Rename columns for clarity
    top_30_jobs_df.columns = ['job_title', 'count']
    # Bar graph for the top 20 job categories
    plt.figure(figsize=(14, 10))
    plt.bar(top_30_jobs_df['job_title'], top_30_jobs_df['count'], color='blue')
    plt.xlabel('Job Title')
    plt.ylabel('Count')
    #plt.title('Top 30 Highest Paid Job Categories by Salary_in_KES')
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90, ha='right')
    plt.tight_layout()
    st.pyplot(plt)
    st.write("Figure 6: The bar graph shows the top 30 highest paid job categories by Salary_in_KES. \n"
    "The five most paid job titles are Data Engineer, Data Scientist, Data Analyst, Machine Learning Engineer, \n" 
    "and Research Scientist respectively. \n"
    "The five least paid job titles are BI Analyst, Machine Learning Infrastructure Engineer, Computer Vision Engineer, \n"
    "Data Modeler, and Data Science Lead respectively."
    "With this in mind, you are able to choose the best career path based on your career compensation and financial goals.")

def Insight_7():
    st.title("7. Salary (KES) Distribution Based on Employee Residence or Country of Stay")
    # Group by 'employee_residence' and salary_in_usd.
    EmployeeResidence_KESSalary = data.groupby('employee_residence')['Salary_in_KES'].sum().reset_index()
    # Sort the DataFrame by 'Salary_in_KES' in ascending order
    EmployeeResidence_KESSalary = EmployeeResidence_KESSalary.sort_values(by='Salary_in_KES', ascending=False)
    # Create a bar chart (histogram) with sorted values
    fig_EmployeeResidence_KESSalary = px.bar(EmployeeResidence_KESSalary,
                                         x='employee_residence',
                                         y='Salary_in_KES',
                                         labels={'Salary_in_KES': 'Total Salary in KES'})
    st.plotly_chart(fig_EmployeeResidence_KESSalary)
    st.write("Figure 7: The Histogram shows that most of the salary was paid to employees residing in the United States of America (US) \n"
             "followed by those in Great Britain (GB), and in Canada (CA) respectively. This means that Geographical locations of companies \n"
             "is impacting the distribution of salary. From the analysis it can be concluded that for Kenyans, the fully remote and freelance \n"
             "work models are the best choices because moving to other countries such as US and GE is difficult and comes with extra costs.")

def Insight_8():
    st.title("Salary - (KES) Distribution Based on Different Company Locations")
    # Group by 'employee_residence' and salary_in_usd.
    EmployeeResidence_USDSalary = data.groupby('company_location')['Salary_in_KES'].sum().reset_index()
    # Sort the DataFrame by 'Salary_in_KES' in ascending order
    EmployeeResidence_USDSalary = EmployeeResidence_USDSalary.sort_values(by='Salary_in_KES', ascending=False)
    # Create a bar chart (histogram) with sorted values
    fig_EmployeeResidence_USDSalary = px.bar(EmployeeResidence_USDSalary,
                                         x='company_location',
                                         y='Salary_in_KES',
                                         labels={'Salary_in_KES': 'Total Salary in Kenyan Shillings'})
    st.plotly_chart(fig_EmployeeResidence_USDSalary)
    st.write("Figure 8: The results are similar to that of insight 7, therefore, refer to visualization on Figure 7 above.")
    
def Insight_9():
    st.title("9. Salary Distribution Over Different Company Locations in USD")
    # Group by 'employee_residence' and salary_in_usd.
    CompanyLocation_USDSalary = data.groupby('company_location')['salary_in_usd'].sum().reset_index()
    # Create a bar chart (histogram)
    fig_CompanyLocation_USDSalary = px.histogram(CompanyLocation_USDSalary, x='company_location', y='salary_in_usd')
    # Show the plot
    st.plotly_chart(fig_CompanyLocation_USDSalary)
    st.write("Figure 9: The histogram chart indicates that most salaries were paid to employees working for companies\n"
            "based in the USA followed by United Kingdom, and canada as depicted in Insight 9. The results strongly indicate that\n"
            "those working and living in the same region with their employer companies have high chances of earning more compared to others.\n"
            "This trend might also mean that companies which are seriously focused in adopting AI, ML, and Data Science are\n"
            "based in countries with the highest paid salaries.")

# Dropdown menu to select visualization
insights = ['Insight_1', 'Insight_2', 'Insight_3', 'Insight_4', 'Insight_5', 'Insight_6', 'Insight_7', 'Insight_8', 'Insight_9']
selected_Insight = st.selectbox('Select an Insight From the Dropdown Menu to Visualize', insights)
# Display selected visualization with description
if selected_Insight == 'Insight_1':
    Insight_1()
elif selected_Insight == 'Insight_2':
    Insight_2()
elif selected_Insight == 'Insight_3':
    Insight_3()
elif selected_Insight == 'Insight_4':
    Insight_4()
elif selected_Insight == 'Insight_5':
    Insight_5()
elif selected_Insight == 'Insight_6':
    Insight_6()
elif selected_Insight == 'Insight_7':
    Insight_7()
elif selected_Insight == 'Insight_8':
    Insight_8()
elif selected_Insight == 'Insight_9':
    Insight_9()

st.write("======================================================================================")
st.title("Congratulations!!!!!")
st.subheader("You have Explored Nine Career Guide Insights")
st.write("You are made for Greatness. A journey of thousand miles begins with a single step. \n"
         "I hope you enjoyed the insights and visualizations generated by this app. \n"
         "Please let me know if you have any questions or feedback. \n"
         "Thank you for using the Data Jobs Guide App.\n")
st.write("Best Regards, \n"
         "Your Data Jobs Guide App, Buddy.")
st.write("======================================================================================")
st.subheader("Goodbye & Welcome Back for More Career Insights.")
st.write("======================================================================================")