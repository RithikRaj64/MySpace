from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from schema import User
from schema import Thread
from schema import Whisper

from typing import List
from datetime import timedelta, datetime

import streamlit as st
from dotenv import load_dotenv


class DB:

    client: MongoClient = None
    db: Database = None
    userCollection: Collection = None
    entryCollection: Collection = None
    whisperCollection: Collection = None
    users: List[User] = []

    def __init__(self):
        load_dotenv()

        self.client = MongoClient(st.secrets["MONGO_URL"])
        self.db = self.client["MySpace"]

        self.userCollection = self.db["Users"]
        self.entryCollection = self.db["Entries"]
        self.whisperCollection = self.db["Whispers"]

        self.users = [
            User(**{**user, "_id": str(user["_id"])})
            for user in self.userCollection.find()
        ]

    def create_new_user(self, user: User) -> dict:
        new_user_id = self.userCollection.insert_one(user.model_dump()).inserted_id
        inserted_user = self.userCollection.find_one({"_id": new_user_id})
        return User(**{**inserted_user, "_id": str(inserted_user["_id"])})

    def create_new_entry(self, entry: Thread) -> None:
        entry.created_at = entry.created_at + timedelta(hours=5, minutes=30)
        self.entryCollection.insert_one(entry.model_dump())

    def fetch_all_entries(self, username: str) -> List[Thread]:
        entries = self.entryCollection.find({"username": username}).sort(
            "created_at", -1
        )
        return [
            Thread(
                username=entry["username"],
                content=entry["content"],
                vibe=entry["vibe"],
                created_at=entry["created_at"],
            )
            for entry in entries
        ]

    def delete_entry(self, entry: Thread) -> None:
        self.entryCollection.delete_one(
            {
                "username": entry.username,
                "content": entry.content,
                "vibe": entry.vibe,
                "created_at": entry.created_at,
            }
        )

    def create_new_whisper(self, whisper: Whisper) -> None:
        whisper_dict = whisper.model_dump()
        whisper_dict["created_at"] = datetime.now()
        self.whisperCollection.insert_one(whisper_dict)

    def fetch_all_whispers(self, username: str) -> List[Whisper]:
        whispers = self.whisperCollection.find({"username": username}).sort("created_at", -1)
        return [
            Whisper(
                username=whisper["username"],
                content=whisper["content"],
                topic=whisper["topic"],
            )
            for whisper in whispers
        ]