#!/bin/bash

mariadb_ready() {
  python <<END
import sys
import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="${DB_HOST}",
        user="${DB_USER}",
        password="${DB_PASSWORD}",
        port="${DB_PORT}"
    )
except mysql.connector.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}
