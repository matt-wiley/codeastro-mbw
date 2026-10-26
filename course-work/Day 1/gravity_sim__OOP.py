# Object-Oriented Programming
import json

class Particle(object):
    """
    A simulated particle that moves in 3D

    TODO: this is just a place holder for now. We need to figure out what fields go in here. 
    """
    def __init__(self):
        pass


class FreeFallParticle(Particle):
    """
    Simulate a particle falling due to Earth's gravity. Particle is stationary at first

    Args:
        height (float): a height in meters
        dt (float): timestep of the simulation in seconds
    """
    def __init__(self, height, dt=0.1):
        """
        Function that is run to initialize the class.

        The input `self` is required for functions that belong to an object,
        meaning that you want to make the function access and/or depend on the 
        attributes of the object (e.g., self.time, and self.velocity below)
        """
        # let's initalize it's parent class (empty for now because it is a blank class)
        super().__init__()

        # note that we are not using the astropy.units class here as we haven't talked about it yet! But it could be useful!
        self.height = height # current height [meters]
        self.velocity = 0 # current velocity [meters/second]
        self.time = 0 # time elapsed [seconds]
        self.dt = dt # timestep of the simulation [seconds]
        self.g = -9.8 # gravitational acceleration (Don't change) [meters/second^2]


    def get_num_steps_run(self):
        """
        Function that returns the number of timesteps that have run by comparing self.time with self.dt

        Returns:
            num_steps (int): number of time steps already completed in the simulation
        """
        num_steps = int(self.time / self.dt)
        return num_steps


    ##### Activity ######
    """
    Add functionality to advance the particle's height by one time step at a time. (hint: implement the function below).
    Then use this code to calculate how long it takes for the particle to fall down from a height of 10 meters.

    Some useful equations for how to calculate the particle's new state at the next time step.
    Pseudo code below:
    acceleration = g
    new_velocity = current_velocity + acceleration * dt
    new_height = current_height + new_velocity * dt

    Add inputs and outputs. 
    """
    def simulate_timestep(self):
        """
        Advance the simulation time by a single timestep (self.dt). 
        Update the simulation with the new time, height, and velocity

        Returns:
            height (float): the current height in meters
        """
        acceleration = self.g
                
        acceleration_delta = acceleration * self.dt
        new_velocity = self.velocity + acceleration_delta

        height_delta = new_velocity * self.dt
        new_height = self.height + height_delta
        
        new_time = self.time + self.dt

        # We've overshot the mark (we're in the ground), so adjust the 
        # calculation to account for the partial step
        if new_height < 0:
            distance_to_ground = self.height
            distance_of_full_step = self.height - new_height
            percent_of_dt_until_impact = distance_to_ground / distance_of_full_step

            final_dt = self.dt * percent_of_dt_until_impact 
            final_acceleration_delta = acceleration * final_dt
            final_velocity = self.velocity + final_acceleration_delta

            final_time_calc = self.time + final_dt

            final_height_delta = final_velocity * final_dt
            final_height_calc = self.height + final_height_delta ## Hopefully zero-ish?

            self.time = final_time_calc
            self.velocity = final_velocity
            self.height = 0.0

            debug_info = dict(
                                percent_of_dt_until_impact=percent_of_dt_until_impact,
                                final_dt=final_dt,
                                final_height_delta=final_height_delta,
                                final_height_calc=final_height_calc,
                                final_time_calc=final_time_calc,
                            )

            # print(json.dumps(debug_info, indent=4))
            return self.height

        else:
            self.velocity = new_velocity
            self.height = new_height
            self.time = new_time

            # self.velocity = self.velocity + acceleration * self.dt
            # self.height = self.height + self.velocity * self.dt
            # self.time = self.time + self.dt

            return self.height




if __name__ == "__main__":
    ball = FreeFallParticle(height=10, dt=0.001) # start out a 10 m above the ground
    print(ball.time, ball.velocity, ball.height)

    while ball.height > 0:
        ball.simulate_timestep()
        print(ball.time, ball.velocity, ball.height)