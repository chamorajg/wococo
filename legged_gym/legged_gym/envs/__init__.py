
from legged_gym import LEGGED_GYM_ROOT_DIR, LEGGED_GYM_ENVS_DIR

from .h1.h1_jumpjack_config import H1JumpJackCfg, H1JumpJackCfgPPO
from .gpr.gpr_jumpjack_config import GPRJumpJackCfg, GPRJumpJackCfgPPO
from .base.legged_robot import LeggedRobot
from .base.gpr_jumpjack import GPRJumpJack
from legged_gym.utils.task_registry import task_registry

task_registry.register( "h1:jumpjack", H1JumpJack, H1JumpJackCfg(), H1JumpJackCfgPPO())
task_registry.register( "gpr:jumpjack", GPRJumpJack, GPRJumpJackCfg(), GPRJumpJackCfgPPO())




