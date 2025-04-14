.. _methods-examples:

METHODS EXAMPLES
================

To get access to a full list of methods, please, read the :ref:`support` page.

SEARCHING ACCOUNTS WITH THE SAME ALIAS (≈3000 WEB-SITES)
--------------------------------------------------------

Users often have the same alias on different platforms. This method, having an alias, finds users on different websites who use the same alias.

In the example above, let's find pages on different resources that use the alias ``elonmusk`` by limiting the number of results to ``6`` and the execution time to ``110`` seconds: 

.. code-block:: bash

    # Search for accounts:
    # - with alias "elonmusk" (query=elonmusk)
    # - limit to 6 results (limit=6)
    # - timeout after 110 seconds (timeout=110)

    curl 'https://{DOMAIN}/api/maigret_search?query=elonmusk&limit=6&timeout=110' -H 'Authorization: {Your API Key}'

.. image:: img/demo1.gif

Here's an example of one of the results:

.. code-block:: json
    
    {
        "exec_time": 3.6316255759447813,
        "count": 6,
        "result": [
            {
            "name": "GitHub",
            "url": "https://github.com/elonmusk",
            "rank": 918,
            "type": "maltego.URL"
            }
        ]
    }


SEARCHING FOR POSTS USING DIFFERENT PARAMETERS
----------------------------------------------

This method allows you to search Twitter user posts using multiple parameters at once.
It is not necessary to fill in all fields, you can filter by only some parameters (according to the social media logic).

Take a look at the example on our public GitHub repository as well: `Analyze Social Media Posts <https://github.com/SocialLinks-IO/sociallinks-api?tab=readme-ov-file#analyze-social-media-posts>`_.

Let's find posts of account ``nytimes`` which contain the words ``Syria`` or ``China``, in ``English``, with at least ``10`` replies, ``2`` likes, ``10`` retweets, and published between ``August 25`` and ``December 16`` of ``2024``. We will also sort the result by showing the most ``latest`` publications first. Limit the number of results to ``5`` and the response time to ``50`` seconds:

.. code-block:: bash

    # Search for tweets
    # - containing "nytimes" (query=nytimes)
    # - with words "Syria" or "China" (these_words=Syria%20China)
    # - in English language (lang=en)
    # - with at least 10 replies (min_replies=10)
    # - with at least 2 likes (min_faves=2)
    # - with at least 10 retweets (min_retweets=10)
    # - posted between August 25, 2024 and December 16, 2024 (from_date=2024-08-25&to_date=2024-12-16)
    # - sorted by latest first (sort=Latest)
    # - limited to 5 results (limit=5)
    # - with 50 seconds timeout (timeout=50)

    curl 'https://{DOMAIN}/api/twitter_v2/search/tweets?query=nytimes&these_words=Syria%20China&lang=en&min_replies=10&min_faves=2&min_retweets=10&from_date=2024-08-25&to_date=2024-12-16&sort=Latest&limit=5&timeout=50' -H 'Authorization: {Your API Key}'

.. image:: img/demo2.gif

Here's an example of one of the results:

.. code-block:: json

    {
        "type": "TwitterSearchTweetsUniversalResult",
        "count": 5,
        "exec_time": 4.95,
        "error": "",
        "results": [
            {
                "type": "TwitterTweet",
                "id": "1867889792706306276",
                "created": 1734174604,
                "tweet_type": "tweet",
                "conversation_id": "1867889792706306276",
                "text": "New York Times reporters explored the monumental palace of Bashar al-Assad, who ruled Syria for more than two decades and fled the country on Sunday. Here\u2019s a look into the abandoned presidential palace in Damascus.",
                "url": "https://twitter.com/nytimes/status/1867889792706306276",
                "view_count": 129072,
                "retweet_count": 32,
                "like_count": 59,
                "reply_count": 38,
                "reply_settings": "everyone",
                "quote_count": 1,
                "bookmark_count": 21,
                "media": {
                    "type": "TwitterTweetMedia",
                    "photos": [],
                    "videos": []
                },
            "lang": "en",
            "original_id": "",
            "original_url": "",
            "original_author_id": "",
            "original_author_alias": "",
            "original_author_url": "",
            "possibly_sensitive": false,
            "source": {
                "type": "TwitterTweetSource",
                "url": "http://www.socialflow.com",
                "title": "SocialFlow"
            },
            "location": {},
            "hashtags": [],
            "user_mentions": [],
            "urls": [
                {
                    "type": "TwitterTweetURL",
                    "display_url": "nyti.ms/3Dc6icj",
                    "expanded_url": "https://nyti.ms/3Dc6icj",
                    "url": "https://t.co/7616fT1hgI"
                }
            ],
            "card": {
                "type": "TwitterTweetCard",
                "url": "https://t.co/7616fT1hgI",
                "title": "A Tour of Assad\u2019s Monumental Palace, With a Scruffy Rebel as a Guide",
                "description": "The televisions may be stripped away now, but a presidential residence still contains many remnants of a brutal reign.",
                "domain": "www.nytimes.com",
                "image_url": ""
            },
            "poll": {},
            "edit_control": {
                "type": "TwitterEditControl",
                "edit_tweet_ids": [
                    "1867889792706306276"
                ],
                "editable_until": 1734178204000,
                "is_editable": true,
                "edits_remaining": 5
            },
            "user": {
                "type": "TwitterUser",
                "id": "807095",
                "alias": "nytimes",
                "url": "https://twitter.com/nytimes",
                "name": "The New York Times",
                "image": "https://pbs.twimg.com/profile_images/1098244578472280064/gjkVMelR_400x400.png",
                "created": 1172868102,
                "description": "News tips? Share them here: http://nyti.ms/2FVHq9v",
                "birthdate": null,
                "friend_count": 851,
                "follower_count": 55230279,
                "normal_follower_count": 55230279,
                "creator_subscription_count": null,
                "tweet_count": 558524,
                "media_count": 72422,
                "favorite_count": 18497,
                "list_count": 207792,
                "pinned_tweets": [],
                "is_default": false,
                "is_protected": false,
                "is_hidden_likes_on_profile": null,
                "is_hidden_subscriptions_on_profile": null,
                "is_verified": true,
                "is_blue_verified": true,
                "verified_type": "",
                "banner_image": "https://pbs.twimg.com/profile_banners/807095/1584666392",
                "location": "New York City",
                "withheld_in_countries": [],
                "hashtags": [],
                "urls": [
                    {
                        "type": "TwitterUserURL",
                        "display_url": "nyti.ms/2FVHq9v",
                        "expanded_url": "http://nyti.ms/2FVHq9v",
                        "url": "https://t.co/ghL9OoYKMM"
                    },
                    {
                        "type": "TwitterUserURL",
                        "display_url": "nytimes.com",
                        "expanded_url": "http://www.nytimes.com/",
                        "url": "http://t.co/ahvuWqicF9"
                    }
                ],
                "highlights_info": null,
                "professional": {},
                "verification_info": null
            }
        ]
    }