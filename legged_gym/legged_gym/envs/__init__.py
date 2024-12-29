from legged_gym import LEGGED_GYM_ENVS_DIR, LEGGED_GYM_ROOT_DIR
from legged_gym.utils.task_registry import task_registry

from .base.gpr_jumpjack import GPRJumpJack
from .base.h1_jumpjack import H1JumpJack
from .base.legged_robot import LeggedRobot
from .gpr.gpr_jumpjack_config import GPRJumpJackCfg, GPRJumpJackCfgPPO
from .h1.h1_jumpjack_config import H1JumpJackCfg, H1JumpJackCfgPPO

task_registry.register(
    "h1:jumpjack", H1JumpJack, H1JumpJackCfg(), H1JumpJackCfgPPO()
)
task_registry.register(
    "gpr:jumpjack", GPRJumpJack, GPRJumpJackCfg(), GPRJumpJackCfgPPO()
)
