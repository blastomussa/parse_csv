#!/bin/bash
#Author: blastomussa
#Date: 6/15/2021

# paths
BOOKS="path/to/csv"
STUDENTS="path/to/csv"
REPLACE="path/to/csv"

while IFS=, read -r serial user; do

  while IFS=, read -r s_last s_first s_email LC_last LC_first LC_email LC_phone; do
    if [[ "$user" == "$s_email" ]]; then
      echo "$s_first,$s_last,$s_email,$LC_first,$LC_last,$LC_email,$LC_phone" >> "${REPLACE}"
    fi
  done <

done < "${BOOKS}"

exit 0
