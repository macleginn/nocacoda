import os.path
from glob import glob
import pandas as pd

data_dir = 'data'
lang_files = sorted(glob(os.path.join('..', data_dir, '*_data.csv')))
marker_files = sorted(glob(os.path.join('..', data_dir, '*_markers.csv')))

# Файлов для языков должно быть столько же, сколько файлов для маркеров
assert len(lang_files) == len(
    marker_files), "Количество файлов для языков и маркеров не совпадает"

# Наборы полей (столбцов) во всех файлах типа languagename_data должны быть идентичны
lang_field_reference = []
for i, lang_file in enumerate(lang_files):
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    lang_fields = lang_df.columns.tolist()
    if i == 0:
        lang_field_reference = lang_fields
    else:
        if lang_field_reference != lang_fields:
            print(
                f"Наборы полей (столбцов) в языковых файлах не совпадают: {lang_file} и {lang_files[0]}")

# Наборы полей (столбцов) во всех файлах типа languagename_markers должны быть идентичны
marker_field_reference = []
for i, marker_file in enumerate(marker_files):
    marker_df = pd.read_csv(marker_file, sep='\t', encoding='utf-8')
    marker_fields = marker_df.columns.tolist()
    if i == 0:
        marker_field_reference = marker_fields
    else:
        if marker_field_reference != marker_fields:
            print(
                f"Наборы полей (столбцов) в файлах с маркерами не совпадают: {marker_file} и {marker_files[0]}")

sentences = pd.read_csv(os.path.join(
    '..', data_dir, '03_sentences.csv'), sep='\t')
languages = pd.read_csv(os.path.join(
    '..', data_dir, '01_languages.csv'), sep='\t')

# В файлах типа languagename_data в столбце “stimulus_no” всегда стоит какое-то целое число в интервале от 1 до 54
for lang_file in lang_files:
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    for stimulus_no in lang_df.stimulus_no:
        if stimulus_no not in range(1, 55):
            print(
                f"В файле {lang_file} неверное занчение в столбце stimulus_no: {stimulus_no} (должно быть целое число в интервале от 1 до 54)")

# В файлах типа languagename_data в столбце “status” всегда либо main, либо alternate
for lang_file in lang_files:
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    for status in lang_df.status:
        if status not in {'main', 'alternate'}:
            print(
                f"В файле {lang_file} неверное занчение в столбце status: {status} (должно быть main или alternate)")

# В файлах типа languagename_data на каждую пару language_no & stimulus_no должна быть ровно одна строка, где status = “main”
for lang_file in lang_files:
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    for stimulus_nos in lang_df.stimulus_no.unique():
        lang_df_subset = lang_df[lang_df.stimulus_no == stimulus_nos]
        if lang_df_subset.status.value_counts()['main'] != 1:
            print(
                f"В файле {lang_file} стимул {stimulus_nos} имеет больше или меньше одной строки с status = main")

# В файлах типа languagename_data в каждой строке в столбце “causal marker” должно что-то быть
for lang_file in lang_files:
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    for i, causal_marker in enumerate(lang_df.causal_marker):
        if causal_marker == '' or pd.isnull(causal_marker):
            print(
                f"В файле {lang_file} нет заполнения в столбце causal_marker в строке {i + 1}")

# В файлах типа languagename_data, если в них есть больше одной строки с одинаковой парой language_no & stimulus_no,
# то во всех этих строках должны быть разные записи в столбце “causal marker” (исключение: запись “n.a.”)
for lang_file in lang_files:
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    for stimulus_nos in lang_df.stimulus_no.unique():
        lang_df_subset = lang_df[lang_df.stimulus_no == stimulus_nos]
        vcs = lang_df_subset.causal_marker.value_counts()
        for k, v in vcs.items():
            if k != 'n.a.' and v > 1:
                print(
                    f"В файле {lang_file} в столбце causal_marker в строках с stimulus_no = {stimulus_nos} имеется повторяющееся значение: {k}")

# В файлах типа languagename_data в каждой строке, где в столбце “sentence” ничего нет, в столбце “causal marker” должно стоять “n.a.”
for lang_file in lang_files:
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    for sentence, causal_marker in zip(lang_df.sentence, lang_df.causal_marker):
        if sentence == '' or pd.isnull(sentence):
            if causal_marker != 'n.a.':
                print(
                    f"В файле {lang_file} в столбце causal_marker в строке с sentence = '' имеется неправильное значение: {causal_marker}")

# В файлах типа languagename_data в каждой строке, где в столбце “causal marker” стоит “n.a.”,
# в столбце “comments” должно быть что-то написано
for lang_file in lang_files:
    # TODO: remove
    break
    # TODO: ends
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    for comment, causal_marker in zip(lang_df.comments, lang_df.causal_marker):
        if causal_marker == 'n.a.' and comment == '' or pd.isnull(comment):
            print(
                f"В файле {lang_file} в столбце в строке с causal_marker = 'n.a.' нет комментария.")

# В файлах типа languagename_data если в столбце causal_marker стоит что-то, кроме n.a.,
# то в этой строке должно что-то быть в столбцах “sentence”, “glosses_en” и “back_translation”;
# исключение: если в столбце “language_name” стоит “English”, в столбце “glosses_en” может ничего не быть.
for lang_file in lang_files:
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    try:
        for row in lang_df.itertuples():
            if row.causal_marker != 'n.a.':
                if row.sentence == '' or pd.isnull(row.sentence):
                    print(
                        f"В файле {lang_file} в столбце sentence в строке с causal_marker = {row.causal_marker} нет текста.")
                if row.language_name != 'English' and (row.glosses_en == '' or pd.isnull(row.glosses_en)):
                    print(
                        f"В файле {lang_file} в столбце glosses_en в строке с causal_marker = {row.causal_marker} нет текста.")
                if row.back_translation_en == '' or pd.isnull(row.back_translation_en):
                    print(
                        f"В файле {lang_file} в столбце back_translation в строке с causal_marker = {row.causal_marker} нет текста.")
    except AttributeError as e:
        print(f"Ошибка {e} в файле {lang_file}.")

# В файлах типа languagename_data, если в столбце causal_marker стоит что-то, кроме n.a.,
# то в аналогичной паре “language_name” и “ causal_marker” должна соответствовать ровно одна строка
# (не больше и не меньше) в соответствующем файле languagename_markers
for lang_file, marker_file in zip(lang_files, marker_files):
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    marker_df = pd.read_csv(marker_file, sep='\t', encoding='utf-8')
    all_markers = set(marker_df.causal_marker.unique())
    for row in lang_df.itertuples():
        if row.causal_marker != 'n.a.':
            if row.causal_marker not in all_markers:
                print(
                    f"В файле {lang_file} есть causal_marker {row.causal_marker}, которого нет в файле {marker_file}")
                break
            if len(marker_df[marker_df.causal_marker == row.causal_marker]) != 1:
                print(
                    f"В файле {lang_file} есть causal_marker {row.causal_marker}, который встречается больше одного раза в {marker_file}")
                break

# Каждой записи в столбце “causal_marker” в файлах типа languagename_markers должен соответствовать
# как минимум один пример в соответствующем файле типа languagename_data
for lang_file, marker_file in zip(lang_files, marker_files):
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    marker_counts = lang_df.causal_marker.value_counts().to_dict()
    marker_df = pd.read_csv(marker_file, sep='\t', encoding='utf-8')
    for marker in marker_df.causal_marker.unique():
        if marker not in marker_counts:
            print(
                f"В файле {marker_file} есть causal_marker {marker}, которого нет в файле {lang_file}.")
            break

# В файлах типа languagename_data, если запись в поле “comments” начинается со слов “This translation is not included…”,
# то в поле “causal_marker” должно быть “n.a.”
for lang_file in lang_files:
    lang_df = pd.read_csv(lang_file, sep='\t', encoding='utf-8')
    for row in lang_df.itertuples():
        if not pd.isnull(row.comments) and row.comments.startswith('This translation is not included'):
            if row.causal_marker != 'n.a.':
                print(
                    f"В файле {lang_file} в столбце comments начинается со слов 'This translation is not included', но в столбце causal_marker не стоит 'n.a.'.")
                break

# В файлах типа languagename_markers в столбце “morphosyntactic_type” допустимы только значения affix и adposition
for marker_file in marker_files:
    marker_df = pd.read_csv(marker_file, sep='\t', encoding='utf-8')
    for row in marker_df.itertuples():
        if row.morphosyntactic_type not in ['affix', 'adposition']:
            print(
                f"В файле {marker_file} в столбце morphosyntactic_type допустимы только значения affix и adposition.")
            break

# В файлах типа languagename_markers в столбце “explicitness”, “goal”, “instrument”, “location”, “object”,
# “source”, “other” допустимы только значения yes и no
for marker_file in marker_files:
    marker_df = pd.read_csv(marker_file, sep='\t', encoding='utf-8')
    for row in marker_df.itertuples():
        if row.explicitness not in ['yes', 'no']:
            print(
                f"В файле {marker_file} в столбце explicitness допустимы только значения yes и no.")
            break
        if row.goal not in ['yes', 'no']:
            print(
                f"В файле {marker_file} в столбце goal допустимы только значения yes и no.")
            break
        if row.instrument not in ['yes', 'no']:
            print(
                f"В файле {marker_file} в столбце instrument допустимы только значения yes и no.")
            break
        if row.location not in ['yes', 'no']:
            print(
                f"В файле {marker_file} в столбце location допустимы только значения yes и no.")
            break
        if row.object not in ['yes', 'no']:
            print(
                f"В файле {marker_file} в столбце object допустимы только значения yes и no.")
            break
        if row.source not in ['yes', 'no']:
            print(
                f"В файле {marker_file} в столбце source допустимы только значения yes и no.")

# Если в файле типа languagename_markers тот или иной маркер помечен “no” во столбцах “goal”,
# “instrument”, “location”, “object” и “source”,
# то в столбце “other” он должен иметь либо “yes”, либо “no”

# Если в файле типа languagename_markers тот или иной маркер помечен “yes” хотя бы в одном из столбцов “goal”,
# “instrument”, “location”, “object” и “source”, то в столбце “other” он должен иметь либо “n.a.”

# Если в файле типа languagename_markers тот или иной маркер помечен “yes” в столбце “other”,
# то в столбце “other_details” должно быть что-то написано
for marker_file in marker_files:
    marker_df = pd.read_csv(marker_file, sep='\t', encoding='utf-8')
    for row in marker_df.itertuples():
        if row.other == 'yes' and (row.other_details == '' or pd.isnull(row.other_details)):
            print(
                f"В файле {marker_file} в столбце other_details должно быть что-то написано, если в столбце other стоит yes.")
            break
