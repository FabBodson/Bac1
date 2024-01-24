import os


def collect_files_with_extension(directory, extensions):
    for root, _, files in os.walk(directory):
        for file in files:
            filename, extension = os.path.splitext(file)
            if extension in extensions:
                yield {
                    'path': f'{root}/{file}',
                    'name': filename,
                    'extension': extension
                }
