# NBA Clutch Project

### Simulate common game scenarios

![Website Generic Demo](demos/nba_clutch_generic_demo.gif)

### Or get specific!

![Website Specific Demo](demos/nba_clutch_specific_demo.gif)

## Background information:

Website with interactive chart that visualizes NBA players' stats under clutch circumstances. As a result, the clutchness of NBA players may be accurately compared and discussed.

## FAQ:

### Why isn't this project hosted?

Unfortunately, there's been a long history of stats.nba.com blocking various cloud provider IPs, as shown in [2019](https://github.com/swar/nba_api/issues/106#issuecomment-559877475), [2018](https://towardsdatascience.com/pretending-to-know-about-the-nba-using-python-699177a58685#7083), and [2017](https://github.com/bttmly/nba/issues/41#issuecomment-294624837). I tried hosting it on PythonAnywhere, Heroku, and OxyCreates, but ran into this problem as well. As a result, it seems as though NBA's stats API can only be requested from a local server.

### Why should I care about this?

Accurately determining the clutchness of an NBA player requires a wealth of data across long periods of time. Thanks to [swar](https://github.com/swar) and NBA.com, this web app pulls from this data and visualizes it in a comprehensible manner, allowing users to settle the age-old argument: who's more clutch?

### Is the data accurate?

The data is pulled directly from [stats.nba.com](https://stats.nba.com/), which is updated after every game, using the Python library [nba_api](https://github.com/swar/nba_api) made by user [swar](https://github.com/swar). So, yes!

### How can I tell which parameters to modify if I get an error message?

It's hard to say. An error message usually occurs for two reasons: this game scenario hasn't happened, or it didn't happen. I'd suggest modifying the parameter that seems most illogical!

## Legal statement:

The data pulled from [stats.nba.com](https://github.com/swar/nba_api) is not stored in any database, nor is it used for monitziation purposes. All statistics are directly attibuted to [stats.nba.com](https://stats.nba.com/).