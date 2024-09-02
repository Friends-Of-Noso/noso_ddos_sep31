#!/bin/bash

max_parallel=6
count=100000


# Функція для надсилання запитів

  for i in $(seq 1 $count); do
    dart run bag.dart &
  # python3 atack_massive.py & 

    # Якщо кількість активних процесів досягає максимального значення, чекаємо, поки один з них завершиться
    while [ "$(jobs -r | wc -l)" -ge "$max_parallel" ]; do
      sleep 0.1
    done
  done


# Чекаємо на завершення всіх фонових процесів
wait
