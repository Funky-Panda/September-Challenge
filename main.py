import inquirer


def createUserId():
  file = open("data.csv", "r+")
  userId = validateUserId()
  for line in file:
    if line.split(",")[0] == userId:
      print("You are already registerd!")
      return
  password, passwordStrength = validatePassword()
  print(f"Password set successfully. Password Status: {passwordStrength}")
  file.write(f"{userId},{password},{passwordStrength}\n")


def validateUserId():
  print("Your User Id must be at least 4 characters.")
  userId = ""
  while len(userId) < 4:
    userId = input("Please Enter a UserID: ")
  return userId


def validatePassword():
  print(
      "Please enter a password 8 characters, include upper and lower case and numbers and one special character."
  )
  passwordStatus = ""
  passwordStrength = 0
  password = ""
  while passwordStrength < 3 or len(password) < 7:
    passwordStrength = 0
    password = input("Password: ")
    has_length = len(password) > 7
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
      if char.isupper() and not has_upper:
        passwordStrength += 1
        has_upper = True
      if char.islower() and not has_lower:
        passwordStrength += 1
        has_lower = True
      if char.isdigit() and not has_digit:
        passwordStrength += 1
        has_digit = True
      if char.isalnum() and not has_special:
        passwordStrength += 1
        has_special = True

    if passwordStrength == 4 and has_length:
      passwordStatus = "great password"
    elif passwordStrength >= 3 and has_length:
      passwordStatus = "low score"
    else:
      print("please try again!")
  return password, passwordStatus


def changePassword():
  newPasswordStrength = ""
  checkUserId = input("Please enter your User Id: ")

  with open("data.csv", "r") as file:
    lines = file.readlines()

  found = False

  for i, line in enumerate(lines):
    UserId, oldPassword, oldPasswordStrength = line.strip().split(",")

    if checkUserId == UserId:
      newPassword, newPasswordStrength = validatePassword()
      lines[i] = f"{UserId},{newPassword},{newPasswordStrength}\n"
      found = True
      break

  if found:
    with open("data.csv", "w") as file:
      file.writelines(lines)
    print(
        f"Password updated successfully. Password Status: {newPasswordStrength}"
    )
  else:
    print("User not found.")


def displayUserIds():
  file = open("data.csv", "r+")
  for line in file:
    UserId = line.strip().split(",")[0]
    print(f"{UserId}")


options = [
    inquirer.List('options',
                  message="Choose an option",
                  choices=[
                      "1) Create a new User ID", "2) Change a password",
                      "3) Display all Users IDs", "4) Quit"
                  ])
]

answersOptions = inquirer.prompt(options)
if answersOptions is not None:
  selected_option = answersOptions['options']
  if selected_option == "1) Create a new User ID":
    createUserId()
  elif selected_option == "2) Change a password":
    changePassword()
  elif selected_option == "3) Display all Users IDs":
    displayUserIds()
  elif selected_option == "4) Quit":
    print("Exiting the program.")
