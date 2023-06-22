"""
USES OF DATETIME IN PYTHON
    event logging — thanks to the knowledge of date and time, we are able to determine when exactly a critical error occurs in our application. 
    When creating logs, you can specify the date and time format;

    tracking changes in the database — sometimes it's necessary to store information about when a record was created or modified. 
    The datetime module will be perfect for this case;

    data validation — you'll soon learn how to read the current date and time in Python. Knowing the current date and time, you'll be able to 
    validate various types of data, e.g., whether a discount coupon entered by a user in our application is still valid;

    storing important information — can you imagine bank transfers without storing the information of when they were made? The date and time of
    certain actions must be preserved, and we must deal with it.


    the datetime module:

    MAXYEAR MINYEAR UTC     __all__ __builtins__    __cached__      __doc__ __file__        __loader__      __name__        __package__     __spec__       
    date    datetime     datetime_CAPI   sys     time    timedelta       timezone        tzinfo

"""

from datetime import date, datetime, sys, time, tzinfo, __doc__

print(dir(tzinfo.tzname()))
