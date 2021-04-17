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
    City_list = ["Chicago","New York City","Washington"]
    Month_list = ["All","January","February","March","April","May","June"]
    Day_list = ["All","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    _outerloop, _innerloop1, _innerloop2, _innerloop3, _innerloop4, _innerloop5 = True, True, True, True, True, True
    city_select, month_select, day_select = 0, 0, 0
    print('Hola Amigo! You want US bikeshare data! I have US bikeshare data!\n')

    #Main While Loop controlling entire loop
    while _outerloop:

     #Inner Loop #1 - Gets user input for city (chicago, new york city, washington).
        while _innerloop1:
            try:
                city_select = int(input("Please select number for desired city. \n(1) Chicago,(2) New York, (3) Washington: "))
                if city_select < 4:
                    _innerloop1 = False
                else:
                    print('That\'s not a valid number selection! Select again.')
            except:
                print('That\'s not a valid number selection! Select again.')

     #Inner Loop #2 - Gets user filter selections (month,day)
        while _innerloop2:
            while _innerloop3:
                try:
                    filter_select = int(input("How would you like to filter the data?: (0) No Filter, (1) By Month, (2) By Day : "))
                    if filter_select < 3:
                        _innerloop3 = False
                    else:
                        print('That\'s not a valid number selection!')
                except:
                    print('That\'s not a valid number selection!')
            if filter_select == 0:  #User selects no filter
               _innerloop2 = False
            elif filter_select == 1:  #Get user input for month if selected
                while _innerloop4:
                    try:
                        month_select = int(input("Data available for January through Jun. \nChoose 0 for all months or (1) Jan, (2) Feb, (3) Mar, (4) Apr, (5) May, (6) Jun: "))
                        if month_select < 7:
                            _innerloop2 = False
                            _innerloop4 = False
                        else:
                          print('That\'s not a valid number selection!')
                    except:
                        print('That\'s not a valid number selection!')
            elif filter_select == 2:  #Get user input for day if selected
                while _innerloop4:
                    try:
                        day_select = int(input("Select day of week. \nChoose 0 for all days or (1) Mon (2) Tues (3) Wed (4) Thur (5) Fri (6) Sat (7) Sun: "))
                        if day_select < 8:
                            _innerloop2 = False
                            _innerloop4 = False
                        else:
                            print('That\'s not a valid number selection!')
                    except:
                        print('That\'s not a valid number selection!')
            else:
                print('That\'s not a valid number selection!')
        print('\n')
        print('-'*40)
        city, month, day = City_list[city_select-1],Month_list[month_select],Day_list[day_select]
        print("Hola amigo!  Filters selected - City: {}, Month: {}, Day: {}".format(city,month,day))
        _innerloop5 = True
        #Asks whether selections are ok or not.  If not, repeat loop again
        while _innerloop5:
            _repeat = input("All good on the selections? (yes or no): ")
            try:
                if _repeat.lower() == "yes":
                    _outerloop = False
                    _innerloop5 = False
                elif _repeat.lower() == "no":
                    _innerloop5 = False
                    _innerloop1, _innerloop2, _innerloop3, _innerloop4 = True, True, True, True
                    city_select, month_select, day_select = 0, 0, 0
            except:
                print("C'mon dude! Select yes or no or we shall be stuck in this loop forever!")

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

    # TO DO: display the most common month

    df['month'] = df['Start Time'].dt.month
    popular_month = int(df['month'].mode())
    print('Most Common Month: ', Month_list[popular_month-1])

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode().values[0]
    print('Most Common Day of the Week: ',popular_day)

    # TO DO: display the most common start hour
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


    df['trip_duration_mins'] = (df['End Time'].sub(df['Start Time']).dt.total_seconds().div(60))
    df['trip_duration_hours'] = (df['End Time'].sub(df['Start Time']).dt.total_seconds().div(3600))

    # TO DO: display total travel time
    tot_travel = round(df['trip_duration_hours'].sum(),2)
    print('Total bikeshare usage (hours): ',tot_travel)

    # TO DO: display mean travel time
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

    display_loop = True
    pd.set_option('display.max_columns',200)
    while display_loop:
            display = input('Would you like to see the raw data? Enter yes or no: ')
            if display.lower() == 'yes':
               _innerloop = True
               N = 0
               while _innerloop:
                       print(df[N:(N+5)])
                       N += 5
                       _innerloop = False
                       display_loop = False
                       raw_data_continue = input('More data? Enter yes or no: ')
                       if raw_data_continue.lower() == 'yes':
                           _innerloop = True
            else:
                display_loop = False

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
