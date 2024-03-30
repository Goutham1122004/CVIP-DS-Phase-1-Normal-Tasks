import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_name):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file_name)
    return pd.read_csv(file_path)

def explore_data(data):
    print(data.info())
    print(data.head())
    print(data.describe())
    print(data.isnull().sum())
    
def visualize_transaction_distribution(data):
    plt.figure(figsize=(12, 6))
    sns.countplot(x='GRP', data=data)
    plt.title('Transaction Distribution by Category')
    plt.xlabel('Category')
    plt.ylabel('Transaction Count')
    plt.xticks(rotation=45)
    plt.show()

def visualize_transaction_by_store(data):
    plt.figure(figsize=(12, 6))
    sns.countplot(x='STORECODE', data=data)
    plt.title('Transaction Distribution by Store')
    plt.xlabel('Store')
    plt.ylabel('Transaction Count')
    plt.show()

def visualize_transaction_by_month(data):
    plt.figure(figsize=(12, 6))
    sns.countplot(x='MONTH', data=data)
    plt.title('Transaction Distribution by Month')
    plt.xlabel('Month')
    plt.ylabel('Transaction Count')
    plt.show()

if __name__ == "__main__":
    file_name = 'D:/Internship_Tasks/Coders_Cave_Task/Phase 1/Transaction data - Task 1/dataset/Hackathon_Validation_Data.csv'  # Assuming the CSV file is in the same directory as the Python script
    transaction_data = load_data(file_name)
    explore_data(transaction_data)
    visualize_transaction_distribution(transaction_data)
    visualize_transaction_by_store(transaction_data)
    visualize_transaction_by_month(transaction_data)
