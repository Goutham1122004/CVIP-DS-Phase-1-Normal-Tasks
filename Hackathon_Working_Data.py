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

def visualize_amount_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['BILL_AMT'], bins=30, kde=True)
    plt.title('Distribution of Transaction Amounts')
    plt.xlabel('Amount')
    plt.ylabel('Frequency')
    plt.show()

def visualize_quantity_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['QTY'], bins=30, kde=True)
    plt.title('Distribution of Transaction Quantities')
    plt.xlabel('Quantity')
    plt.ylabel('Frequency')
    plt.show()

def visualize_amount_by_category(data):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='GRP', y='BILL_AMT', data=data)
    plt.title('Transaction Amounts by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.show()

def visualize_amount_by_brand(data):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='BRD', y='BILL_AMT', data=data)
    plt.title('Transaction Amounts by Brand')
    plt.xlabel('Brand')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.show()

def visualize_correlation_matrix(data):
    correlation_matrix = data.corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

if __name__ == "__main__":
    file_path = 'D:/Internship_Tasks/Coders_Cave_Task/Phase 1/Transaction data - Task 1/dataset/Hackathon_Working_Data.csv'
    transaction_data = load_data(file_path)

    explore_data(transaction_data)
    visualize_amount_distribution(transaction_data)
    visualize_quantity_distribution(transaction_data)
    visualize_amount_by_category(transaction_data)
    visualize_amount_by_brand(transaction_data)
    visualize_correlation_matrix(transaction_data)
