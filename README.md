# subnetCalculator
Subnet calculator script using python3

## Interactive Version

Define the subnet variable interactively

Use: subnetDict = subnetCalculator(subnet)

The output will print and the subnetDict dictionary can be available to manipulate

### Example

  subnetDict.keys()

  Output: dict_keys(['Address', 'Netmask', 'Network', 'Broadcast', 'HostMin', 'HostMax', 'TotalHosts'])

## Argument Version

Run: python3 subnetArg.py 10.1.1.1/29

With 10.1.1.1/29 being the desired subnet to calculate

Script expects only one argument which is the subnet in slash notation

### Example

Terminal ~ python3 subnetArg.py 10.1.1.1/29

Output:

Address: 10.1.1.1

Netmask: 255.255.255.248

Network: 10.1.1.0/29

Broadcast: 10.1.1.7

HostMin: 10.1.1.1

HostMax: 10.1.1.6

Host/Net: 6


## Status

Limited testing has been completed but so far no additional error handling is needed if syntax is correct

Planning to add more syntax handling soon
