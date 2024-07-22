import GraphFile
import User
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import networkx as nx
import matplotlib.pyplot as plt

class SocialNetwork:
    def __init__(self, root):
        self.graph = GraphFile.Graph()
        self.root = root
        self.root.title("Social Network")

        # Create UI Elements
        self.createWidgets()

    def createWidgets(self):
        tk.Label(self.root, text="Social Network GUI", font=("Arial", 16)).pack(pady=10)

        self.addUserWidgets()
        self.removeUserWidgets()
        self.addRelationshipWidgets()
        self.removeRelationshipWidgets()
        self.viewUserDetailsWidget()
        self.sortUsersByNameWidget()
        self.searchUserByIdWidget()
        # self.searchUserByNameWidget()
        self.visualizeGraphWidget()
        self.exitButton()

    def addUserWidgets(self):
        tk.Label(self.root, text="Add User").pack(pady=10)

        user_frame = tk.Frame(self.root)
        user_frame.pack(pady=5)

        self.user_id_entry = tk.Entry(user_frame)
        self.user_id_entry.grid(row=0, column=0)
        tk.Label(user_frame, text="User ID").grid(row=0, column=1)

        self.name_entry = tk.Entry(user_frame)
        self.name_entry.grid(row=1, column=0)
        tk.Label(user_frame, text="Name").grid(row=1, column=1)

        self.email_entry = tk.Entry(user_frame)
        self.email_entry.grid(row=2, column=0)
        tk.Label(user_frame, text="Email").grid(row=2, column=1)

        self.age_entry = tk.Entry(user_frame)
        self.age_entry.grid(row=3, column=0)
        tk.Label(user_frame, text="Age").grid(row=3, column=1)

        self.add_user_button = tk.Button(self.root, text="Submit", command=self.addUser)
        self.add_user_button.pack(pady=5)