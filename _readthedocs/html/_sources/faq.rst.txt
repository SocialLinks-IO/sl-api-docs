.. _faq:

Frequently Asked Questions
==========================

What data can I get from social media?
--------------------------------------

Basically, you can get everything you can extract manually from social networks after logging in to the account: accounts info, posts, comments, etc.

I get a 403 error. What should I do?
------------------------------------

Check the specified path to the endpoint.

I get a 401 error. What should I do?
------------------------------------

Check your API key in the Authorization header.

I get a 500 error. What should I do?
------------------------------------

There was a request processing error on our side. In this case you will not be charged. Please contact us through :ref:`support` page.

I get a 503 error. What should I do?
------------------------------------

This means that the endpoint has been moved to the “Maintained” status and we are fixing the problem. In this case you will not be charged. If you need the result of your request urgently, please contact us through :ref:`support` page.

Why am I getting an incomplete number of results in the response?
-----------------------------------------------------------------

Since all data is extracted from open sources, sometimes external factors or temporary limitations can impact the ability to retrieve the full set of requested results. If such interruptions occur during the process, additional time may be required to retry and complete the data retrieval. If this occurs within the timeout set by the endpoint, it may result in fewer messages being returned than expected.

In response to this issue, the development team has implemented a quick fix. We also continuously monitor these processes to identify potential areas for optimization and ensure that performance remains within acceptable parameters.

Why am I getting zero results in the response?
----------------------------------------------

When extracting data from open sources, external factors and temporary limitations may affect the result of your query. In this case, try to repeat your request after some time.

You may also get zero results if there is no data matching the request in open sources. Try changing the query parameters or their values to broaden the search area.

Why am I waiting so long for a response? Is it possible to shorten the waiting time for a response?
---------------------------------------------------------------------------------------------------

The execution time is determined by the complex implementation of real-time parsing.

Why does the endpoint return an error?
--------------------------------------

Probably the endpoint has been disabled or there are problems on the Source side.

Method parameters may change when the documentation is updated. See the support section to get an updated version of the documentation.

What are the parameters ``lat``, ``lng`` and ``radius``? 
--------------------------------------------------------

The ``lat`` and ``lng`` parameters represent geographic coordinates, where ``lat`` is latitude and ``lng`` is longitude in decimal format. The ``radius`` parameter specifies the search area from the point specified by the geographic coordinates. 

What is the ``delayed`` parameter and how can I use it?
-------------------------------------------------------

The ``delayed=1`` parameter, allows the request to be executed asynchronously, meaning that the result will be delayed. The instant response will contain the ``task_id`` parameter.

I received the ``task_id`` parameter in the response. What should I do?
-----------------------------------------------------------------------

To find out the execution status of your request, use the ``/task_status`` method by specifying the ``task_id`` value instead of ``{TASK ID}``:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/delayed/task_status?task_id={TASK ID}' -H 'Authorization: {Your API Key}'

To get the result of running the request, make the same request as you did the first time, adding the ``task_id`` parameter:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/{...}?query={...}&task_id={TASK ID}' -H 'Authorization: {Your API Key}'

I haven't found an answer to my question. What should I do?
-----------------------------------------------------------

If you have a different question or your problem is not fixed, please see the :ref:`support` page.