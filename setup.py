from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'humanoid_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'rsp.launch.py'))),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'launch_sim.launch.py'))),
        (os.path.join('share', package_name, 'description'), glob(os.path.join('description', 'humanoid.urdf.xacro'))),
        (os.path.join('share', package_name, 'description'), glob(os.path.join('description', 'humanoid_core.xacro'))),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.dae')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.*')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.stl')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'base_link.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'Left_hand.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'Left_leg.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'lh1.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'lh2.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'lh3.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'll1.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'll2.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'll3.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'll4.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'll5.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'Right_hand.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'Right_leg.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'rh1.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'rh2.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'rh3.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'rl1.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'rl2.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'rl3.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'rl4.dae')),
        # (os.path.join('share', package_name, 'meshes')), glob(os.path.join('meshes', 'rl5.dae')),
    ],  
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kingayush',
    maintainer_email='ayush.prasad0511@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'bot_teleop='+package_name+'.bot_teleop:main',
                    'spawn_entity='+package_name+'.spawn_entity:main',
        ],
    },
)