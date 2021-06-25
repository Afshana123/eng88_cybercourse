# Network Address Translation (NAT)

We use NAT to solve the IP Address shortage problem. 
There are not enough public IPv4 addresses to assigned a unique address to each device connected to the internet 
The private addresses are used within an organisation or site to allow devices to communicate locally. 
Private IPv4 addresses cannot be routed over the internet. 

When you give a private IP address to each host in the organisation, it is then changed to a public IP address in the router.

## NAT
- To allow a device with a private Ipv4 address to access devices and resources outside of the local network, the private address must first be translated to a public address.
- NAT provides the translation of private addresses to public addresses.
- A single, public IPv4 address can be shared by hundreds, even thousand of devices (i.d private addresses)

## Types of NAT
- Static NAT: It ses a one-to-one mapping of local and global addresses 
- Dynamic NAT: It uses a pool of public addresses and assigns them on a first-come, first-serve basis.
- Port Address Translation(PAT): also known as NAT overlpad, maps multiple private IPv4 addresses to a single IPv4 address or a few addresses.
