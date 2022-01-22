#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-loyalbooks.jarbasai=skill_loyalbooks:LoyalBooksSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-loyalbooks',
    version='0.0.1',
    description='ovos loyal books skill plugin',
    url='https://github.com/JarbasSkills/skill-loyalbooks',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_loyalbooks": ""},
    package_data={'skill_loyalbooks': ['locale/*', 'res/*', 'ui/*']},
    packages=['skill_loyalbooks'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
