def create_character(name, strength, perception, endurance, charisma, intelligence, luck):
    if not isinstance(name, str):
        return "The character name should be a string"

    if len(name) == 0:
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    stats = [strength, perception, endurance, charisma, intelligence, luck]

    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"

    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"

    if sum(stats) != 20:
        return "The character should start with 20 points"

    full_dot = '●'
    empty_dot = '○'

    str_bar = full_dot * strength + empty_dot * (10 - strength)
    per_bar = full_dot * perception + empty_dot * (10 - perception)
    end_bar = full_dot * endurance + empty_dot * (10 - endurance)
    cha_bar = full_dot * charisma + empty_dot * (10 - charisma)
    int_bar = full_dot * intelligence + empty_dot * (10 - intelligence)
    luc_bar = full_dot * luck + empty_dot * (10 - luck)

    result = (
        f"{name}\n"
        f"STR {str_bar}\n"
        f"PER {per_bar}\n"
        f"END {end_bar}\n"
        f"CHA {cha_bar}\n"
        f"INT {int_bar}\n"
        f"LUC {luc_bar}\n"
    )

    return result


print(create_character('Jaime', 3, 2, 1, 6, 5, 3))
