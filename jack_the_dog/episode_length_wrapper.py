import gymnasium as gym
from gymnasium import Wrapper


class EpisodeLengthWrapper(Wrapper):
    """
    Wrapper that terminates episodes after a maximum number of steps.
    """
    
    def __init__(self, env, max_episode_steps=50):
        super().__init__(env)
        self.max_episode_steps = max_episode_steps
        self.step_count = 0
    
    def reset(self, **kwargs):
        self.step_count = 0
        return self.env.reset(**kwargs)
    
    def step(self, action):
        self.step_count += 1
        
        observation, reward, terminated, truncated, info = self.env.step(action)
        
        # Truncate if max steps reached
        if self.step_count >= self.max_episode_steps:
            truncated = True
        
        return observation, reward, terminated, truncated, info

    def get_all_states(self):
        """Forward to the underlying env so this method is visible with Gymnasium v1.0."""
        return self.env.get_all_states()

    def get_possible_actions(self, state):
        """Forward to the underlying env so this method is visible with Gymnasium v1.0."""
        return self.env.get_possible_actions(state)

    def get_next_states(self, state, action):
        """Forward to the underlying env so this method is visible with Gymnasium v1.0."""
        return self.env.get_next_states(state, action)
