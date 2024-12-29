import glob
import os
import os.path as osp
import pdb
import sys

sys.path.append(os.getcwd())

import os
import sys
from datetime import datetime

import numpy as np
import torch

import isaacgym
from legged_gym.envs import *
from legged_gym.utils import get_args, helpers, task_registry


def train(args):
    env, env_cfg = task_registry.make_env(name=args.task, args=args)
    ppo_runner, train_cfg = task_registry.make_alg_runner(
        env=env, name=args.task, args=args
    )

    log_dir = ppo_runner.log_dir
    env_cfg_dict = helpers.class_to_dict(env_cfg)
    train_cfg_dict = helpers.class_to_dict(train_cfg)
    # Save cfgs
    os.makedirs(log_dir, exist_ok=True)

    ppo_runner.learn(
        num_learning_iterations=train_cfg.runner.max_iterations,
        init_at_random_ep_len=True,
    )


if __name__ == "__main__":
    args = get_args()
    train(args)
