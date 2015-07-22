# CPAPI Examples (cpapi_examples.py)
#
# cpapi.py is a simple SDK library that gives you the ability to use
# the CloudPassage Halo API in a very simple way.
#
# CPAPI allows you to make Halo API calls with a minimal knowledge
# of REST. CPAPI does all the "initialization" scaffolding  work for you in several
# simple method calls.
#
# cpapi_examples.py is a set of simple examples that show you how to 
# use cpapi, from creating your initial apicon (api connection) object and
# then using it to make cpapi method calls to make Halo REST API calls.
# The examples in cpapi_examples.py show GET, PUT, and DELETE calls. So it is fairly
# complete as far as showing you all different aspects of using CPAPI.
#
# Most of the HAlO API usage examples created so far typically only show
# you how to do REST GET calls and maybe a REST PUT call. As a bonus, a
# less common REST DELETE call example is included in these examples.
#
# Initialization of the connection object (apicon) is one line of code.
# Getting the authorization token is three lines of code.
# Making a Halo API call using a CPAPI method call -- is usually only one line of code.
# Extracting the data is done by pulling data out of the JSON response
# object you get back using simple Python list and dictionary indexing operations.
#
# The Halo API makes heavy use of JSON response objects.  JSON is the the data
# format that you use to transfer data to and from the Halo API server.
# Thus, you need to import Python's json module so you can work with data in JSON form,
# and of course you also need to import the cpapi module. Make sure you put cpapi.py
# somewhere where your Python interpreter can find it.
#
# For simplicity (ease of use) this example makes use of a pre-created CSM policy called
# "cassandra-linux-v1.policy.json".  This allows us to demonstrate several PUT and DELETE API call
# examples. Place this example policy file somewhere where your Python interpreter can find it.
# Usually the best place is the same location where cpiapi_examples.py is being executed from.
#
# Created: 2015.05.01
# Last Modified: 2015.07.07.0

import json
import cpapi

# Global variables
# Create the global variable apiCon so that it can be used at the global module level
# Setting it to None is a simple placeholder trick, where it will then be
# initialized later.
# This global variable is used for simplicity purposes, so that you don't have to pass the apiCon object into
# your functions. Normally using a global variable like this is not good coding practice.
apiCon = None

def create_api_connection():
    # A Halo API key (id and secret) can be obtained via the Halo user interface (UI)
    # Just cut-and-paste them from the Halo UI.
    # Normally you would put the id and secret in a text file, or a yaml file, etc... but for
    # the purposes of simplicity this is hard-coded in.
    clientid     = '513464c8'                           #This is a sample. Make sure and get one from the Halo UI.
    clientsecret = '0663e0957f42c270890935d84952e97f'   #This is a sample. Make sure and get one from the Halo UI.

    # Create an apiCon object to manage the connection to the Halo API server in order to use the Halo API
    # This connection object gives you access to all the methods and attributes of the CPAPI
    global apiCon
    apiCon = cpapi.CPAPI()


    #Set two of the attributes of the apiCon object to the API key ID and API secret
    apiCon.key_id = clientid
    apiCon.secret = clientsecret

    # Log-in to the Halo REST API Server and get an authentication token (usually only good
    # for around 15 minutes). The authentication token actually gets stored in the apiCon object as one
    # of its attributes, so no need to pass it in with any further apiCon method calls.
    # Note: to keep this example simple I don't check the value of 'resp' to see if an error occurred.
    resp = apiCon.authenticateClient()

    # OK -- That was easy. Seven simple lines of code and now you can start making calls. Cool!


#----EXAMPLE #1 ------------------------
# Make a Halo REST API call though a simple method call. This method "getServerList" gets the list of servers in your account
# and  then stores it as a JSON object (this JSON object can be accessed as a Python dictionary) in the variable "data".
# Note the print json.dumps() line that is commented out I included so you can see what the JSON response onject looks like
# Examining the JSON response object is useful so you can see what kind of data is returned and then decide what you want to
# grab from the JSON object.

def ex1():
    data, autherr = apiCon.getServerList()

    # Print out the response from the API call in a human-readable way, this is very useful
    # for troubleshooting and to see what the response data looks like

    #print json.dumps(data, sort_keys=True, indent=4) #used for experimentation and debug

    # Iterate through the list of servers and print out the count and the host names as an example of
    # how to handle the json data you get back from the API call.
    count = data['count']
    print "\nExample#1: List the names of the servers in you Halo account" 
    print "You have  %d active servers:" % (count)    
    servers = data['servers']
    for server in servers:
        print server['hostname']
    

#----EXAMPLE #2------------------------
#  This method "getServerGroupList" gets the list of server groups in your account
#  Note: the two variables on the left are not an error. This method returns a "tuple",
#  'data' is a JSON object, and 'autherr' is a Boolean variable.
#  Note: For simplicity I don't use autherr. You normally use it to check to see if your token has expired.
#  Note: That you use simple list and dictionary indexing to pull the data out of the JSON object.
#  In this case the JSON response object is basically a list of dictionaries.

def ex2():
    data, autherr = apiCon.getServerGroupList()
    #print json.dumps(data, sort_keys=True, indent=4)
    count = data['count']
    print "\nExample#2: List the Server Groups in your Halo Account"
    print "You have the following %d server groups:" % (count)    
    groups = data['groups']
    for group in groups:
        s_counts = group['server_counts']
        print "%s, active=%d, deactivated=%d, missing=%d" % (group['name'], s_counts['active'], s_counts['deactivated'], s_counts['missing'])
    

#----EXAMPLE #3------------------------
# This method "getFirewallPolicyList" gets the list of the firewall policies in your account
# This example is very similar to Example #2. Maka a method call, get a JSON response
# object back, and pull some data out of it and display the data.

def ex3():
    data, autherr = apiCon.getFirewallPolicyList()
    # print json.dumps(data, sort_keys=True, indent=4)
    count = data['count']
    print "\nExample#3: List the firewall policies in your account" 
    print "You have %d firewall policies:" % (count)    
    firewall_policies = data['firewall_policies']
    for fp in firewall_policies:
        print "%s, platform=%s" % (fp['name'], fp['platform'])

#----EXAMPLE #4-----------------------
# Here we load a CSM policy that is in JSON format and load it into Halo.
# This is an example of using CPAPI to insert data into Halo.
# For this example to work you have to have a Halo CSM policy. The easiest
# way to get one is to export one out from the Halo UI and save it
# somewhere where your Python interpreter can find it.
# We use the JSON load method to place  the policy into the variable called "data",
# and then we make a method call using our CPAPI connection object to load
# the JSON-formatted data that is in the "data" variable into Halo.
#
# This is the REST API call that is essentially being made:
# POST https://api.cloudpassage.com/v1/policies/
#
# Note: Halo won't let you load a policy if a policy with that name already
# exists in your account!! So if you have a problem make sure this isn't the case. :-)

def ex4():
    print "\nExample#4: Loading a CSM policy into Halo"
    filename = 'cassandra-linux-v1.policy.json' 
    ifile = open( filename, 'rU')
    # ofile = open ("testfile.txt", 'w') # used for debug
    print "Processing the input file.... %s" % (filename)
    
    data = json.load(ifile)
    print "Loading the policy: %s" % (data['policy']['name'])
    json_response,autherr = apiCon.createConfigurationPolicy(data)

    # print json.dumps(json_response, sort_keys=True, indent=4)
    # ofile.writelines(json.dumps(json_response, sort_keys=True, indent=4)) # used for debug
    # ofile.close() # used for debug
    ifile.close() 

#----EXAMPLE #5-----------------------
#  List configuration policies
#  You are essentially making the following REST API Call:
#  GET https://api.cloudpassage.com/v1/policies
#  You can use this call to, for example, obtain the ID of an individual policy so that you can
#  then view it or manipulate it by using some of the methods in cpapi.

def ex5():
    print "\nExample#5: Listing the Configuration Policies"

    data, autherr = apiCon.listConfigurationPolicies()
    # print json.dumps(data, sort_keys=True, indent=4)    

    count = data['count']
    print "There are %d CSM policies in your Halo account." % count
    policies = data['policies']
    for policy in policies:
        print "name=%-40s, id=%s, platform=%s" % (policy['name'], policy['id'], policy['platform'])

#----EXAMPLE #6-----------------------
#  Delete a Configuration Policy
#  Requires that you pass this function a policy id of a policy that exists in you Halo account
#  Essentially what you are doing is making the following REST API call:
#  DELETE https://api.cloudpassage.com/v1/policies/{policy_id}

def ex6():
    print "\nExample#6: Deleting a Configuration (CSM) Policy"
    # First we need to get the policy_id of the policy we want to delete
    # if the policy we want to delete doesn't exist then don't try to delete it.
    policy_id = 0
    data, autherr = apiCon.listConfigurationPolicies()
    policies = data['policies']
    for policy in policies:
        if policy['name'] == "Cassandra (Linux) v1":
            policy_id = policy['id']
            print "Name=%s, policy_id=%s" % (policy['name'], policy_id)
    
    # Note: if the policy_id is non zero (i.e. True) then the policy exists.
    # So now that we have the policy_id of the policy we want to
    # delete, we can go ahead and delete it if it exists.
    if policy_id:
        data, autherr = apiCon.deleteConfigurationPolicy(policy_id)
    else:
        print "The policy you are trying to delete does not exist in Halo."

#---MAIN---------------------------------------------------------------------

# One simple function call and you're off to the races!!
create_api_connection()

# Note: you can comment out the examples that you don't want to run.
# This lets you experiment easily with the code.
ex1()   # Get a list of servers and print them
ex2()   # Get a list of server groups and print them
ex3()   # Get a list of firewall policies and print them
ex6()   # Check if the Cassandra CSM policy exists, if it does delete it
ex4()   # Load the Cassandra CSM policy into Halo
ex5()   # List the configuration policies in your Halo account, You will see that the
        # Cassandra CSM policy is one of your policies
ex6()   # Delete the Cassandra CSM policy
ex5()   # List the configuration policies, this time you will see that the
        # Cassandra CSM policy is not there.



