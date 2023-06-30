from website import create_app

app = create_app()

"""
Add the line if __name__ == '__main__':
This keeps it from running on import and only runs the web server when we directly run the main.py file.
"""
if __name__ == '__main__':
    app.run(debug=True)
