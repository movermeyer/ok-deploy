# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, bad-continuation
""" Project automation for Invoke.
"""
from __future__ import absolute_import, unicode_literals

from rituals.easy import * # pylint: disable=redefined-builtin


@task
def ci(ctx): # pylint: disable=invalid-name
    """Perform continuous integration tasks."""
    ctx.run("invoke --echo --pty clean --all build --docs test check --reports")

namespace.add_task(ci)
