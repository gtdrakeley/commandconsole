test_data1 = """
COMMAND "some phrase"
    [a],
    [b],
    [space],
    ([leftctrl], [z]),
    DELAY 1000,
    [tab],
    [,],
    [1],
    [2],
    [num9],
    [&],
    [*],
    [\t],
    [\n],
    [\r],
    [ ]
END
"""

test_data2 = """
COMMAND "some phrase"
    [a]
END
"""

test_data3 = """
COMMAND "some phrase"
    ([leftctrl], [a])
END
"""

test_data4 = """
COMMAND "some phrase"
    DELAY 1000
END
"""

test_data5 = """
COMMAND "some phrase"
    [a],
    [b]
END
"""

test_data6 = """
COMMAND "some phrase"
    [a],
    DELAY 1000
END
"""

test_data7 = """
COMMAND "some phrase 1"
    [a]
END
COMMAND "some phrase 2"
    [b]
END
COMMAND "some phrase 3"
    [c],
    [d]
END
COMMAND "some phrase 4"
    ([e], [f]),
    DELAY 1000
END
"""

test_data8 = """
COMMAND "some phrase"
    [a],
    [b],
    [c]
END
"""
