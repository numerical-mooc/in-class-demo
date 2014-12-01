# --Schemes for convection
import numpy 
import matplotlib.pyplot as plt

# set the interactive mode to get an animation on screen
plt.ion()

# parameters
nx = 81      # number of x-intervals
nt = 80      # number of time intervals
sigma = 0.8  # CFL number
c  = 1.      # wave speed
dx = 4.0/(nx-1)
dt = sigma * dx/c

# initialization
x =  numpy.arange(0,4+dx,dx)
u =  numpy.zeros(nx)
un = numpy.zeros(nx)
unminus1 = numpy.zeros(nx)
u[0] = 1      # sets the LHS value to 1
un[0]    = 1
unminus1[0] = 1

# create initial plot lines        
line1,line2 = plt.plot(x,u,'k.-',x,u, 'b--')
plt.axis([0,4,-0.5,1.5])
plt.xlabel('x')
plt.ylabel('u')

for i in range(1,nx-1):
	# backward difference for first step in time
	u[i] = un[i]- sigma*( un[i]- un[i-1] )

for it in range(nt):
	for i in range(1,nx):
		# backward difference
		u[i] = un[i]- sigma*( un[i]- un[i-1] )
		# central difference
		#u[i] = un[i]- sigma/2*( un[i+1]- un[i-1] )
	u[0] = 1
	line1.set_ydata(u)
	line2.set_ydata(numpy.where(x < c*dt*(it+1), numpy.ones(nx),numpy.zeros(nx) ) )
	un = u.copy()
	
# Unset interactive mode
plt.ioff()

plt.title('nx='+str(nx)+', nt='+str(nt)+', dt='+str(dt), family='serif')
#plt.savefig('FOupwind')
# "the call to show is blocking and should be ... last"
plt.show()
