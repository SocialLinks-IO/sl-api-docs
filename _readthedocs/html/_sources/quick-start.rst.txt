.. _quick-start:

Quick Start
===========

To get started with Social Links API, you need to follow the 3 steps below:

1. Get the API key and domain: :ref:`support` page.
2. Send a request, replacing ``{DOMAIN}`` with the provided domain and ``{Your API Key}`` with your actual API key:

.. code-block:: bash

   curl 'https://{DOMAIN}/api/stats' -H 'Authorization: {Your API Key}'

3. If you receive a response with a following structure, it indicates that everything is functioning properly:

.. code-block:: json

   {
      "plan": "...",
      "expires": "20XX-01-01T00:00:00",
      "throttling": [],
      "points": 100000,
      "message": ""
   }

Read more about the possible requests in the :ref:`methods-examples` page.