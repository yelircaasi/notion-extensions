class dotdict(dict):
    """dot.notation access to dictionary attributes"""

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def as_dotdict(nested_dict):
    nested_dict = dotdict(nested_dict)
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            nested_dict[key] = as_dotdict(value)
    return nested_dict


WEEKDAY_DICT = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

MONTH_DICT = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

TEN_DAY_DICT = as_dotdict(
    {
        "fri0": (-1, 5),
        "sat0": (-1, 6),
        "sun0": (-1, 7),
        "mon": (0, 1),
        "tue": (0, 2),
        "wed": (0, 3),
        "thu": (0, 4),
        "fri": (0, 5),
        "sat": (0, 6),
        "sun": (0, 7),
    }
)
