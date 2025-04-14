.. _faq:

FREQUENTLY ASKED QUESTIONS
==========================

WHAT DATA CAN I GET FROM SOCIAL MEDIA?
--------------------------------------

Basically, you can get everything you can extract manually from social networks after logging in to the account: accounts info, posts, comments, etc.

I GET A 403 ERROR. WHAT SHOULD I DO?
------------------------------------

Check the specified path to the endpoint.

I GET A 401 ERROR. WHAT SHOULD I DO?
------------------------------------

Check your API key in the Authorization header.

I GET A 500 ERROR. WHAT SHOULD I DO?
------------------------------------

There was a request processing error on our side. In this case you will not be charged. Please contact us through :ref:`support` page.

I GET A 503 ERROR. WHAT SHOULD I DO?
------------------------------------

This means that the endpoint has been moved to the “Maintained” status and we are fixing the problem. In this case you will not be charged. If you need the result of your request urgently, please contact us through :ref:`support` page.

WHY AM I GETTING AN INCOMPLETE NUMBER OF RESULTS IN THE RESPONSE?
-----------------------------------------------------------------

Since all data is extracted from open sources, sometimes external factors or temporary limitations can impact the ability to retrieve the full set of requested results. If such interruptions occur during the process, additional time may be required to retry and complete the data retrieval. If this occurs within the timeout set by the endpoint, it may result in fewer messages being returned than expected.

In response to this issue, the development team has implemented a quick fix. We also continuously monitor these processes to identify potential areas for optimization and ensure that performance remains within acceptable parameters.

WHY AM I GETTING ZERO RESULTS IN THE RESPONSE?
----------------------------------------------

When extracting data from open sources, external factors and temporary limitations may affect the result of your query. In this case, try to repeat your request after some time.

You may also get zero results if there is no data matching the request in open sources. Try changing the query parameters or their values to broaden the search area.

WHY AM I WAITING SO LONG FOR A RESPONSE? IS IT POSSIBLE TO SHORTEN THE WAITING TIME FOR A RESPONSE?
---------------------------------------------------------------------------------------------------

The execution time is determined by the complex implementation of real-time parsing.

WHY DOES THE ENDPOINT RETURN AN ERROR?
--------------------------------------

Probably the endpoint has been disabled or there are problems on the Source side.

Method parameters may change when the documentation is updated. See the support section to get an updated version of the documentation.

WHAT ARE THE PARAMETERS ``LAT``, ``LNG`` AND ``RADIUS``?
--------------------------------------------------------

The ``lat`` and ``lng`` parameters represent geographic coordinates, where ``lat`` is latitude and ``lng`` is longitude in decimal format. The ``radius`` parameter specifies the search area from the point specified by the geographic coordinates. 

WHAT IS THE ``DELAYED`` PARAMETER AND HOW CAN I USE IT?
-------------------------------------------------------

The ``delayed=1`` parameter, allows the request to be executed asynchronously, meaning that the result will be delayed. The instant response will contain the ``task_id`` parameter.

I RECEIVED THE ``TASK_ID`` PARAMETER IN THE RESPONSE. WHAT SHOULD I DO?
-----------------------------------------------------------------------

To find out the execution status of your request, use the ``/task_status`` method by specifying the ``task_id`` value instead of ``{TASK ID}``:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/delayed/task_status?task_id={TASK ID}' -H 'Authorization: {Your API Key}'

To get the result of running the request, make the same request as you did the first time, adding the ``task_id`` parameter:

.. code-block:: bash
    
    curl 'https://{DOMAIN}/api/{...}?query={...}&task_id={TASK ID}' -H 'Authorization: {Your API Key}'

I HAVEN'T FOUND AN ANSWER TO MY QUESTION. WHAT SHOULD I DO?
-----------------------------------------------------------

If you have a different question or your problem is not fixed, please see the :ref:`support` page.