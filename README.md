#GotoNewest

A small tool to obtain the newest directory created in any base directory. It
reads the base directory from a configuration file, and returns the latest
subdirectory based on modified time in that directory.

Originally the intention was to to run this as a standalone tool. However,
Python does not allow permanent directory switching (it reverts back to the
original directory as soon as the program exits). That is not a workable
solution.

Alternative: This gist here:

*https://gist.github.com/ambidextrousTx/af77f6819d066ab2d510*

~Ambidextrous
Feb, 2015
