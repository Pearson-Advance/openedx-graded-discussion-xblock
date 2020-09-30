# openedx-graded-discussion-xblock

This xblock allows course staff users to grade student discussion entries.

## INSTALLATION.

### Virtual env:

```
pip install git+https://github.com/Pearson-Advance/openedx-graded-discussion-xblock.git@v1.0.0#egg=openedx-graded-discussion-xblock==1.0.0
```

### Platform requirements:

In requirements/edx/github.txt, add:

```
git+https://github.com/Pearson-Advance/openedx-graded-discussion-xblock.git@v1.0.0#egg=openedx-graded-discussion-xblock==1.0.0
```

## CONFIGURATION.

Before proceed, an OpenedX client-id & client-secret credentials are required. You can generate them from the admin interface -> Django OAuth Toolkit.

Depending on the environment, add these settings to devstack_docker.py or production.py:

```
XBLOCK_SETTINGS.update({
    'GradedDiscussionXBlock': {
        'client_id': 'openedx-client-id',
        'client_secret': 'openedx-client-secret',
    },
})
```

## Course Authoring in Studio.

### Add to advanced settings:

- Go to Course Settings -> Advanced settings.
- Add: "graded_discussion" to the Advanced Module list.
- Save changes.

### Add the component:

- Create a Section, Sub-section and Unit, if you haven't already.
- In the "Add New Component" interface, you should now see an "Advanced" button.
- Click "Advanced" and choose "Graded Discussion".
