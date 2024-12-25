participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(first_group, second_group):
    first = first_group.split('|')
    second = second_group.split('|')
    first_set = set(first)
    common = first_set.intersection(second)
    common = list(common)
    common.sort()
    return common
result = find_common_participants(participants_first_group, participants_second_group)
print(result)
