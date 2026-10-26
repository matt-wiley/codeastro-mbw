from dataclasses import dataclass
import json

@dataclass
class FuncParticle():

    def __init__(self, initial_height, initial_velocity=0):
        self.height = initial_height
        self.velocity = initial_velocity

    def __dict__(self):
        return dict(
            height=self.height,
            velocity=self.velocity
        )

def freefall_timestep(particle: FuncParticle, dt=0.1) -> FuncParticle:
    acceleration = -9.8

    new_velocity = particle.velocity + acceleration * dt
    new_height = particle.height + new_velocity * dt

    new_particle = FuncParticle(
        new_height,
        new_velocity
    )
    return new_particle


def freefall_sim():
    time_step_delta = 0.1
    ball = FuncParticle(1)
    current_time = 0
    ball_history: list[tuple] = [(current_time, ball)]


    while ball.height > 0:
        current_time = current_time + time_step_delta
        ball = freefall_timestep(ball, time_step_delta)
        ball_history.append((current_time, ball))

    return ball_history


def freefall_heights_for_times():
    history = freefall_sim()

    times = [ x[0] for x in history ]
    heights = [ x[1].height for x in history ]

    return (
        heights,
        times
    )


if __name__ == "__main__":
    results = freefall_heights_for_times()
    print(results)

    