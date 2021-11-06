#!/bin/bash
isExistApp=`pgrep gunicorn`
if [[ -n  $isExistApp ]]; then
    kill $isExistApp || true
fi