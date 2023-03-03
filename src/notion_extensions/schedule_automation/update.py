from datetime import date
import json 

from notion_extensions.config import config, recipe
from notion_extensions.utils.date import (
    fix_date,
    fix_day,
    parse_key,
    get_times_from_recipe_agenda,
    unparse,
)
from notion_extensions.utils.notion import get_client
from notion_extensions.utils.pauses import minipause, pause
from notion_extensions.utils.selenium import (
    by_xpath,
    get_browser,
    get_get_xpath_function,
    get_click_function,
    get_escape_function,
)

notion = get_client(config.integration_token)
browser = get_browser(config)
browser.get(recipe.page_url)

click = get_click_function(browser, min_pause=0.7, max_pause=1.4)
escape = get_escape_function(browser, min_pause=0.7, max_pause=1.2)
get_xpath = get_get_xpath_function(recipe.xpaths.reminder_template)


def change_date_header(week, day):
    day_block_id = recipe.day_block_ids[unparse(week, day)]
    d = notion.blocks.retrieve(day_block_id)["toggle"]
    minipause()
    text = fix_day(week, day)
    d["rich_text"][0]["text"]["content"] = text
    d["rich_text"][0]["plain_text"] = text
    notion.blocks.update(day_block_id, toggle=d)
    minipause()


def change_date(week, day, hour, minute):
    id = recipe.time_block_ids[unparse(week, day, hour, minute)]
    minipause()
    new_to_do = notion.blocks.retrieve(id)["to_do"]
    d = new_to_do["rich_text"][0]["mention"]["date"]["start"]
    new_d = fix_date(d, week, day)
    new_to_do["rich_text"][0]["mention"]["date"]["start"] = new_d
    new_to_do["rich_text"][0]["plain_text"] = new_d
    minipause()
    u = notion.blocks.update(id, to_do=new_to_do)


def change_date_move_content(day, hour, minute): #TODO
    """Specifically for updating the weekend during the week."""
    assert day > 4

    id_week = recipe.time_block_ids[unparse(0, day, hour, minute)]
    id_plan = recipe.time_block_ids[unparse(-1, day, hour, minute)]

    d = notion.blocks.retrieve(id_week)["to_do"]

    to_do_week = {}
    to_do_week.update(json.loads(json.dumps(d)))
    to_do_plan = {}
    to_do_plan.update(json.loads(json.dumps(d)))

    old_date = to_do_week["rich_text"][0]["mention"]["date"]["start"]
    new_date_week = fix_date(old_date, 0, day)
    new_date_plan = fix_date(old_date, -1, day)
    # print("week", new_date_week)
    # print("plan", new_date_plan)
    # print("old", old_date)

    week_text = to_do_week["rich_text"][1]["text"]["content"]

    to_do_week["rich_text"][0]["mention"]["date"]["start"] = new_date_week
    to_do_week["rich_text"][0]["plain_text"] = new_date_week
    to_do_week["rich_text"][1]["text"]["content"] = " \n"
    to_do_week["rich_text"][1]["plain_text"] = " \n"

    to_do_plan["rich_text"][0]["mention"]["date"]["start"] = new_date_plan
    to_do_plan["rich_text"][0]["plain_text"] = new_date_plan
    to_do_plan["rich_text"][1]["text"]["content"] = week_text
    to_do_plan["rich_text"][1]["plain_text"] = week_text
    
    assert to_do_week != to_do_plan
    _ = notion.blocks.update(id_week, to_do=to_do_week)
    # print("WEEK =====================================================================")
    # print(json.dumps(to_do_week, indent=2))
    # print("-------------------------------------------------------------------------------")
    # print(json.dumps(_["to_do"], indent=2))
    # print()
    _ = notion.blocks.update(id_plan, to_do=to_do_plan)
    # print("PLAN =====================================================================")
    # print(json.dumps(to_do_plan, indent=2))
    # print("-------------------------------------------------------------------------------")
    # print(json.dumps(_["to_do"], indent=2))
    

    



def close_toggles():
    for key in recipe.xpaths.day_toggles.keys():
        week, day = parse_key(key)
        try:
            pause()
            browser.find_element(by_xpath, get_xpath(week, day, 8, 30))
            pause()
            click(recipe.xpaths.day_toggles[key])
        except:
            pass


def days_from_times(times: list):
    return list(set([t[:2] for t in times]))


def fix_reminder_menu():
    click(recipe.xpaths.buttons.remind)
    click(recipe.xpaths.buttons.five_minutes_before)

    click(recipe.xpaths.buttons.date_format_and_timezone)

    click(recipe.xpaths.buttons.date_format)
    click(recipe.xpaths.buttons.relative)

    click(recipe.xpaths.buttons.time_format)
    click(recipe.xpaths.buttons.twentyfour_hour)

    escape()
    escape()
    #click(recipe.xpaths.background)


def fix_manually_single(week, day, hour, minute):
    reminder_xpath = get_xpath(week, day, hour, minute)
    click(reminder_xpath)
    fix_reminder_menu()


def fix_manually_list(times):
    days = days_from_times(times)
    #print(days)
    for week, day in days:

        toggle_xpath = recipe.xpaths.day_toggles[unparse(week, day)]
        click(toggle_xpath)

        for _week, _day, hour, minute in times:
            if (week, day) == (_week, _day):
                fix_manually_single(week, day, hour, minute)

        click(toggle_xpath)


# def main():
#     close_toggles()
#     times = get_times_from_recipe_agenda(recipe.agenda)
#     for week, day in days_from_times(times):
#         change_date_header(week, day)
#     for week, day, hour, minute in times:
#         change_date(week, day, hour, minute)
#     fix_manually_list(times)
#     browser.close()


def update_during_planning(): #TODO
    if not recipe.agenda.days:
        recipe.agenda.days = ["mon", "tue", "wed", "thu"]
    close_toggles()
    times = get_times_from_recipe_agenda(recipe.agenda)
    for week, day in days_from_times(times):
        change_date_header(week, day)
        print(f"Changed header ({week}) {day}")
    for week, day, hour, minute in times:
        change_date(week, day, hour, minute)
        print(f"Changed date ({week}) {day} {hour:02d}:{minute:02d}")
    fix_manually_list(times)
    browser.close()
    


def update_during_week(): #TODO
    if not recipe.agenda.days:
        recipe.agenda.days = ["fri0", "sat0", "sun0", "fri", "sat", "sun"]
    print(list(recipe.agenda.days))
    print(recipe.agenda.times)
    close_toggles()
    times = get_times_from_recipe_agenda(recipe.agenda)
    for week, day in days_from_times(times):
        change_date_header(week, day)
    for week, day, hour, minute in times:
        if not week and day > 4:
            change_date_move_content(day, hour, minute)
    fix_manually_list(times)
    browser.close()


def main():
    if date.today().isoweekday() > 4:
        update_during_planning()
    else:
        update_during_week()
        

if __name__ == "__main__":
    main()
