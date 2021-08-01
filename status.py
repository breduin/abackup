"""
This is workflow status.

Status is global variable. If an error in workflow occurs,
one writes the name of the function where the exception has been
raised as the key of the 'status' and False as the value.
"""

status = {}