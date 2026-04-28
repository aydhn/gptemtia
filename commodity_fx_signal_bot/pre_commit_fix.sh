#!/bin/bash
black . || true
flake8 . || true
