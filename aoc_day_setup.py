import unicodedata
import re
import aocd.models

import os
import shutil


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def create_folder(folder_path: str) -> bool:
    if os.path.exists(folder_path):
        user_input = input(
            f"The folder '{folder_path}' already exists. Do you want to overwrite it? (y/n) "
        ).lower()
        if user_input == "y" or user_input == "":
            shutil.rmtree(folder_path)
        else:
            return False
    os.makedirs(folder_path)
    return True


def read_file(file_path: str) -> str:
    with open(file_path, "r") as input_file:
        file_content = input_file.read()
    return file_content


def write_file(file_path: str, content: str):
    with open(file_path, "w") as output_file:
        output_file.write(content)


if __name__ == "__main__":
    year_day = input("Please enter the year_day string: ")
    year = int(year_day[:4])
    day = int(year_day[4:6])

    puzzle = aocd.models.Puzzle(year, day)
    example = puzzle.examples[0]

    title = puzzle.title
    safe_title = slugify(title)

    folder_name = f"{year_day} {safe_title}"
    folder_path = os.path.join(os.getcwd(), str(year), f"{year_day} {safe_title}")
    relative_path = "/".join([str(year), folder_name])

    utils_template_content = read_file("templates/template_utils.py")

    template_content = read_file("templates/template.py")
    template_content = template_content.replace("$relative_path", relative_path)
    part_1_content = template_content.replace("$part", "1")
    part_2_content = template_content.replace("$part", "2")

    test_template_content = read_file("templates/template_test.py")
    test_content = test_template_content.replace("$year_day", year_day)
    test_content = test_content.replace(
        "$test_1", str([(example.input_data, example.answer_a, example.extra)])
    )
    test_content = test_content.replace(
        "$test_2", str([(example.input_data, example.answer_a, example.extra)])
    )

    submit_template_content = read_file("templates/template_submit.py")
    submit_template_content = submit_template_content.replace("$year", str(year))
    submit_template_content = submit_template_content.replace("$day", str(day))
    part_1_submit_content = submit_template_content.replace("$n", "1")
    part_1_submit_content = part_1_submit_content.replace("$x", "a")
    part_2_submit_content = submit_template_content.replace("$n", "2")
    part_2_submit_content = part_2_submit_content.replace("$x", "b")

    if not create_folder(folder_path):
        exit(0)
    write_file("/".join([relative_path, "input.txt"]), puzzle.input_data)
    write_file("/".join([relative_path, "utils.py"]), utils_template_content)
    write_file("/".join([relative_path, "part_1.py"]), part_1_content)
    write_file("/".join([relative_path, "part_2.py"]), part_2_content)
    write_file("/".join([relative_path, f"aoc{year_day}_test.py"]), test_content)
    write_file("/".join([relative_path, "part_1_submit.py"]), part_1_submit_content)
    write_file("/".join([relative_path, "part_2_submit.py"]), part_2_submit_content)
