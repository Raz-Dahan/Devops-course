#!/usr/bin/bash


password=Aa123456

while read user;
do
  echo "adding user $user to the system"
  sudo useradd -m -s /bin/bash $user
  echo "$user:$password" | chpasswd
done < usernames_file

echo 'Users have been added!'
cat /etc/passwd | grep user
