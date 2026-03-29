'''
*
*   ===================================================
*       CropDrop Bot (CB) Theme [eYRC 2025-26]
*   ===================================================
*
*  This script is intended to be an Boilerplate for 
*  Task 1B of CropDrop Bot (CB) Theme [eYRC 2025-26].
*
*  Filename:		Qlearning.py
*  Created:		    24/08/2025
*  Last Modified:	11/10/2025
*  Author:		    e-Yantra Team + Customized by Nitin Thakur
*  Team ID:		    [ CB_2202 ]
*
*
*
*
*
*
*
*
*
*****************************************************************************************
'''

import numpy as np
import random
import pickle
import os

class QLearningController:
    def __init__(self, n_states=32, n_actions=3, filename="q_table.pkl"): 
        """
        Initialize the Q-learning controller.
        """
        self.n_states = n_states
        self.n_actions = n_actions
        self.filename = filename

        # === Hyperparameters ===
        self.lr = 0.3             # Learning rate (alpha)
        self.gamma = 0.9          # Discount factor
        self.epsilon = 0.2        # Exploration rate (epsilon)

        # === Q-table ===
        self.q_table = np.zeros((n_states, n_actions))

        # === Actions ===
        # 0: Left, 1: Forward, 2: Right
        self.action_list = [0, 1, 2]

        # === Motor mappings [Left_speed, Right_speed] ===
        self.actions = {
            0: (0.3, 0.7),   # Left
            1: (0.7, 0.7),   # Forward
            2: (0.7, 0.3)    # Right
        }

    # ---------------------------------------------------------------------
    def Get_state(self, sensor_data):
        """
        Convert binary sensor readings (list of 5) into a discrete state index.
        """
        if len(sensor_data) != 5:
            raise ValueError("Sensor data must contain 5 binary values.")

        # Convert binary array to integer (e.g., [0,1,1,0,0] -> 12)
        state = 0
        for i, bit in enumerate(sensor_data):
            state += bit << (4 - i)  # 4-i ensures leftmost bit is MSB

        return state

    # ---------------------------------------------------------------------




    def Calculate_reward(self, state, reached_goal=False, hit_obstacle=False):
        """
        Return reward based on environment conditions.
        """
        if reached_goal:
            return +10
        elif hit_obstacle:
            return -1
        else:
            return 0







    # ---------------------------------------------------------------------
    def choose_action(self, state):
        """
        Epsilon-greedy action selection.
        """
        if random.uniform(0, 1) < self.epsilon:
            # Exploration
            action = random.choice(self.action_list)
        else:
            # Exploitation (choose best known action)
            action = np.argmax(self.q_table[state])

        return action

    # ---------------------------------------------------------------------


    
    def update_q_table(self, state, action, reward, next_state):
        """
        Standard Q-learning update rule:
        Q(s,a) ← Q(s,a) + α * [r + γ * max_a' Q(s',a') − Q(s,a)]
        """
        a_idx = self.action_list.index(action)
        old_value = self.q_table[state][a_idx]
        next_max = np.max(self.q_table[next_state])

        # Q-learning update
        new_value = old_value + self.lr * (reward + self.gamma * next_max - old_value)
        self.q_table[state][a_idx] = new_value

    # ---------------------------------------------------------------------
    def perform_action(self, action):
        """
        Return normalized motor speeds [0–1] based on action.
        """
        if action not in self.actions:
            raise ValueError("Invalid action ID")

        left_speed, right_speed = self.actions[action]
        return left_speed, right_speed

    # ---------------------------------------------------------------------
    def save_q_table(self):
        """
        Save Q-table for persistent learning.
        """
        with open(self.filename, 'wb') as f:
            pickle.dump({
                'q_table': self.q_table,
                'epsilon': self.epsilon,
                'n_action': self.n_actions,
                'n_states': self.n_states
            }, f)

    # ---------------------------------------------------------------------
    def load_q_table(self):
        """
        Load previously saved Q-table if available.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                data = pickle.load(f)
            self.q_table = data.get('q_table', self.q_table)
            self.epsilon = data.get('epsilon', self.epsilon)
            self.n_actions = data.get('n_action', self.n_actions)
            self.n_states = data.get('n_states', self.n_states)
            return True
        return False
