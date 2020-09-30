"""Setup for graded_discussion XBlock."""

import os

from setuptools import setup
__version__ = '1.0.0'


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='graded_discussion-xblock',
    version=__version__,
    description='graded_discussion XBlock',   # TODO: write a better description.
    license='UNKNOWN',          # TODO: choose a license: 'AGPL v3' and 'Apache 2.0' are popular.
    packages=[
        'graded_discussion',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'graded_discussion = graded_discussion:GradedDiscussionXBlock',
        ]
    },
    package_data=package_data("graded_discussion", ["static", "public"]),
)
