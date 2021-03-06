import os
import pickle
import torch.optim as optim

import config


def create_folders():
    if not os.path.exists('checkpoints'):
        os.makedirs('checkpoints')
    if not os.path.exists('checkpoints/' + 'models'):
        os.makedirs('checkpoints/' + 'models')
    if not os.path.exists('checkpoints/' + 'records'):
        os.makedirs('checkpoints/' + 'records')

def save_history(history):
    print("Saving history...")
    pickle.dump(history,
                open("checkpoints/records/history.p", "wb"))

    pickle.dump(history,
                open("checkpoints/records/history_backup.p", "wb"))

def load_history():
    print("Loading History...")
    try:
        history = pickle.load(open("checkpoints/records/history.p", "rb"))
        print("Successfully loaded history.")
    except FileNotFoundError:
        print("Loss history not found, starting new history.")

        history = []

    return history

def load_memories():
    print("Loading memories...")
    try:
        memories = pickle.load(
            open("checkpoints/records/memories.p", "rb"))
        print("Number of memories: " + str(len(memories)))
    except FileNotFoundError:
        print("Memories not found, making new memories.")
        memories = []

    return memories


def save_memories(memories):
    print("Saving memories...")
    pickle.dump(memories,
                open("checkpoints/records/memories.p", "wb"))

    pickle.dump(memories,
                open("checkpoints/records/memories_backup.p", "wb"))
