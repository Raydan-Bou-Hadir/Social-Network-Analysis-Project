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
        self.visualizeGraphWidget()
        self.exitButton()