#!/usr/bin/env bash

cd backend\src
gunicorn src.wsgi:application