import collections
import glob
import sqlite3

import yaml


def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def generate_schema(table_name, column_names):
    columns = ', '.join(['"{}" TEXT'.format(column_name) for column_name in column_names])
    return f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns})'


def insert_metadata(connection, table_name, metadata):
    question_marks = ", ".join(["?" for i in range(len(metadata))])
    column_names = ', '.join('"%s"' % _ for _ in metadata.keys())
    values = tuple(metadata.values())
    connection.execute(
        f'INSERT INTO {table_name} ({column_names}) VALUES ({question_marks})',
        values)


def generate_database(filename, sections, skipped_keys):
    """Generate sqlite database from yaml metadata files

    Args
    ====
    filename: str
      sqlite database filename
    sections: set
      set of directories to parse for *.yml files and flatten into sqlite tables
    skipped_keys: set
      dictionary of keys in metadata files to skip (mainly a hack to handle tags and groups
    """
    connection = sqlite3.connect(filename)

    with connection:
        for section in sections:
            keys = set()
            for filename in glob.glob(f'{section}/*.yml'):
                with open(filename) as f:
                    metadata = yaml.safe_load(f)
                    keys = keys | flatten(metadata).keys()

            section_schema = generate_schema(section, keys)
            connection.execute(section_schema)

            for filename in glob.glob(f'{section}/*.yml'):
                with open(filename) as f:
                    metadata = yaml.safe_load(f)
                    for key in skipped_keys.get(section, set()):
                        if key in metadata:
                            del metadata[key]
                try:
                    insert_metadata(connection, section, flatten(metadata))
                except:
                    print('failed to insert', filename)


def main():
    sections = {
        'bloggers', 'conferences', 'coworking_spaces',
        'event_spaces', 'groups', 'organizations', 'organizers'
    }

    # for now we skip lists this will require a many to many
    # relationship table
    skipped_keys = {
        'groups': {'tags'},
        'organizers': {'group'},
    }

    generate_database('db.sqlite', sections, skipped_keys)


if __name__ == "__main__":
    main()
