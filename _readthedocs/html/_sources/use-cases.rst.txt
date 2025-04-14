.. _use-cases:

Use Cases and Methods Combination
=================================

The methods can be combined for a more efficient search.

Searching for User's Connections with Categorization by Relationship Type
-------------------------------------------------------------------------

Learning the connections of a social media user can be necessary in different use cases — crimes investigation, background checks, KYC, fraud prevention. For more efficient search for related users, we at Social Links have combined several methods to quickly create a schema of relationships for any user of interest.

This technique recursively searches for a user's connections, which provides complete information about the user's relationships with other users and is especially useful when the user has hidden connections.

As input we are given a profile of the user of interest, and as output we get related users, each of which is assigned an index of the nature of the relationship with the user of interest. The method returns a list of linked users consisting of commenters, likers, reposters and authors from posts, photos, videos and comments in which the user of interest has been tagged or published. In addition to the user's connections, you will get photos, videos, posts, groups, tags, pages, and profile information.

Here is an example of part of the result of such a technique:

.. code-block:: json
    
    {
        "id": "100002044080395",
        "name": "Yana Djachenko",
        "url": "https://{domain}/jana.djachenk",
        "alias": "jana.djachenk",
        "photo": "",
        "is_page": false,
        "category": "",
        "is_verified": false,
        "type": "profile",
        "is_author": false,
        "score": 20,
        "connection_types": [
            "with"
        ],
        "connection_photos": {
            "10202451179037294": {
                "with": [
                    1483702814
                ]
            },
            "814657788698701": {
                "with": [
                    1494914810
                ]
            }
        }
    },
    {
        "id": "830011384",
        "name": "Inna Davidenko",
        "url": "https://{domain}/830011384",
        "alias": "",
        "photo": "{link}",
        "is_page": false,
        "category": "",
        "is_verified": false,
        "type": "profile",
        "score": 20,
        "connection_types": [
            "with"
        ],
        "connection_photos": {
            "814657788698701": {
                "with": [
                    1494914810
                ]
            }
        },
        "connection_posts": {
            "814657788698701": {
                "with": [
                    1494914810
                ]
            }
        }
    },
    {
        "id": "1506516798",
        "name": "Oksana Kobets",
        "alias": "oksana.kryvenko",
        "profile-image": "{link}",
        "url": "https://{domain}/oksana.kryvenko",
        "reaction_type": "Like",
        "score": 12,
        "connection_types": [
            "reaction",
            "with"
        ],
        "connection_posts": {
            "1206867989362420": {
                "reaction": [],
                "with": [
                    1488366299
                ]
            }
        }
    }


To get access to this method, please, read the :ref:`support` page.

Searching for Social Media Profiles with the Same Profile Picture and Name
--------------------------------------------------------------------------

Face recognition techniques are extremely important in many cases, such as KYC and general background checks. To make face searches more effective, you can combine face and name searches.

This technique is straightforward: first, conduct a general search by name or alias across social media platforms. This step will yield a list of potential matches, even if the name is not exactly the same — because many social media platforms use fuzzy search.

Next, compare the profile photos in these results with the original photo you have. This process doesn’t require access to a biometric database — just a name and a picture. As a result, you'll get a list of matched accounts.

.. image:: img/usecase1.gif

See the source code of the script in the `GitHub repository <https://github.com/SocialLinks-IO/sociallinks-api?tab=readme-ov-file#search-by-face-and-name>`_.

Analyzing Social Media Posts
----------------------------

Effective social media analysis is essential for gaining quick access to structured insights, supporting a variety of use cases — from brand protection to VIP monitoring or gaining situational awareness and performing narrative analysis.

The main use cases include:

- Retrieving posts, replies, and comments from specific accounts
- Gathering posts by keyword or hashtag
- Collecting posts from a particular region or specified geolocation

If you need to speed up your post analysis, Social Links API can be especially useful: it allows you to obtain posts from all major social media platforms using all the methods mentioned above. With fast access to data, you can analyze related posts, detect trends and anomalies, and automate content gathering to gain real-time insights into public opinion, possible risks, or evolving narratives.

Additionally, SL API supports content preprocessing functions with LLMs, such as topic and sentiment extraction, translation, and summarization, which are highly useful for identifying and prioritizing issues to explore.

.. image:: img/usecase2.png

See the source code of the script in the `GitHub repository <https://github.com/SocialLinks-IO/sociallinks-api?tab=readme-ov-file#analyze-social-media-posts>`_.