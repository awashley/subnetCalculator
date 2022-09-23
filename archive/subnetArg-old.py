#!/usr/bin/env python
import sys


#default defined test subnet
#subnet = '10.2.3.4/28'
#
def findSubnetrangeFourth(slashMask, fourthOctet):
    #function to narrow the details for subnets specifically defined in the fourth octet
    #the lastDetails dictionary will be return for use in the subnetCalculator function
    lastDetails = {}
    subnetFour = 0
    startFour = 0
    endFour = 0
    broadFour = 0
    usable = 0
    if slashMask == 24:
        amount = 1
        space = 256
        mask = '255.255.255.0'
    elif slashMask == 25:
        amount = 2
        space = 128
        mask = '255.255.255.128'
    elif slashMask == 26:
        amount = 4
        space = 64
        mask = '255.255.255.192'
    elif slashMask == 27:
        amount = 8
        space = 32
        mask = '255.255.255.224'
    elif slashMask == 28:
        amount = 16
        space = 16
        mask = '255.255.255.240'
    elif slashMask == 29:
        amount = 32
        space = 8
        mask = '255.255.255.248'
    elif slashMask == 30:
        amount = 64
        space = 4
        mask = '255.255.255.252'
    elif slashMask == 31:
        amount = 128
        space = 2
        mask = '255.255.255.254'
    field = []
    count = 0
    for i in range(amount):
        if count == 0:
            field.append(count)
            count = count + space
        elif count == 2:
            field.append(count)
            count = count + space
        else:
            count = count + space
            field.append(count)
    for section in field:
        endSection = section + space
        if fourthOctet in range(section, endSection):
            lastDetails['subnetFour'] = section
            lastDetails['startFour'] = section + 1
            lastDetails['endFour'] = section + space - 2
            lastDetails['broadFour'] = section + space - 1
            lastDetails['usable'] = space - 2
            lastDetails['mask'] = mask
    return lastDetails

def findSubnetrangeThird(slashMask, thirdOctet):
    #function to narrow the details for subnets specifically defined in the third octet
    #the lastDetails dictionary will be return for use in the subnetCalculator function
    lastDetails = {}
    subnetFour = 0
    startFour = 0
    endFour = 0
    broadFour = 0
    usable = 0
    if slashMask == 16:
        amount = 1
        space = 256
        mask = '255.255.0.0'
    elif slashMask == 17:
        amount = 2
        space = 128
        mask = '255.255.128.0'
    elif slashMask == 18:
        amount = 4
        space = 64
        mask = '255.255.192.0'
    elif slashMask == 19:
        amount = 8
        space = 32
        mask = '255.255.224.0'
    elif slashMask == 20:
        amount = 16
        space = 16
        mask = '255.255.240.0'
    elif slashMask == 21:
        amount = 32
        space = 8
        mask = '255.255.248.0'
    elif slashMask == 22:
        amount = 64
        space = 4
        mask = '255.255.252.0'
    elif slashMask == 23:
        amount = 128
        space = 2
        mask = '255.255.254.0'
    field = []
    count = 0
    for i in range(amount):
        field.append(count)
        count = count + space
    for section in field:
        endSection = section + space
        if thirdOctet in range(section, endSection):
            lastDetails['subnetThird'] = f"{section}.0"
            lastDetails['startThird'] = f"{section}.1"
            findThird = section + space
            lastDetails['endThird'] = f"{findThird - 1}.254"
            lastDetails['broadThird'] = f"{findThird - 1}.255"
            subnetSpace = space * 256
            lastDetails['usable'] = subnetSpace - 2
            lastDetails['mask'] = mask
    return lastDetails

def findSubnetrangeSecond(slashMask, secondOctet):
    #function to narrow the details for subnets specifically defined in the second octet
    #the lastDetails dictionary will be return for use in the subnetCalculator function
    lastDetails = {}
    if slashMask == 8:
        amount = 1
        space = 256
        mask = '255.0.0.0'
    elif slashMask == 9:
        amount = 2
        space = 128
        mask = '255.128.0.0'
    elif slashMask == 10:
        amount = 4
        space = 64
        mask = '255.192.0.0'
    elif slashMask == 11:
        amount = 8
        space = 32
        mask = '255.224.0.0'
    elif slashMask == 12:
        amount = 16
        space = 16
        mask = '255.240.0.0'
    elif slashMask == 13:
        amount = 32
        space = 8
        mask = '255.248.0.0'
    elif slashMask == 14:
        amount = 64
        space = 4
        mask = '255.252.0.0'
    elif slashMask == 15:
        amount = 128
        space = 2
        mask = '255.254.0.0'
    field = []
    count = 0
    for i in range(amount):
        field.append(count)
        count = count + space
    for section in field:
        endSection = section + space
        if secondOctet in range(section, endSection):
            lastDetails['subnetSecond'] = f"{section}.0.0"
            lastDetails['startSecond'] = f"{section}.0.1"
            findSecond = section + space
            lastDetails['endSecond'] = f"{findSecond - 1}.255.254"
            lastDetails['broadSecond'] = f"{findSecond - 1}.255.255"
            subnetSpace = space * 65536
            lastDetails['usable'] = subnetSpace - 2
            lastDetails['mask'] = mask
    return lastDetails


def findSubnetrangeFirst(slashMask, firstOctet):
    #function to narrow the details for subnets specifically defined in the first octet
    #the lastDetails dictionary will be return for use in the subnetCalculator function
    lastDetails = {}
    if slashMask == 1:
        amount = 2
        space = 128
        mask = '128.0.0.0'
    elif slashMask == 2:
        amount = 4
        space = 64
        mask = '192.0.0.0'
    elif slashMask == 3:
        amount = 8
        space = 32
        mask = '224.0.0.0'
    elif slashMask == 4:
        amount = 16
        space = 16
        mask = '240.0.0.0'
    elif slashMask == 5:
        amount = 32
        space = 8
        mask = '248.0.0.0'
    elif slashMask == 6:
        amount = 64
        space = 4
        mask = '252.0.0.0'
    elif slashMask == 7:
        amount = 128
        space = 2
        mask = '254.0.0.0'
    field = []
    count = 0
    for i in range(amount):
        field.append(count)
        count = count + space
    for section in field:
        endSection = section + space
        if firstOctet in range(section, endSection):
            lastDetails['subnetFirst'] = f"{section}.0.0.0"
            lastDetails['startFirst'] = f"{section}.0.0.1"
            findFirst = section + space
            lastDetails['endFirst'] = f"{findFirst - 1}.255.255.254"
            lastDetails['broadFirst'] = f"{findFirst - 1}.255.255.255"
            subnetSpace = space * 16777216
            lastDetails['usable'] = subnetSpace - 2
            lastDetails['mask'] = mask
    return lastDetails

def octetCheck(octet):
    checkCode = None
    if octet in range(0,256):
        checkCode = 1
    else:
        checkCode = 0
    return checkCode



def subnetCalculator(subnet):
    #function to parse the octets and finish the calculation of the subnet
    #this function works for /1 to /31 subnets only
    #
    #define the empty result
    resultDict = {}
    #define the empty slashMask
    slashMask = None
    #breakdown the subnet string with syntax error bailouts
    octetList = subnet.split('.')
    if octetList[0].isnumeric() == False:
        print('Error: The first octet input is not a number')
        return
    firstOctet = int(octetList[0])
    if octetCheck(firstOctet) == 0:
        print(f"Error: The first octet input: {firstOctet} is out of range")
        return
    if octetList[1].isnumeric() == False:
        print('Error: The second octet input is not a number')
        return
    secondOctet = int(octetList[1])
    if octetCheck(secondOctet) == 0:
        print(f"Error: The second octet input: {secondOctet} is out of range")
        return
    if octetList[2].isnumeric() == False:
        print('Error: The third octet input is not a number')
        return
    thirdOctet = int(octetList[2])
    if octetCheck(thirdOctet) == 0:
        print(f"Error: The third octet input: {thirdOctet} is out of range")
        return
    if octetList[3].find('/') == -1:
        print('Error: Missing Slash Notation for the Subnet')
        return
    if octetList[3].split('/')[0].isnumeric() == False:
        print('Error: The fourth octet input is not a number')
        return
    fourthOctet = int(octetList[3].split('/')[0])
    if octetCheck(fourthOctet) == 0:
        print(f"Error: The fourth octet input: {fourthOctet} is out of range")
        return
    if octetList[3].split('/')[1] == '':
        print('Error: Slash Notation is Empty')
        return
    slashMask = int(octetList[3].split('/')[1])
    #
    #work with small subnets defined in the fourth octet
    if slashMask in range(24,32):
        lastDetails = findSubnetrangeFourth(slashMask, fourthOctet)
        resultDict['Address'] = subnet.split('/')[0]
        resultDict['Netmask'] = lastDetails['mask']
        resultDict['Network'] = f"{firstOctet}.{secondOctet}.{thirdOctet}.{lastDetails['subnetFour']}/{slashMask}"
        resultDict['Broadcast'] = f"{firstOctet}.{secondOctet}.{thirdOctet}.{lastDetails['broadFour']}"
        resultDict['HostMin'] = f"{firstOctet}.{secondOctet}.{thirdOctet}.{lastDetails['startFour']}"
        resultDict['HostMax'] = f"{firstOctet}.{secondOctet}.{thirdOctet}.{lastDetails['endFour']}"
        resultDict['TotalHosts'] = lastDetails['usable']
    #work with medium subnets defined in the third octet
    elif slashMask in range(16,24):
        lastDetails = findSubnetrangeThird(slashMask, thirdOctet)
        resultDict['Address'] = subnet.split('/')[0]
        resultDict['Netmask'] = lastDetails['mask']
        resultDict['Network'] = f"{firstOctet}.{secondOctet}.{lastDetails['subnetThird']}/{slashMask}"
        resultDict['Broadcast'] = f"{firstOctet}.{secondOctet}.{lastDetails['broadThird']}"
        resultDict['HostMin'] = f"{firstOctet}.{secondOctet}.{lastDetails['startThird']}"
        resultDict['HostMax'] = f"{firstOctet}.{secondOctet}.{lastDetails['endThird']}"
        resultDict['TotalHosts'] = lastDetails['usable']
    #work with larger subnets defined in the second octet
    elif slashMask in range(8,16):
        lastDetails = findSubnetrangeSecond(slashMask, secondOctet)
        resultDict['Address'] = subnet.split('/')[0]
        resultDict['Netmask'] = lastDetails['mask']
        resultDict['Network'] = f"{firstOctet}.{lastDetails['subnetSecond']}/{slashMask}"
        resultDict['Broadcast'] = f"{firstOctet}.{lastDetails['broadSecond']}"
        resultDict['HostMin'] = f"{firstOctet}.{lastDetails['startSecond']}"
        resultDict['HostMax'] = f"{firstOctet}.{lastDetails['endSecond']}"
        resultDict['TotalHosts'] = lastDetails['usable']
    #work with the largest subnets defined in the first octet
    elif slashMask in range(1,8):
        lastDetails = findSubnetrangeFirst(slashMask, firstOctet)
        resultDict['Address'] = subnet.split('/')[0]
        resultDict['Netmask'] = lastDetails['mask']
        resultDict['Network'] = f"{lastDetails['subnetFirst']}/{slashMask}"
        resultDict['Broadcast'] = f"{lastDetails['broadFirst']}"
        resultDict['HostMin'] = f"{lastDetails['startFirst']}"
        resultDict['HostMax'] = f"{lastDetails['endFirst']}"
        resultDict['TotalHosts'] = lastDetails['usable']
    #bail out on syntax for the subnet
    else:
        if slashMask == 32:
            print(f"Informational: No Need to Calculate a /{slashMask} Subnet!!")
            return
        else:
            print(f"Error: Slash Notation for Mask: {slashMask} is Invalid")
            return
    #print the results dictionary for output and verification in the interactive prompt
    if lastDetails:
        print(f"Address: {resultDict['Address']}")
        print(f"Netmask: {resultDict['Netmask']}")
        print(f"Network: {resultDict['Network']}")
        print(f"Broadcast: {resultDict['Broadcast']}")
        print(f"HostMin: {resultDict['HostMin']}")
        print(f"HostMax: {resultDict['HostMax']}")
        print(f"Host/Net: {resultDict['TotalHosts']}")
        return resultDict
    else:
        print('Error information not collected')
        return

def main():
    #Key on the subnet sting variable to calcuate the subnet details
    subnet = sys.argv[1]
    subnetDict = subnetCalculator(subnet)
    #
if __name__ == '__main__':
    main()
