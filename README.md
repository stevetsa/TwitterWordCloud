# TwitterWordCloud

This repository contains instructions for creating a wordcloud using Python.  
The scripts were modified from [Marco Bonzanini](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/) and his book - [Mastering Social Media Mining with Python](https://www.packtpub.com/big-data-and-business-intelligence/mastering-social-media-mining-python)

```
user = "theNCI"
print("Creating wordcloud for @", user, "...", sep="" )
json_name = "user_timeline_" + user + ".jsonl"
python3 twitter_get_user_timeline.py $user
python3 twitter_term_frequency_graph.py $json_name 
````
 
