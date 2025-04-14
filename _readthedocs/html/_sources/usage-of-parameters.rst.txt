.. _usage-of-parameters:

USAGE OF PARAMETERS
===================

In this section, you can learn more about some of the query string parameters. If you still have any questions, please, read the :ref:`support` page.

QUERY
-----

Parameter ``query`` is the main request input for API endpoints which depends on the path parameters. For example, ``query`` in ``/twitter_v2/user/following`` would contain Twitter profile ID or alias to get its followees and ``query`` in ``/maigret_search`` would contain alias to search profile on about 3000 websites:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/twitter_v2/user/following?query={...}' -H 'Authorization: {Your API Key}'

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/maigret_search?query={...}' -H 'Authorization: {Your API Key}'

Also, there are some API methods that use other parameters to run. These are 'advanced' search methods that require more than one input parameter. For example, to use a method which searches Twitter posts you can use different parameters as input data such as ``query``, ``exact_phrase``, ``hashtags``, ``lang``, ``from_accounts``, ``to_accounts``, ``mentioning_accounts``, etc:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/twitter_v2/search/tweets?query={...}&exact_phrase={...}&hashtags={...}&lang={...}&from_accounts={...}&to_accounts={...}&mentioning_accounts={...}&min_replies={...}&min_faves={...}&min_retweets={...}&filter_replies={...}&filter_links={...}&from_date={...}&to_date={...}&lat={...}&lng={...}&radius={...}&ignore_words={...}' -H 'Authorization: {Your API Key}'

LIMIT
-----

You should use the parameter ``limit`` to specify the upper limit of entities’ count that will return in your response. It helps to optimize work with methods with many results. For example, the response for the following request will contain up to ``12`` reposters of the post:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/twitter_v2/tweet/retweeters?query=1655981859447111701&limit=12' -H 'Authorization: {Your API Key}'

Order of entities in this limited piece of response will be equal to its order in data source layout/API. The larger the value of the limit parameter, the more likely the method will take longer to execute, since it takes longer to extract more data.

TIMEOUT
-------

The parameter ``timeout`` helps you to limit the time of query execution. For example, the following request of getting subscriptions by profile will be executed for no more than ``100`` seconds:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/twitter_v2/user/subscriptions?query=MrBeast&timeout=100' -H 'Authorization: {Your API Key}'

We do not support a ``timeout`` parameter value more than ``300`` seconds.

Some endpoints work in an asynchronous way, so if the time specified in the ``timeout`` parameter is not enough to get a result, during this time you will receive a response containing the ``task_id`` parameter. To learn more about asynchronous methods, see the Delayed methods section. 

DELAYED METHODS
---------------

If a method returns a result within the time limit specified in the ``timeout`` parameter (up to ``300`` seconds), it works in a synchronous way.

However, some data source operations are time-consuming. Therefore, many of our API methods support an asynchronous way of execution to get results if the result cannot be returned within the set `timeout` parameter. This means that the result will not be returned instantly, as it takes time to process the request. The instant response of such a method will contain the ``task_id`` parameter, which is the identifier for your task.

Some of our asynchronous methods also support the ability to switch between synchronous and asynchronous ways of execution due to the ``delayed`` parameter.

DELAYED
~~~~~~~

The ``delayed`` parameter helps you to delay the result if the request takes too long to execute.

If the ``delayed`` parameter is set to ``0`` (set by default) and the result can be returned within the set ``timeout`` parameter (up to ``300`` seconds), the method will respond in a synchronous way, i.e., the response will instantly contain the result.

If the ``delayed`` parameter is set to ``1``, the method will work in an asynchronous way and in the response will indicate either the result and ``task_id`` (if the value of the ``timeout`` parameter was enough to execute the request), or only the ``task_id`` parameter. The time to get the ``task_id`` parameter is limited by the ``timeout`` parameter.

TASK_ID
~~~~~~~

The ``task_id`` parameter is a task identifier, which, in case of asynchronous work of the method, will help you to check the status of the request execution or its result.

To get the status of a request execution use the same method with the same parameters used in the initial request inserted instead of ``{Your first request}`` and with the previously obtained value of the ``task_id`` parameter inserted instead of ``{...}``:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/{Your first request}&task_id={...}' -H 'Authorization: {Your API Key}'

In the response you will get the status of the request execution. Depending on the method, in the response, in addition to the status, you may also get a part of the request result — the data that the endpoint has managed to collect over time.

The request execution status can take the values in case it is still being processed and ``SUCCESS`` if the request is successful and the result is ready to be returned.

To get the result of the request, you need to use the same method with the same parameters that were used in the initial request with the addition of the ``task_id`` parameter. For example, use the Twitter method to get reposters by post in an asynchronous way by setting the ``delayed`` parameter to ``1``:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/twitter_v2/tweet/retweeters?query={...}&delayed=1' -H 'Authorization: {Your API Key}'

The instant response would contain the ``task_id`` parameter with value instead of ``{TASK ID}``:

.. code-block:: json
    
    {
        "task_id": "{TASK ID}"
    }

After the task is executed, we retrieve the result using the same method, adding the ``task_id`` returned earlier:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/twitter_v2/tweet/retweeters?query={...}&delayed=1&task_id={TASK ID}' -H 'Authorization: {Your API Key}'

We keep results for every asynchronous execution only for ``24`` hours (1 day).

TASK_TIMEOUT
~~~~~~~~~~~~

The ``task_timeout`` parameter helps you to limit the execution time of an asynchronous request. For example, to execute the following asynchronous Twitter method for getting reposters by post, the endpoint will run for no more than ``3000`` seconds:

.. code-block:: bash

    curl 'https://{DOMAIN}/api/twitter_v2/tweet/retweeters?query={...}&delayed=1&task_timeout=3000' -H 'Authorization: {Your API Key}'

We do not support ``task_timeout`` value more than ``3600`` seconds (1 hour).

USAGE AND COST CONTROL
----------------------

Using the method ``/stats`` you can get information about your API key:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/stats' -H 'Authorization: {Your API Key}'

The result in the response will contain: 

- Your Plan
- Expiration date 
- Available points (balance) 
- Rate limits (if applicable) 

TROUBLESHOOTING
---------------

If you notice any problems with the methods, please, read the :ref:`support` page.

All incidents can be tracked on a dedicated `web page <https://osintreststatus.statuspage.io/>`_, where you can also subscribe to updates to track the troubleshooting process.