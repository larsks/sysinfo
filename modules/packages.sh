#!/bin/sh

rpm -qa --qf='package %{NAME} %{VERSION}\n' | sort

