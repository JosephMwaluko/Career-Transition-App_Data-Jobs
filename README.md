**Project Title:** The Ultimate Career Decision-Making Guide: - Data Jobs

**Tagline:** Navigating the Data-Driven Career Landscape: A Deep Dive into AI, Machine Learning, and Data Science Salaries.

**1.0 Introduction:**
In the ever-evolving landscape of technology, the allure of Artificial Intelligence (AI), Machine Learning (ML), and Data Science has captivated the ambitions of professionals
seeking career transitions or skill advancements. However, stepping into these domains is not without its challenges. Aspiring individuals often confront uncertainties surrounding
market demands, skill prerequisites, and the intricacies of navigating a competitive job market.

**1.1 The Challenge:**
One of the primary challenges faced by individuals venturing into the realms of AI, ML, and Data Science is understanding the nuanced factors that influence career progression and
salary structures within these fields. The demand for skilled professionals is high, but so is the competition. Navigating this landscape requires a comprehensive understanding of
how various elements such as years of experience, employment type, company size, and geographic location impact earning potential.

**1.2 The Solution:**
To address these challenges, the project embarks on a journey to demystify the intricate web of factors contributing to success in AI, ML, and Data Science careers.
By leveraging data analytics and visualization techniques, we aim to provide actionable insights that empower individuals to make informed decisions about their career trajectories.

**1.3 Project Objectives:**
The project analyzes a dataset encompassing global salaries in the AI, ML, and Data Science domains. We delve into critical variables, including working years, experience levels,
employment types, company sizes, employee residence, company locations, remote work ratios, and salary in USD and KES. The goal is to create a comprehensive visualization highlighting
salary distributions and uncover patterns and trends that can guide aspiring professionals.

**2.0 Dataset description**
The dataset contains 11 columns with the following characteristics:
1.	work_year: The year the salary was paid.
2.	experience_level: The experience level in the job during the year with the following possible values:
•	EN: Entry-level / Junior
•	MI: Mid-level / Intermediate
•	SE: Senior-level / Expert
•	EX: Executive-level / Director
3.	employment_type: The type of employment for the role:
o	PT: Part-time
o	FT: Full-time
o	CT: Contract
o	FL: Freelance
4.	job_title: The role worked during the year.
5.	salary: The total gross salary amount paid.
6.	salary_currency: The currency of the salary paid is an ISO 4217 currency code.
7.	salary_in_usd: The salary in USD (FX rate divided by avg. USD rate of the respective year via data from fxdata.foorilla.com).
8.	employee_residence: Employee's primary country of residence in during the work year as an ISO 3166 country code.
9.	remote_ratio: The overall amount of work done remotely; possible values are as follows:
	0: No remote work (less than 20%)
	50: Partially remote/hybrid
	100: Fully remote (more than 80%)
10.	company_location: The country of the employer's main office or contracting branch as an ISO 3166 country code.
11.	company_size: The average number of people that worked for the company during the year:
	S: less than 50 employees (small)
	M: 50 to 250 employees (medium)
	L: more than 250 employees (large)

**2.1 The Engineered Features**
1.	Combining the experience levels, employment types, remote ratios, and company sizes initials with their full names.
   This ensured proper labeling, especially during data visualizations.
  	![Alt text](https://github.com/JosephMwaluko/Career-Transition-App-Guide--Data-Jobs/blob/main/Engineered%20Feature%201.PNG)
2.	The "salary_in_usd" column was converted to Kenyan Shillings and renamed “Salary_in_KES.” Since the dataset is updated weekly, the process of conversion was automated.
    A function was created that requests the current USD Dollar exchange rate versus the Kenyan Shilling and multiplies it by the salary values in dollars to get salary value in
  	Kenyan money. The function uses an API Key and a base URL for a website where it requests the current exchange rate, prints it on the output, and multiplies it with salary calculated
  	in USD dollars to create a new column named “Salary_in_KES.” Therefore, every time the data-jobs guide application is launched, the process will be repeated, and the output will be
  	updated accordingly. This was proven during the application development as the current value was printed out every time the Data analysis Jupyter Notebook was opened and the cell ran.
  	![Alt text](https://github.com/JosephMwaluko/Career-Transition-App-Guide--Data-Jobs/blob/main/Engineered%20Feature%202.PNG)
3.	Creating a new dataset column that checks and indicates if an employee comes from the company location - same country code in the dataset.
   ![Alt text](https://github.com/JosephMwaluko/Career-Transition-App-Guide--Data-Jobs/blob/main/Engineered%20Feature%203.PNG)
 	
**2.2 Key Analytical Dimensions:**
1. Work Years: Examining how salaries evolve over the years.
2. Experience Level: Understanding the impact of skill proficiency on earning potential.
3. Employment Type: Unraveling the nuances of salaries in full-time, part-time, contract, or freelance roles.
4. Company Size: Analyzing the correlation between company size and compensation.
5. Company Location: Investigating geographical variations in salary structures.
6. Employee Residence:  Exploring the impact of residing in a specific country on earnings.
7. Remote Ratio: Assessing the influence of remote work arrangements on salaries.
8. Salary_in_KES: Standardizing salaries to a common currency for cross-country comparisons.

**Conclusion**
By examining these dimensions, the project seeks to provide a nuanced perspective on the diverse factors shaping salaries in the AI, ML, and Data Science sectors.
Armed with these insights, individuals can navigate their career paths with a clearer understanding of the landscape, making strategic decisions that enhance their success in these
dynamic and high-demand fields.

**The Streamlit Application Link:** It takes you to the final application deployed using the Streamlit Sharing platform - Streamlit.io.
https://career-transition-app-guide--data-jobs-mykju9yk46ziy4cagw9it8.streamlit.app/

