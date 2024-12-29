from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from schema import User
from schema import Entry

from typing import List

import streamlit as st
from dotenv import load_dotenv
import os


class DB:

    client: MongoClient = None
    db: Database = None
    userCollection: Collection = None
    entryCollection: Collection = None
    users: List[User] = []

    def __init__(self):
        load_dotenv()

        self.client = MongoClient(st.secrets["MONGO_URL"])
        self.db = self.client["MySpace"]

        self.userCollection = self.db["Users"]
        self.entryCollection = self.db["Entries"]

        self.users = [
            User(**{**user, "_id": str(user["_id"])})
            for user in self.userCollection.find()
        ]

    def create_new_user(self, user: User) -> dict:
        new_user_id = self.userCollection.insert_one(user.model_dump()).inserted_id
        inserted_user = self.userCollection.find_one({"_id": new_user_id})
        return User(**{**inserted_user, "_id": str(inserted_user["_id"])})

    def create_new_entry(self, entry: Entry) -> None:
        self.entryCollection.insert_one(entry.model_dump())

    def fetch_all_entries(self, username: str) -> List[Entry]:
        entries = self.entryCollection.find({"username": username}).sort(
            "created_at", -1
        )
        return [
            Entry(
                username=entry["username"],
                content=entry["content"],
                vibe=entry["vibe"],
                created_at=entry["created_at"],
            )
            for entry in entries
        ]
