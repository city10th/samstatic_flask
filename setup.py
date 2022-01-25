from setuptools import setup, find_packages

def copy_github_files_to_package_doc(files:list):
    import os
    from shutil import copyfile
    def copy_it(file):
        this_filepath = os.path.abspath(__file__)
        this_filefold = os.path.dirname(this_filepath)
        os.makedirs(this_filefold, exist_ok=True)
        source_file = os.path.join(this_filefold, file)
        target_file = os.path.join(this_filefold, 'src', 'samstatic_flask', 'doc', file)
        try:
            print(f'coping {source_file} -> {target_file}')
            copyfile(source_file, target_file)
        except Exception as e:
            print(e)
    for file in files:
        copy_it(file)

setup_kwargs = dict(
    name="samstatic_flask",
    version="1.0.0",
    keywords=["samstatic_flask", "flask"],
    description="enable the same static url search multi folders",
    long_description="enable the same static url (e.g. /static) search multi folders (e.g. /static /upload)",
    license="MIT Licence",

    author="City10th",
    author_email="city10th@foxmail.com",
    url="https://github.com/city10th/samstatic_flask",

    package_dir={'': 'src'},
    package_data={'samstatic_flask': ['doc/*.md', 'doc/LICENSE']},
    packages=find_packages(where='src'),
    platforms="any",
    install_requires=['Flask >= 2.0.0'],
)

if __name__ == '__main__':
    copy_github_files_to_package_doc(['README.md', 'LICENSE'])
    setup(**setup_kwargs)
