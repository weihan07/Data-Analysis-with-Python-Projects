import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(), 1) 

    # What is the percentage of people who have a Bachelor's degree?
    bachelor_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelor_count/len(df)*100), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    adv_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    high_salary_adv = adv_edu[adv_edu['salary']=='>50K']

    non_adv_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    high_salary_non_adv = non_adv_edu[non_adv_edu['salary']=='>50K']

    # percentage with salary >50K
    higher_education_rich = round((len(high_salary_adv)/len(adv_edu) *100 ), 1)
    lower_education_rich = round((len(high_salary_non_adv)/len(non_adv_edu) * 100), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hour = df[df['hours-per-week'] == df['hours-per-week'].min()]
    
    num_min_hour = len(min_hour[min_hour['salary'] == '>50K'])
    rich_percentage = num_min_hour/len(min_hour) * 100

    # What country has the highest percentage of people that earn >50K?
    country = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    percent = country['>50K'] * 100
    highest_earning_country = percent.idxmax()
    highest_earning_country_percentage = round(percent.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    income = df[(df['native-country']=='India') & (df['salary']=='>50K')]
    top_IN_occupation = income['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }