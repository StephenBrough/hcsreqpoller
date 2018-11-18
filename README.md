# hcsreqpoller
Poll HCS thread for new posts

Based on a script written by Hunter Thornsberry (https://github.com/Hunter275)

Polls HCS thread for new posts
Breaks when latest page reaches 20 posts (the page limit)
Plays mgs.mp3 when a change is detected, then attempts to get the next page (which breaks if current last page has 20, but there is no next page)

A request would stall every so often, so I added a timeout and a retry
