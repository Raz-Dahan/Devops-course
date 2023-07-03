#!/usr/bin/bash


while read user;
do
  sudo userdel -r $user
done < usernames_file

echo 'Users have been deleted!'

