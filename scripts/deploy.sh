#!/bin/bash
set -e
helm upgrade --install ci-cd-demo ./helm/chart -n default
