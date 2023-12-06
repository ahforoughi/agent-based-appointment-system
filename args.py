# import argparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--register", help="register new user", nargs='*',)
parser.add_argument("--login", help="login user", action="store_true")
parser.add_argument("--get_appoinments_times", help="get appoinments times", action="store_true")

args = parser.parse_args()

if args.register:
    print("Registering new user")

# define a variable to set the action of the agent based on the command line arguments
behavior = None
if args.register not in [False, True]:
    print(f"Registering new user with identifier: {args.register}")
    behavior = "register"
elif args.login:
    behavior = "login"
elif args.get_appoinments_times:
    behavior = "get_appoinments_times"


if args.register:
    print("Registering new user")
    username = args.register[1]
    print(username)
