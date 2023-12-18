# GifDetector

This came up because I could not find the source of a GIF online. This tool enables detection of gif from source material like movies. One way to do this would be to hash frames, skip a certain number
but hash it. The problem with that solution is that often times gifs are of the wrong size or have a filter on them or some other weird watermark that hashing would fail to find. This is an algorthim that
uses Harris Corner Points as feature points so that they can be made invariant to disruptions usually seen. What this does is it captures and stores feature points of a movie and when the gif is presented 
it compares to see which feature points match and a vote is taken on the greatest number of matches to determine the movie or source material
