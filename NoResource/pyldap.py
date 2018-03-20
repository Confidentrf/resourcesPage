import sys
import ldap


Server = "ldap://university.liberty.edu"
DN, Secret, un = sys.argv[1:4]

Base = "dc=university,dc=liberty,dc=edu"
Scope = ldap.SCOPE_SUBTREE
Filter = "(&(objectclass=user)(|(memberof=CN=ITCampusSupportSW,OU=Distribution Lists,OU=Exchange,DC=University,DC=liberty,DC=edu)(memberof=CN=ITCampusSupportSW,OU=Distribution,OU=Exchange,DC=Exchange,DC=University,DC=liberty,DC=edu)(memberof=CN=Network Services - VoIP,OU=AssignmentGroups,OU=ServiceNow,OU=IS,OU=FSA,DC=University,DC=liberty,DC=edu)))"
Attrs = ["displayName"]

l = ldap.initialize(Server)
l.protocol_version = 3
print l.simple_bind_s(DN, Secret)

r = l.search(Base, Scope, Filter, Attrs)
Type,user = l.result(r,60)
Name,Attrs = user[0]
if hasattr(Attrs, 'has_key') and Attrs.has_key('displayName'):
  displayName = Attrs['displayName'][0]
  print displayName

sys.exit()
