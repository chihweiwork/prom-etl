#!/bin/bash

WORKDIR=$(dirname $0)

stime=$1
etime=$2

${WORKDIR}/monitor/prom-tool/promtool tsdb dump \
    --min-time=${stime}000 \
    --max-time=${etime}000 \
    $(grep "PrometheusDataPath" ${WORKDIR}/config/setup.conf| awk -F'=' '{print $NF}') \
    | python3 ${WORKDIR}/main.py --output $3
