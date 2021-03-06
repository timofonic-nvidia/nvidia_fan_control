"""
Module with general utilities such as parsers
"""

import shlex
import subprocess

def command_parser(oscommand):
    """
    Simple OS command parser.

    Args:
    	osCommand: The command to be parsed.
    	e.g.: 'nvidia-smi -L'

    Returns:
    	A string corresponding to the osCommand stdout.
    	e.g.: GPU 0: GeForce GTX 960 (UUID: GPU-1d11ae72-cd45-276f-0a0d-b2be8b74e4da)


    """
    command = shlex.split(oscommand)
    result = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)

    return result.stdout.read()

def get_gpu_count():
    """
    Get local machine total attached gpu devices

    Returns:
        Total attached GPU count

    """

    return int(command_parser("nvidia-smi --query-gpu=count --format=csv,noheader"))


def get_gpu_info(slot):
    """
    Get data from GPU in `slot`

    Returns:
        {slot,name} dict

    """
    gpu_data = {"slot":slot}

    command = "nvidia-smi -i %d --query-gpu=name --format=csv,noheader" % slot
    gpu_data["name"] = command_parser(command).strip()

    return gpu_data
