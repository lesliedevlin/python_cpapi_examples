#CloudPassage CPAPI Examples

Version: *1.0 - 2015.06.24*
<br />
Author: *John Alexander* - *jalexander@cloudpassage.com*

The CPAPI SDK was authored by Apurva Singh. This Python script (cpapi_examples.py) includes
examples of using the CPAPI SDK library to call the CloudPassage REST API.

CPAPI (cpapi.py) is an SDK for using the CloudPassage Halo REST API. The primary purpose
of the CPAPI SDK is to make the CloudPassage API much easier to use, and it can help get you up
and running in as little as 30 minutes. 

The CPAPI SDK provides a method to do authentication to the Halo API server, and provides
a significant number of methods that can easily be used to make Halo API calls. 
This example code is heavily documented and meant to serve as a tutorial on how to use CPAPI,
and to help get started very quickly with using the Halo API.

Note: Not all Halo API REST calls are currently included in CPAPI. For those calls that currently don't exist
in CPAPI you can create your own, by making a copy of an already existing similar method in CPAPI, and then
modifying it slightly. So for example if you need a method to load a FIM Policy, you can take the method that loads a
configuration policy, copy it, rename it, and make a few minor changes to it - and you now have a
method to load a FIM policy. 

Note: There is also a Ruby version of the CPAPI SDK available -- and I'm working on a Go version.


##Requirements and Dependencies

To run, the (cpapi_examples.py) script requires:

* Python installed on the host that runs the script. (Python 2.7 recommended)
* The Python modules: base64, sys, json, urllib, urllib2 (note: All of these Python modules come with the standard default installation of Python, so you shouldn't need to do anything to include them.)
* A Halo API Key: read-only key (for GETs) or full-access key (For PUTs and DELETEs); Get the key and copy it from the Halo Portal


##List of Files

* **cpapi.py**  -  The CPAPI SDK
* **cpapi_examples.py**  -  The Python script that provides examples on how to use the CPAPI SDK. This is the script you want to run
* **cassandra-linux-v1.policy.json**  -  This is a pre-built Halo CSM policy that is used in several of the examples
* **README.md**  -  This ReadMe file
* **LICENSE.txt**  -  License from CloudPassage



##Usage

1. Copy the two-part Halo API key from the Halo Portal into the proper location in the cpapi_example.py script.
2. Copy cpapi_examples.py, cpapi.py, and the cassandra-linux-v1.policy.json file to your host.
2. Make sure Python can find the cassandra-linux-v1.policy.json file (i.e. path is set correctly)
3. Make sure Python can find the cpapi.py file (i.e. path is set correctly)
4. Execute the cpapi_example.py script.

##Acknowledgements
Thanks to Apurva Singh for creating the Python CPAPI SDK (cpapi.py)
Note: Apurva wrote a Ruby version of the CPAPI SDK that is also available.

<!---
#CPTAGS:community-supported api-example
#TBICON:images/python_icon.png
-->
