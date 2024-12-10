#!/bin/bash
NAME="archivos_planos"
PATHHOME="/home/dev2/archivos_planos"
PATHDJANGO="$PATHHOME"
USER="dev2"
GROUP="dev2"
WORKERS=3
DJANGOWSGI="archivos_planos.wsgi"
IP=***.000.0000.000
PORT=0000
LEVEL="debug"
echo "Starting app $NAME"
cd $PATHDJANGO
source env/bin/activate
pip install -r > requirements.txt
exec gunicorn $DJANGOWSGI --bind=$IP:$PORT --workers=$WORKERS --user=$USER --group=$GROUP --log-level=$LEVEL