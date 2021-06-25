# Virtual Private Network (VPN) 

## Introduction
To secure network traffic between sites and users, organisations use virtual private networks (VPNs) to create end-to-end private network connections. 
A VPN is virtual in that it carries information within a private network, but that information is actually transported over a public network.
A VPN is private in that the traffic is encripited to keep the data confidential while it is transported across the public network. 

## VPN Protocols 
- Point-to-Point Tunneling Protocol (PPTP)
- Generic Route Encapsulation (GRE)
- Layer 2 Tunelling Protocol (L2TP)
- IP Security (IPSec)
- Secure Sockets Layer (SSL)

We can create a VPN connection using any one of these protocols, but they all have different things that they provide. For example, some provide tunnelling and encryption and some only provide tunnelling. Therefore, we can use more than one protocol to provide the tunnelling and encryption for the VPN.

**VPN has two operations:**
-	Tunnelling: in order to connect two sites or two networks 
-	Encryption: in order to hide and protect information to those who do not have access to the organisation when they are passed in the tunnel. They will not be recognised by anyone on the public network.

## Types of VPN
- Host-to-Host VPN
- Host-To-Site VPN
- Site-to-Site VPN 

## Summary
We create a VPN whenever we are passing information across a public network. User’s outside the network may be able to see that traffic is exchanged between two networks but they will not be able to read into the information as it’s encrypted.
Whenever you connect to a site, you create a connection with the whole network in order to behave as part of this network. There is a private IP address inside the network when a VPN is created and a public IP address which is seen outside of the network.

