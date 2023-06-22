"""
    Module:
    Pieces of reusable code
"""
import os
import sys
import platform

class GetSystemDetails:

    def myos():
        print(sys.platform())

    def pycompiler():
        print(sys.implementation())

systw = GetSystemDetails()
systw.myos()
