import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('choose one of the three cities in our Database (chicago, new york city or washington): ')
    while city.lower() not in ('chicago', 'new york city', 'washington'):
        print('Database only have info for chicago, new york city or washington')
        city = input('choose one of the three cities in our Database (chicago, new york city or washington): ')

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('Choose a month (january, february, march, april, may, june) or all: ')
    while month.lower() not in months:
        print('invalid month. Check if it is one the current available months')
        month = input('choose one of the current available months january, february, march, april, may, june or all: ')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input('Choose a day of the week (monday, tuesday, wednesday, thursday, fridary, saturday or sunday) and all for every data. Which one: ')
    while day.lower() not in days:
        print('check for typo')
        day = input('Choose a day of the week (monday, tuesday, wednesday, thursday, fridary, saturday or sunday). Which one: ')

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    import pandas as pd

    CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv','washington': 'washington.csv' }
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Startand End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    Month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']

    # Display the most common month

    df['month'] = df['Start Time'].dt.month
    popular_month = int(df['month'].mode())
    print('Most Common Month: ', Month_list[popular_month-1])

    # Display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode().values[0]
    print('Most Common Day of the Week: ',popular_day)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = int(df['hour'].mode())
    if popular_hour <= 12:
        time_of_day = "AM"
    else:
        popular_hour -= 12
        time_of_day = "PM"
    print('Most Common Start Hour: {} {} '.format(popular_hour,time_of_day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    start_station = df['Start Station'].mode().values[0]
    print('Most Commonly Used Start Station: ', start_station)

    # Display most commonly used end station
    end_station = df['End Station'].mode().values[0]
    print('Most Commonly Used End Station: ', end_station)

    # Display most frequent combination of start station and end station trip
    start_end_combo = (df['Start Station'] + ' / ' + df['End Station']).mode().values[0]
    print('Most Commonly Used Start / End Station Combination: ', start_end_combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['trip_duration_secs'] = (df['End Time'].sub(df['Start Time']).dt.total_seconds())
    df['trip_duration_mins'] = (df['End Time'].sub(df['Start Time']).dt.total_seconds().div(60))
    df['trip_duration_hours'] = (df['End Time'].sub(df['Start Time']).dt.total_seconds().div(3600))

    # Display total travel time
    tot_travel = round(df['trip_duration_hours'].sum(),2)
    print('Total bikeshare usage (hours): ',tot_travel)

    # Display mean travel time
    avg_travel_time = round(df['trip_duration_mins'].mean(),2)
    print('Average bikeshare usage (mins): ',avg_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city, df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating BikeShare User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_types = df['User Type'].value_counts().to_string()

    print('Total Number of BikeShare Users')
    print(user_types)

    #Display counts of gender - Washington data does not have gender so have to skip
    if city != 'washington':
        gender = df['Gender'].value_counts().to_string()
        print('\nBikeShare User Gender Breakdown')
        print(gender)

    #Display earliest, most recent, and most common year of birth - Washington data does not have birth year so have to skip

        print('\nBikeShare Users Birth Year Information\n')
        print('Youngest BikeShare user birth year: ', int(df['Birth Year'].max()))
        print('Oldest BikeShare user birth year: ',int(df['Birth Year'].min()))
        print('Most common birth year for BikeShare users: ',int(df['Birth Year'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Displays 5 rows of raw data for user"""
    from tabulate import tabulate
    while True:
    display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
    if display_data.lower() != 'yes':
        break
    print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
    i+=5

def main():
        _mainloop = True
        while _mainloop:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            pause = input('\nPress Enter key to see additional statistics.')
            trip_duration_stats(df)
            user_stats(city, df)
            pause = input('\nPress Enter key to see additional statistics.')
            display_data(df)
            _innerloop = True
            while _innerloop:
                    _mainloop = False
                    restart = input('\nWould you like to redo analysis with different data? Enter yes or no : ')
                    if restart.lower() == 'yes':
                        _innerloop = False
                        _mainloop = True
                    else:
                        _innerloop = False
            print('Adios Amigo!  Have a good day!')



if __name__ == "__main__":
	main()
