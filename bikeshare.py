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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please choose the city (chicago, new york city, washington) for your data output: ")
        if city.lower() in CITY_DATA.keys():
            break
        else:
            print("Sorry, wrong input. Please choose one of the citis chicago, new york city, washington.")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please choose the month (January - June) or 'all' for your analysis: ")
        if month.lower() in ["all", "january", "february", "march", "april", "may", "june"]:
            break
        else:
            print("Sorry, please enter 'all' or a month from Jan-Jun.")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please choose a day of the week (monday, tuesday, ... sunday) or all for your analysis: ")
        if day.lower() in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            break
        else:
            print("Sorry, please choose a weekday (monday, tuesday, ... sunday) or all.")
            continue

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
    if city == "chicago":
        df = pd.read_csv("chicago.csv")
    elif city == "new york city":
        df = pd.read_csv("new_york_city.csv")
    elif city == "washington":
        df = pd.read_csv("washington.csv")
        
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()

    if month != "all":
        df = df[df["month"] == month]
    
    if day != "all":
        df = df[df["day_of_week"] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is " + str(df["month"].value_counts().index[0]))

    # TO DO: display the most common day of week
    print("The most common day of the week is " + str(df["day_of_week"].value_counts().index[0]))

    # TO DO: display the most common start hour
    print("The most common start hour is " + str(df["Start Time"].dt.hour.value_counts().index[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is " + df["Start Station"].value_counts().index[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station is " + df["End Station"].value_counts().index[0])

    # TO DO: display most frequent combination of start station and end station trip
    comb_cities = df.groupby(["Start Station", "End Station"]).size().sort_values(ascending=False).reset_index()
    print("The most frequent combination of start and end stations are: " + str(comb_cities["Start Station"][0]) + " and " + str(comb_cities["End Station"][0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is: " + str(df["Trip Duration"].sum() // 3600) + " hours and " + str((df["Trip Duration"].sum() % 3600)/60) + " minutes.")

    # TO DO: display mean travel time
    print("The mean travel time is: " + str(df["Trip Duration"].mean() // 60) + " minutes.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Count of different User Types:")
    print(df["User Type"].value_counts())

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print("Count of gender:")
        print(df["Gender"].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("Overview of earliest, most recent and most commen year of birth:")
        print("Earliest year of birth: " + str(df["Birth Year"].min()))
        print("Most recent year of birth: " + str(df["Birth Year"].max()))
        print("Most common year of birth: " + str(df["Birth Year"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        scan_df = input("\nWould you like to see the dataset? Enter yes or no.\n")
        if scan_df.lower() == "yes":
            while True:
                print(df.head())
                check_scan = input("\nWould you like to see more data? Enter yes or no.\n")
                if check_scan.lower() != "yes":
                    break
                df = df.iloc[5:]

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
