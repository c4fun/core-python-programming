__author__ = 'Richard'


class User:
    """User contains all the info for a person entering the chat room"""
    def __init__(self, account_name, password, name, age = 1, sex="unbound", location="unbound"):
        """At least input the account_name, password, name"""
        self.account_name = account_name
        self.password = password
        self.name = name
        self.age = age
        self.sex = sex
        self.location = location


class Message:
    def __init__(self, message = None, sender, recipient='@all'):
        """Contains the message for a user who wants to send"""
        self.message = message
        # sender should be a User class
        self.sender = sender
        self.recipient = recipient

    def input_message(self, message):
        message = input("Please input a message >")
        self.message = message


class Room():
    """Room class represents a more sophisticated chat system where
    users can create separate “rooms” within the chat area and
    invite others to join."""
    # 这里创建room可以是User的一个方法
    def __init__(self, room_name, room_password, owner):
        self.room_name = room_name
        self.room_password = room_password
        # owner should be a User class
        self.owner = owner

    def invite(self, recipient):
        # TODO The owner of the room can invite other User to join
        pass
