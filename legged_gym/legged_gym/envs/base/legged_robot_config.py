from .base_config import BaseConfig


class LeggedRobotCfg(BaseConfig):
    class env:
        num_envs = 4096
        num_observations = 48
        num_privileged_obs = None  # if not None a priviledge_obs_buf will be returned by step() (critic obs for assymetric training). None is returned otherwise
        num_actions = 12
        env_spacing = 3.0  # not used with heightfields/trimeshes
        send_timeouts = True  # send time out information to the algorithm
        episode_length_s = 20  # episode length in seconds
        test = False
        # stack_obs_history = 50
        # stack_obs_dim = 101 - 38
        num_noise = 101
        period_contact = [0.1, 0.5]
        joint_hist_len = 5

    class table:
        num_table = 0

    class terrain:
        mesh_type = (
            "plane"  # "heightfield" # none, plane, heightfield or trimesh
        )
        # mesh_type = 'trimesh' # "heightfield" # none, plane, heightfield or trimesh
        horizontal_scale = 0.1  # [m]
        vertical_scale = 0.005  # [m]
        # curriculum = True
        margin = 10  # [m]
        curriculum = False
        static_friction = 1.0
        dynamic_friction = 1.0
        restitution = 0.0
        # rough terrain only:
        measure_heights = False  # keep it False
        measured_points_x = [
            -0.8,
            -0.7,
            -0.6,
            -0.5,
            -0.4,
            -0.3,
            -0.2,
            -0.1,
            0.0,
            0.1,
            0.2,
            0.3,
            0.4,
            0.5,
            0.6,
            0.7,
            0.8,
        ]  # 1mx1.6m rectangle (without center line)
        measured_points_y = [
            -0.5,
            -0.4,
            -0.3,
            -0.2,
            -0.1,
            0.0,
            0.1,
            0.2,
            0.3,
            0.4,
            0.5,
        ]
        selected = False  # select a unique terrain type and pass all arguments
        terrain_kwargs = None  # Dict of arguments for selected terrain
        max_init_terrain_level = 9  # starting curriculum state
        terrain_length = 8.0
        terrain_width = 8.0
        num_rows = 10  # number of terrain rows (levels)
        num_cols = 20  # number of terrain cols (types)
        # terrain types: [smooth slope, rough slope, stairs up, stairs down, discrete]
        terrain_proportions = [0.5, 0.5]
        # trimesh only:
        slope_treshold = 0.75  # slopes above this threshold will be corrected to vertical surfaces

        class box:
            min_height = 0.0
            max_height = 0.2
            min_length = 0.4
            max_length = 0.5
            min_width = 0.7
            max_width = 0.9
            x_range = [0.7, 2.7]
            y_range = [-0.02, 0.02]
            num_box = 4
            uneven_height_range = [0.0, 0.0]
            shift_range = [0.2, 0.4]
            boder_margin = 0.0
            num_gravel_per_box = 0
            gravel_size_range = [0.0, 0.0]

        # class motion:
        #     preset = 'T_rex'

        class gravel:
            num_gravel = 0
            x_range = [-1.0, 1.0]
            y_range = [-0.8, 0.8]
            length_range = [0.5, 1.2]
            width_range = [0.1, 0.3]
            height_range = [0.05, 0.08]
            randomize_orientation = False
            yaw_range = [1.57, 1.57]
            roll_range = [-0.1, 0.1]

        class table:
            num_table = 0

    class commands:
        curriculum = False
        max_curriculum = 1.0
        num_commands = 4  # default: lin_vel_x, lin_vel_y, ang_vel_yaw, heading (in heading mode ang_vel_yaw is recomputed from heading error)
        resampling_time = 10.0  # time before command are changed[s]
        heading_command = (
            True  # if true: compute ang vel command from heading error
        )

        class ranges:
            lin_vel_x = [-1.0, 1.0]  # min max [m/s]
            lin_vel_y = [-1.0, 1.0]  # min max [m/s]
            ang_vel_yaw = [-1, 1]  # min max [rad/s]
            heading = [-3.14, 3.14]

    class init_state:
        pos = [0.0, 0.0, 1.0]  # x,y,z [m]
        rot = [0.0, 0.0, 0.0, 1.0]  # x,y,z,w [quat]
        lin_vel = [0.0, 0.0, 0.0]  # x,y,z [m/s]
        ang_vel = [0.0, 0.0, 0.0]  # x,y,z [rad/s]
        default_joint_angles = {  # target angles when action = 0.0
            "joint_a": 0.0,
            "joint_b": 0.0,
        }

        randomize_upperbody = False

    class control:
        control_type = "P"  # P: position, V: velocity, T: torques
        # PD Drive parameters:
        stiffness = {"joint_a": 10.0, "joint_b": 15.0}  # [N*m/rad]
        damping = {"joint_a": 1.0, "joint_b": 1.5}  # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.5
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4
        action_filt = False
        torque_effort_scale = 1.0

    class asset:
        file = ""
        name = "legged_robot"  # actor name
        foot_name = "None"  # name of the feet bodies, used to index body state and contact force tensors
        penalize_contacts_on = []
        terminate_after_contacts_on = []
        disable_gravity = False
        collapse_fixed_joints = True  # merge bodies connected by fixed joints. Specific fixed joints can be kept by adding " <... dont_collapse="true">
        fix_base_link = False  # fixe the base of the robot
        default_dof_drive_mode = 3  # see GymDofDriveModeFlags (0 is none, 1 is pos tgt, 2 is vel tgt, 3 effort)
        self_collisions = 0  # 1 to disable, 0 to enable...bitwise filter
        replace_cylinder_with_capsule = True  # replace collision cylinders with capsules, leads to faster/more stable simulation
        flip_visual_attachments = (
            True  # Some .obj meshes must be flipped from y-up to z-up
        )

        density = 0.001
        angular_damping = 0.0
        linear_damping = 0.0
        max_angular_velocity = 1000.0
        max_linear_velocity = 1000.0
        armature = 0.0
        thickness = 0.01

        terminate_by_knee_distance = False
        terminate_by_feet_distance = False
        terminate_by_low_height = False
        terminate_by_lin_vel = False
        terminate_by_ang_vel = False
        terminate_by_gravity = False
        terminate_by_low_height = False
        terminate_by_y = False
        terminate_by_hip_yaw = False

        terminate_by_ref_motion_distance = False
        terminate_by_1time_motion = False

        class termination_scales:
            base_height = 0.3
            base_vel = 10.0
            base_ang_vel = 5.0
            gravity_x = 0.7
            gravity_y = 0.7
            min_knee_distance = 0.0
            global_y = 0.0
            hip_yaw_sum = 0.8

    class domain_rand:
        randomize_dof_bias = False
        max_dof_bias = 0.0
        randomize_yaw = False
        init_yaw_range = [-0.0, 0.0]

        randomize_base_com = False

        class base_com_range:
            x = [-0.1, 0.1]
            y = [-0.1, 0.1]
            z = [-0.2, 0.2]

        randomize_link_mass = False
        randomize_link_body_names = [
            "world",
            "pelvis",
            "left_hip_yaw_link",
            "left_hip_roll_link",
            "left_hip_pitch_link",
            "left_knee_link",
            "left_ankle_link",
            "right_hip_yaw_link",
            "right_hip_roll_link",
            "right_hip_pitch_link",
            "right_knee_link",
            "right_ankle_link",
            "torso_link",
            "left_shoulder_pitch_link",
            "left_shoulder_roll_link",
            "left_shoulder_yaw_link",
            "left_elbow_link",
            "right_shoulder_pitch_link",
            "right_shoulder_roll_link",
            "right_shoulder_yaw_link",
            "right_elbow_link",
        ]
        link_mass_range = [0.75, 1.25]
        randomize_pd_gain = False
        kp_range = [0.75, 1.25]
        kd_range = [0.75, 1.25]
        randomize_friction = False
        friction_range = [0.5, 1.25]
        randomize_base_mass = False
        push_robots = False
        push_interval_s = 15
        max_push_vel_xy = 1.0
        randomize_torque_rfi = False
        rfi_lim = 0.1

        randomize_rfi_lim = True
        rfi_lim_range = [0.5, 1.5]

    class rewards:
        class scales:
            termination = -0.0
            tracking_lin_vel = 1.0
            tracking_ang_vel = 0.5
            lin_vel_z = -2.0
            ang_vel_xy = -0.05
            orientation = -0.0
            torques = -0.00001
            dof_vel = -0.0
            dof_acc = -2.5e-7
            base_height = -0.0
            feet_air_time = 1.0
            collision = -1.0
            feet_stumble = -0.0
            action_rate = -0.01
            stand_still = -0.0
            joint_position = 0.0
            joint_vel = 0.0
            body_position = 0.0
            body_rotation = 0.0
            body_vel = 0.0
            body_ang_vel = 0.0

        only_positive_rewards = True  # if true negative total rewards are clipped at zero (avoids early termination problems)
        tracking_sigma = 0.25  # tracking reward = exp(-error^2/sigma)
        soft_dof_pos_limit = 1.0  # percentage of urdf limits, values above this limit are penalized
        soft_dof_vel_limit = 1.0
        soft_torque_limit = 1.0
        base_height_target = 1.0
        max_contact_force = 100.0  # forces above this value are penalized
        joint_pos_sigma = 1.0
        joint_vel_sigma = 1.0
        body_pos_sigma = 1.0
        body_rot_sigma = 1.0
        body_vel_sigma = 1.0
        body_ang_vel_sigma = 1.0
        teleop_body_rot_selection = ["pelvis"]
        teleop_body_vel_selection = ["pelvis"]
        teleop_body_pos_selection = ["pelvis"]
        teleop_body_ang_vel_selection = ["pelvis"]

        class curiosity:
            xbinset = [0.2, 2.0, 0.05]
            zbinset = [0.2, 1.6, 0.05]
            dxbinset = [-1.0, 5.0, 0.1]
            dzbinset = [-1.0, 1.0, 0.05]

        class onbox_regularization:
            elbow_ori = False
            arm_ori = False
            torso_ori = False
            jurassic = False

    class normalization:
        class obs_scales:
            lin_vel = 2.0
            ang_vel = 0.25
            dof_pos = 1.0
            dof_vel = 0.05
            height_measurements = 5.0
            body_pos = 1.0
            body_lin_vel = 1.0
            body_rot = 1.0
            delta_base_pos = 1.0
            delta_heading = 1.0

        clip_observations = 100.0
        clip_actions = 100.0

    class noise:
        add_noise = False
        noise_level = 1.0  # scales other values

        class noise_scales:
            dof_pos = 0.01  # joint angle
            dof_vel = 0.02  # joint angle velocity
            lin_vel = 0.1  # root linear velocity
            ang_vel = 0.2  # root angular velocity
            gravity = 0.05  # gravity
            height_measurements = 0.1  # height measurements
            body_pos = 0.01  # body pos in cartesian space: 19x3
            body_lin_vel = 0.01  # body velocity in cartesian space: 19x3
            body_rot = 0.01  # 6D body rotation
            ref_body_pos = 0
            ref_body_rot = 0
            ref_lin_vel = 0
            ref_ang_vel = 0
            ref_dof_pos = 0
            ref_dof_vel = 0
            ref_gravity = 0
            delta_base_pos = 0.05
            delta_heading = 0.1
            last_action = 0.0
            box_3dpos = 0.0

    # viewer camera:
    class viewer:
        debug_viz = False
        ref_env = 0
        pos = [10, 0, 6]  # [m]
        lookat = [11.0, 5, 3.0]  # [m]

    class sim:
        dt = 0.005
        substeps = 1
        gravity = [0.0, 0.0, -9.81]  # [m/s^2]
        up_axis = 1  # 0 is y, 1 is z

        class physx:
            num_threads = 10
            solver_type = 1  # 0: pgs, 1: tgs
            num_position_iterations = 4
            num_velocity_iterations = 0
            contact_offset = 0.01  # [m]
            rest_offset = 0.0  # [m]
            bounce_threshold_velocity = 0.5  # 0.5 [m/s]
            max_depenetration_velocity = 1.0
            max_gpu_contact_pairs = 2**24  #  -> needed for 8000 envs and more
            default_buffer_size_multiplier = 5
            contact_collection = (
                2  # 0: never, 1: last sub-step, 2: all sub-steps (default=2)
            )

    class motion:
        teleop = False
        visualize = False
        reset_at_start = False
        num_markers = 0
        motion_file = ""
        skeleton_file = ""
        marker_file = ""
        num_dof_pos_reference = 0
        num_dof_vel_reference = 0
        num_ef_pos_reference = 0
        num_ef_vel_reference = 0
        teleop_obs_version = ""
        teleop_selected_keypoints_names = []

        class visualize_config:
            customize_color = True
            marker_joint_colors = [
                # ['left_hip_yaw_joint', 'left_hip_roll_joint', 'left_hip_pitch_joint', 'left_knee_joint', 'left_ankle_joint', 'right_hip_yaw_joint', 'right_hip_roll_joint', 'right_hip_pitch_joint', 'right_knee_joint', 'right_ankle_joint', 'torso_joint', 'left_shoulder_pitch_joint', 'left_shoulder_roll_joint', 'left_shoulder_yaw_joint', 'left_elbow_joint', 'right_shoulder_pitch_joint', 'right_shoulder_roll_joint', 'right_shoulder_yaw_joint', 'right_elbow_joint']
                (0.157, 0.231, 0.361),  # left_hip_yaw_joint
                (0.157, 0.231, 0.361),  # left_hip_roll_joint
                (0.157, 0.231, 0.361),  # left_hip_pitch_joint
                (0.157, 0.231, 0.361),  # left_knee_joint
                (0.157, 0.231, 0.361),  # left_ankle_joint
                (0.157, 0.231, 0.361),  # right_hip_yaw_joint
                (0.157, 0.231, 0.361),  # right_hip_roll_joint
                (0.157, 0.231, 0.361),  # right_hip_pitch_joint
                (0.157, 0.231, 0.361),  # right_knee_joint
                (0.157, 0.231, 0.361),  # right_ankle_joint
                (0.765, 0.298, 0.498),  # torso_joint
                (1, 0.651, 0),  # left_shoulder_pitch_joint
                (1, 0.651, 0),  # left_shoulder_roll_joint
                (1, 0.651, 0),  # left_shoulder_yaw_joint
                (1, 0.651, 0),  # left_elbow_joint
                (1, 0.651, 0),  # right_shoulder_pitch_joint
                (1, 0.651, 0),  # right_shoulder_roll_joint
                (1, 0.651, 0),  # right_shoulder_yaw_joint
                (1, 0.651, 0),  # right_elbow_joint
            ]


class LeggedRobotCfgPPO(BaseConfig):
    seed = 1
    runner_class_name = "OnPolicyRunner"

    class policy:
        class_name = "ActorCritic"
        init_noise_std = 1.0
        actor_hidden_dims = [512, 256, 128]
        critic_hidden_dims = [512, 256, 128]
        activation = (
            "elu"  # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
        )
        # only for 'ActorCriticRecurrent':
        # rnn_type = 'lstm'
        # rnn_hidden_size = 512
        # rnn_num_layers = 1

    class algorithm:
        class_name = "PPO"
        # training params
        value_loss_coef = 1.0
        use_clipped_value_loss = True
        clip_param = 0.2
        entropy_coef = 0.01
        num_learning_epochs = 5
        num_mini_batches = 4  # mini batch size = num_envs*nsteps / nminibatches
        learning_rate = 1.0e-3  # 5.e-4
        schedule = "adaptive"  # could be adaptive, fixed
        gamma = 0.99
        lam = 0.95
        desired_kl = 0.01
        max_grad_norm = 1.0

    class runner:
        num_steps_per_env = 24  # per iteration
        max_iterations = 100000  # number of policy updates
        empirical_normalization = False

        # logging
        save_interval = (
            200  # check for potential saves every this many iterations
        )
        experiment_name = "test"
        run_name = ""
        # load and resume
        resume = False
        load_run = -1  # -1 = last run
        checkpoint = -1  # -1 = last saved model
        resume_path = None  # updated from load_run and chkpt
