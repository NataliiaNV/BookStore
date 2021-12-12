from setuptools import setup, find_packages

setup(
    name='BooksStore',
    version='1.0.0',
    author='Nataliia Kaptur',
    author_email='vasylivna.nv@gmail.com',
    description='Web application for a bookstore',
    url='https://github.com/NataliiaNV/BookStore.git',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==2.0.2',
        'Flask-Migrate==3.1.0',
        'Flask-SQLAlchemy==2.5.1',
        'Flask-WTF==1.0.0',
        'mysql-connector-python==8.0.27',
        'WTForms==3.0.0',
        'PyMySQL==1.0.2'
    ]
)
