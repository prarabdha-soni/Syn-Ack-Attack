from distutils.core import setup

setup(
    name="Slowloris",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["slowloris=slowloris:main"]},
    version="0.2.1",
    description="Low bandwidth DoS tool. Slowloris rewrite in Python.",
    author="prarabdha soni",
    author_email="prarabdha21@gmail.com",
    url="https://github.com/prarabdha-soni/Syn-Ack-Attack",
    keywords=["dos", "http", "slowloris"],
    license="MIT",
)
