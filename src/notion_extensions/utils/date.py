from datetime import date
from typing import Union
from itertools import product

from notion_extensions.utils.dicts import (
    MONTH_DICT,
    WEEKDAY_DICT,
    TEN_DAY_DICT,
    dotdict,
)


todays_date = date.today()


def parse_key(key: str) -> tuple:
    strings = key.split("_")
    if len(strings) == 3:
        day, hour, min = strings
        week, day = TEN_DAY_DICT[day]
        hour, min = map(int, (hour, min))
        return (week, day, hour, min)
    elif len(strings) == 1:
        return TEN_DAY_DICT[key]


def parse_time_str(key: str) -> Union[int, tuple]:
    strings = key.split(":")
    # if len(strings) == 1:
    #     return int(strings[0])
    # elif len(strings) == 2:
    if len(strings) == 2:
        hour, min = map(int, strings)
    else:
        raise ValueError
    return (hour, min)


def unparse(week, day, hour=None, minute=None) -> str:
    day = {1: "mon", 2: "tue", 3: "wed", 4: "thu", 5: "fri", 6: "sat", 7: "sun"}[day]
    if week:
        day += "0"
    if (hour is not None) and (minute is not None):
        day += f"_{hour:02d}_{minute:02d}"
    return day


def get_new_date(week, day, today: date = todays_date) -> date:
    
    today_weekday = today.isoweekday()
    today_ordinal = today.toordinal()
    is_planning = today_weekday > 4

    day_diff = (day - today_weekday) % 7 + 7 * (day > 4 and week==0)
    day_diff = day_diff if (day_diff < 11 or not is_planning) else day_diff % 7
    print(day_diff)
    next_day = today_ordinal + day_diff
    new_date = date.fromordinal(next_day)
    return new_date


def fix_date(date_str: str, week, day) -> str:
    new_date = get_new_date(week, day)
    return str(new_date) + date_str[10:]


# def filt(k):
#     return k[0] == (-1 if today_weekday in {1, 2, 3, 4} else 0)


def fix_day(week, day):
    new_date = get_new_date(week, day)
    return f"{WEEKDAY_DICT[day]}, {MONTH_DICT[new_date.month]} {str(new_date.day)}, {str(new_date.year)}"


def get_times_from_recipe_agenda(agenda: dotdict) -> list:
    days: list = agenda.days
    times: list = agenda.times
    if days:
        days = list(map(parse_key, days))
    else:
        today_weekday = date.today().isoweekday()
        if today_weekday > 4:
            days = [(0, 1), (0, 2), (0, 3), (0, 4)]
        else:
            days = [(-1, 5), (-1, 6), (-1, 7), (0, 5), (0, 6), (0, 7)]
    if times:
        times = list(map(parse_time_str, times))
    else:
        _ = [times.extend([(hour, 0), (hour, 30)]) for hour in range(4, 24)]
    return sorted([(*day, *time) for day, time in product(days, times)])
