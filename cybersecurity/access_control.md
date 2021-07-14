### Access Control Models 
Discretionary AC (DAC)
Mandatory AC (MAC)
Role-based AC (RBAC)
Attribute-based AC (ABAC)
Rule-based AC (RBAC)
Time-based AC (TBAC)
The principle of least privilege

### AAA Framework
Authentication -Users and admins must prove that they are who they say they are
Authorisation - Authorisation services determine which resources the user can access and which operations the user is allowed to perform
Accounting - Accounting records what the user does, including what is accessed, the amount of time the resource is accessed and any changes that were made

### AAA Architecture 
Local AAA Authentication
- this method is sometimes known as self-contained authentication because it authenticates users against locally stored usernames and passwords
Server-based AAA Authentication
- This method authenticates against a central AAA server that contains the usernames and passwords for all users

### AAA Protocols 
Remote authentication dial-in user service (RADIUS)
- a protocol that supports centralised authentication, authorisation and accounting management for clients that establish connection with a network and intend to use any of the provided services
Terminal Access Controller Access Control System (TACAS_
- an old authentication protocol that was used on UNIX networks to allow a remote server to forward login requests to authentication servers for access control purposes
TACACS+
- released by Cisco as a response to RADIUS
- Cisco believed that RADIUS could use some design alterations
