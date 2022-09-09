#!/usr/bin/env bash

# Generate the resume html
yaml-resume export swe.yaml -t simple -e html
# Convert the html resume to a pdf
weasyprint resume.html resume.pdf
