# NBA Clutch Project

## Background information:

Website with interactive chart that visualizes NBA players' stats under clutch circumstances. As a result, the clutchness of NBA players may be accurately compared and discussed.

## Legal statement:

The data pulled from stats.nba.com is not stored in any database, nor is it used for monitziation purposes. All statistics are directly attibuted to stats.nba.com.

## FAQ:

### Is the data accurate?

The data is pulled directly from stats.nba.com, which is updated after every game, using the Python library 'nba_api' made by user [swar](https://github.com/swar). So, yes!

### Why is it taking so long to load a chart?

There is no publicly accessible API for stats.nba.com, so via [nba_api](https://github.com/swar/nba_api), the endpoints where data is stored in stats.nba.com are accessed by an http request to stats.nba.com constructed from the parameters that users choose. Along the way, these requests can be throttled, significantly slowing down the loading process. 

### How can I tell which parameters to modify if I get an error message?

It's hard to say. An error message usually occurs for two reasons: this game scenario hasn't happened, or it didn't happen. I'd suggest modifying the parameter that seems most illogical!

### Why should I care about this?

Accurately determining the clutchness of an NBA player requires a wealth of data across long periods of time. Thanks to [swar](https://github.com/swar) and NBA.com, this web app pulls from this data and visualizes it in a comprehensible manner, allowing users to settle the age-old argument: who's more clutch?
