import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days= ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

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
    while True:
        city= input('Which of these 3 cities would you like to know more about: Chicago, New York City or Washington? ').lower()

        if city not in CITY_DATA :
            print("\n \n It seems that this city is not on the list, please type it again: ")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month= input('Please select a month or all of them: ').lower()

        if month not in months:
            print("\n \n That month is incorrect, please type it again: ")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('Please select a day of the week or all of them: ').lower()

        if day not in days:
            print("\n \n That day is incorrect, please type it again: ")
        else:
            break


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


    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month!='all':

        month_number= months.index(month)+1
        df=df[df['month'] == month_number]

    if day!='all':

        df=df[df['day_of_week'] == day.title()]

    print('Thank you! You have chosen the next data: \nCity: {}\nMonth: {}\nDay: {}'.format(city, month, day))
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month_idx= df['month'].value_counts().idxmax() -1
    popular_month=months[popular_month_idx]
    print('The most common month is: {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print('The most common day of the week is: {}'.format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('The most common Start hour is: {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: {}'.format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: {}'.format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination of start and end station trip is: ', combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time for the trip is: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean of travel time for the trip is: {}'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n User Type Count')
    print(df['User Type'].value_counts())
    print('\n Gender Count')

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print(df['Gender'].value_counts())
        print('\n')
        print('\n Year of Birth Information')
    else:
        print("There is no available data for gender")
        print('\n')
        print('\n Year of Birth Information')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].value_counts().idxmax()

        print('Earliest year of birth: {}'.format(earliest))
        print('Most recent : {} '.format(most_recent))
        print('Most Common : {}'.format(most_common))
    else:
        print("There is no available data for year of birth")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #Raw data display
    input_data = input('\nWould you like to see the first 5 lines of raw data? Please enter yes or no: ').lower()
    if input_data in ('yes'):
        i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
            add_data = input('Would you like to see more raw data? Please enter yes or no: ').lower()
            if add_data not in ('yes'):
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
