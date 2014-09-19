#!/bin/bash
# ----------------------------------------
# OpenBazaar image update and build script
# ----------------------------------------

set -e

TARGET=/tmp/obgit
OB=/bazaar

if [ -f $TARGET/requirements.txt ]; then
   echo Dir $TARGET Exists.
   rm -rf  $OB
   cp -R $TARGET $OB
   #cd $OB/pysqlcipher && python setup.py install
   pip install -r $OB/requirements.txt
fi
# check $TARGET/.imgtesting
if [ -f $TARGET/.imgtesting ]; then
   sudo add-apt-repository -y ppa:chris-lea/node.js
   sudo apt-get update
   sudo apt-get install -y nodejs
   sudo npm install -g jslint jshint
   pip install -r $OB/test_requirements.txt
fi
