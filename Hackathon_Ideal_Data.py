import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    return pd.read_csv(file_path)

def explore_data(data):
    print(data.info())
    print(data.head())
    print(data.describe())
    print(data.isnull().sum())

def visualize_transaction_by_month(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='MONTH', data=data)
    plt.title('Transaction Distribution by Month')
    plt.xlabel('Month')
    plt.ylabel('Transaction Count')
    plt.show()

def visualize_transaction_by_store(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='STORECODE', data=data)
    plt.title('Transaction Distribution by Store Code')
    plt.xlabel('Store Code')
    plt.ylabel('Transaction Count')
    plt.show()

def visualize_transaction_by_category(data):
    plt.figure(figsize=(12, 8))
    sns.countplot(x='GRP', data=data)
    plt.title('Transaction Distribution by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Transaction Count')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    file_path = 'D:/Internship_Tasks/Coders_Cave_Task/Phase 1/Transaction data - Task 1/dataset/Hackathon_Ideal_Data.csv'
    transaction_data = load_data(file_path)

    explore_data(transaction_data)
    visualize_transaction_by_month(transaction_data)
    visualize_transaction_by_store(transaction_data)
    visualize_transaction_by_category(transaction_data)
