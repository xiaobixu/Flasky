#!/bin/bash

export FLASK_APP=demo_app
export FLASK_PORT=8080

if [ ! -e instance/demo_app.sqlite]; then
    flask init-db
fi

flask run
