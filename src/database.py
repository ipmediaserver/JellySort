#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from pathlib import Path

DB_PATH = Path("database/jellysort.db")


class Database:

    def __init__(self):
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)

        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row

        self.create_tables()

    def create_tables(self):

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS files (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            path TEXT UNIQUE NOT NULL,

            filename TEXT NOT NULL,

            library TEXT NOT NULL,

            size INTEGER NOT NULL,

            mtime INTEGER NOT NULL,

            status TEXT DEFAULT 'new',

            tmdb_id INTEGER,

            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        self.conn.commit()

    def add_or_update(self, path, filename, library, size, mtime):

        self.conn.execute("""
        INSERT INTO files(path,filename,library,size,mtime)
        VALUES(?,?,?,?,?)

        ON CONFLICT(path)
        DO UPDATE SET

            size=excluded.size,
            mtime=excluded.mtime,
            updated_at=CURRENT_TIMESTAMP;
        """, (path, filename, library, size, mtime))

        self.conn.commit()

    def get_all(self):

        return self.conn.execute(
            "SELECT * FROM files"
        ).fetchall()

    def close(self):
        self.conn.close()
