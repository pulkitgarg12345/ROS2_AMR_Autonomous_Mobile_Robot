from setuptools import find_packages, setup

package_name = 'pub_sub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robotics-05',
    maintainer_email='robotics-05@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        
        'pub_hello=pub_sub.pub_hello:main',
        'sub_hello=pub_sub.sub_hello:main',
        
        'pub_input=pub_sub.pub_input:main',
        'sub_input=pub_sub.sub_input:main',
        
        'pub_us=pub_sub.US_Pub:main',
        'sub_us=pub_sub.US_Sub:main',
        ],
    },
)
