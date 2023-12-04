
import time


class PID_Controller:
    # set up attributes of controller
    def __init__(self, Kp, Ki =0., Kd=0., ref=0., offset = 0., lims=(None, None)):
        # controller coefficients
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        # reference
        self.ref = ref

        # initialize integrator (riemann summer) to 0 initially
        self._integral = 0

        # initialize previous time and error
        self.time_prev = None
        self.error_prev = None

        # offset, output value when there is no error
        self.offset = offset
        
        # lower and upper limits for the output manipulated variable
        self._lims = lims


    def __call__(self, cur, time_current=time.time_ns()/1_000_000_000):
        # error on reference
        error = self.ref - cur

        # proportional control
        proportional = self.Kp * error

        # if first iteration no derivative/integral
        if self.error_prev is None or self.time_prev is None:
            derivative = 0
        else:
            # derivative control
            de = error - self.error_prev # delta error
            dt =  time_current - self.time_prev # delta time
                
            derivative = self.Kd*(de/dt) 

            # integral control
            self._integral += self.Ki*error*dt 

        # manipulated variable output
        out = self.offset + proportional + self._integral + derivative

        # update tracker variables
        self.error_prev = error
        self.time_prev = time_current

        # clamp output
        return self._clamp(out) 
        

    def _clamp(self, val):
        if self._lims[0] is not None:
            val = max(self._lims[0], val)
        if self._lims[1] is not None:
            val = min(self._lims[1], val)
        
        return val