import os

if __name__ == '__main__':
    '''Main entry point for the application.'''
    _location = os.path.dirname(__file__)
    main_path = '{0}/splash.py'.format(_location)
    os.system('python "{0}"'.format(main_path))


    