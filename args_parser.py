import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--register", help="register new user", nargs='*')
parser.add_argument("--login", help="login user", nargs='*')
parser.add_argument("--get_appoinments_times", help="get appoinments times", nargs='*')
parser.add_argument("--set_appoinment", help="set appoinment", nargs='*')
parser.add_argument("--send_email", help="send confirmation", nargs='*')
parser.add_argument("--send_reminder", help="send reminder", nargs='*')
