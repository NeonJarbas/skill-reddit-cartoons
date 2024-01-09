#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-reddit-cartoons.jarbasai=skill_reddit_cartoons:RedditCartoonsSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-reddit-cartoons',
    version='0.0.1',
    description='ovos reddit cartoons skill plugin',
    url='https://github.com/JarbasSkills/skill-reddit-cartoons',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_reddit_cartoons": ""},
    package_data={'skill_reddit_cartoons': ['locale/*', 'res/*']},
    packages=['skill_reddit_cartoons'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
