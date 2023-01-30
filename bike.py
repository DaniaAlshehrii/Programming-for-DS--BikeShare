import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
Days = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

Cities = ['Chicago' , 'New york city', 'Washington']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input ("Please choose one of these cities: \n new york city, washington, chicago\n").lower()
        if city not in  CITY_DATA :                                      
            print ("Please choose city from the cities list\n")
        else :
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    print ("The list of Months:")
    for month in Months :
        print (month , end =" \n")  
        
            
    monthN = " "
    while monthN.lower() not in Months:
        monthN = input ("please choose a month\n")
        if monthN.lower() in Months:            
            month = monthN.lower()
        else:
            print ("Please choose month from the months list\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)   
        
    DayN = ''
    while DayN.lower() not in Days:
        DayN = input("please choose a day from monday to sunday\n")
        if DayN.lower() in Days:         
            day = DayN.lower()
        else:            
            print ("Please choose correct day from monday to sunday\n")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     
    df = pd.read_csv(CITY_DATA[city])

   
    df['Start Time'] = pd.to_datetime(df['Start Time'])
  
    df['month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name
    
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
       
       month = Months.index(month)      
    
       df = df.loc[df['month'] == month]  
      
    if day != 'all':
      # analyze and create the new dataframe
      df = df.loc[df['Day'] == day.title()]

    return df


def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common Month is: ', common_month)

    # TO DO: display the most common day of week
    common_day = df['Day'].mode()[0]
    print('Most common Day is: ', common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common Hour is: ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    
    Combination = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nMost Commonly used combination of start station and end station trip:', Combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Time = sum(df['Trip Duration']) 
    print('Total travel time is: ', Total_Time)


    # TO DO: display mean travel time
    Mean_Time = df['Trip Duration'].mean() 
    print('Mean travel time is:', Mean_Time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    types = df['User Type'].value_counts()
    print('User Types:\n', types)
       
    
    # TO DO: Display counts of gender
    try:      
      gender = df['Gender'].value_counts()
      print(gender)
    except KeyError:
      print("\nThere is no Gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest = int(df['Birth Year'].min())
      print("The earliest year of birth is: ", earliest)
    except KeyError:
      print("\nThere is no Year for earliest year ")

    try:
      most_recent = int(df['Birth Year'].max())
      print("\nMost recent year is: ", most_recent)
    except KeyError:
      print("\nThere is no Year for recent year")

    try:
     most_common = int(df['Birth Year'].value_counts().idxmax())
     print("\n The most common year is: ", most_common)
    except KeyError:
      print("\nThere is no Year for common year")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(df):
    
    print("\nWould you like to view 5 rows of individual trip data? Enter yes or no\n")
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df[x:x+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
