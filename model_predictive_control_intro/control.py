from apm import *

s = 'http://byu.apmonitor.com'
a = 'myApp'

# clear prior application
apm(s,a,'clear all')

# load model and data
apm_load(s,a,'model.apm')
csv_load(s,a,'data.csv')

# specify FV, MV, SV, CV
apm_info(s,a,'FV','K')
apm_info(s,a,'MV','u')
apm_info(s,a,'SV','x')
apm_info(s,a,'CV','y')

# configuration parameters
apm_option(s,a,'nlc.imode',6)
apm_option(s,a,'nlc.nodes',3)

# turn on MV as a degree of freedom
apm_option(s,a,'u.status',1)
# turn on CV to add terms to objective function
apm_option(s,a,'y.status',1)

# tune MV in the controller
apm_option(s,a,'u.lower',0)
apm_option(s,a,'u.upper',100)
apm_option(s,a,'u.dcost',0.1)

# tune CV in the controller
apm_option(s,a,'y.tau',5)
apm_option(s,a,'y.sphi',26)
apm_option(s,a,'y.splo',24)

# solve and retrieve results
output = apm(s,a,'solve')
print(output)

# open web-viewer
apm_web(s,a)

# retrieve solution
z = apm_sol(s,a)
