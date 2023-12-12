def username_generator(first_name,last_name):
  if len(first_name) < 3:
    user_name = first_name + last_name[:4]
  if len(last_name) < 4:
    user_name = first_name[:3] + last_name
  else:
    user_name = first_name[:3] + last_name[:4]
  return user_name

def password_generator(user_name):
  password = ""
  for i in range(0,len(user_name)):
    password = user_name[-1] + user_name[:-1]
  return password
