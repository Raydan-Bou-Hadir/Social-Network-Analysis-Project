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
    
    def removeUserWidgets(self):
        tk.Label(self.root, text="Remove User").pack(pady=10)

        remove_user_frame = tk.Frame(self.root)
        remove_user_frame.pack(pady=5)

        self.remove_user_id_entry = tk.Entry(remove_user_frame)
        self.remove_user_id_entry.grid(row=0, column=0)
        tk.Label(remove_user_frame, text="User ID").grid(row=0, column=1)

        self.remove_user_button = tk.Button(self.root, text="Submit", command=self.removeUser)
        self.remove_user_button.pack(pady=5)

    def addRelationshipWidgets(self):
        tk.Label(self.root, text="Add Relationship").pack(pady=10)

        add_relationship_frame = tk.Frame(self.root)
        add_relationship_frame.pack(pady=5)

        self.user_id1_entry = tk.Entry(add_relationship_frame)
        self.user_id1_entry.grid(row=0, column=0)
        tk.Label(add_relationship_frame, text="User ID 1").grid(row=0, column=1)

        self.user_id2_entry = tk.Entry(add_relationship_frame)
        self.user_id2_entry.grid(row=1, column=0)
        tk.Label(add_relationship_frame, text="User ID 2").grid(row=1, column=1)

        self.add_relationship_button = tk.Button(self.root, text="Submit", command=self.addRelationship)
        self.add_relationship_button.pack(pady=5)
    
    def removeRelationshipWidgets(self):
        tk.Label(self.root, text="Remove Relationship").pack(pady=10)

        remove_relationship_frame = tk.Frame(self.root)
        remove_relationship_frame.pack(pady=5)

        self.remove_user_id1_entry = tk.Entry(remove_relationship_frame)
        self.remove_user_id1_entry.grid(row=0, column=0)
        tk.Label(remove_relationship_frame, text="User ID 1").grid(row=0, column=1)

        self.remove_user_id2_entry = tk.Entry(remove_relationship_frame)
        self.remove_user_id2_entry.grid(row=1, column=0)
        tk.Label(remove_relationship_frame, text="User ID 2").grid(row=1, column=1)

        self.remove_relationship_button = tk.Button(self.root, text="Submit", command=self.removeRelationship)
        self.remove_relationship_button.pack(pady=5)
    
    def viewUserDetailsWidget(self):
        tk.Button(self.root, text="View User Details", command=self.searchUserById).pack(pady=10)
    
    def sortUsersByNameWidget(self):
        tk.Button(self.root, text="Sort Users by Name", command=self.sortUsersByName).pack(pady=10)

    def searchUserByIdWidget(self):
        tk.Button(self.root, text="Search User by ID", command=self.searchUserById).pack(pady=10)

    # def searchUserByNameWidget(self):
    #     tk.Button(self.root, text="Search User by Name", command=self.searchUserByName).pack(pady=10)

    def visualizeGraphWidget(self):
        tk.Button(self.root, text="Visualize Graph", command=self.visualize).pack(pady=10)

    def exitButton(self):
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def addUser(self):
        userId = self.user_id_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_entry.get()
        if userId and name and email and age:
            try:
                age = int(age)
                if self.graph.addUser(userId, name, email, age):
                    messagebox.showinfo("Success", "User added successfully.")
                else:
                    messagebox.showwarning("Warning", "User ID already exists.")
            except ValueError:
                messagebox.showwarning("Warning", "Age must be an integer.")
        else:
            messagebox.showwarning("Warning", "All fields must be filled.")

    def removeUser(self):
        userId = self.remove_user_id_entry.get()
        if userId:
            if self.graph.removeUser(userId):
                messagebox.showinfo("Success", "User removed successfully.")
            else:
                messagebox.showwarning("Warning", "User not found.")

    def addRelationship(self):
        userId1 = self.user_id1_entry.get()
        userId2 = self.user_id2_entry.get()
        if userId1 and userId2:
            if self.graph.addRelationship(userId1, userId2):
                messagebox.showinfo("Success", "Relationship added successfully.")
            else:
                messagebox.showwarning("Warning", "One or both users not found.")
