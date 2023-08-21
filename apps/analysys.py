import os
import streamlit as st


def app():

  st.title("トレーニング結果分析")

import matplotlib.pyplot as plt
import seaborn as sns

# Setting up the style and size of the plots
sns.set(style="whitegrid")
plt.figure(figsize=(18, 15))

# Creating subplots for H, S, V
for i, feature in enumerate(['H', 'S', 'V'], 1):
    plt.subplot(3, 1, i)
    
    # Boxplot for each feature by kwd for each year
    sns.boxplot(data=color_data_updated, x='Year', y=feature, hue='kwd', palette='Set3')
    
    # Title and labels
    plt.title(f'Distribution of {feature} by Keyword for Each Year')
    plt.ylabel(f'{feature} Value')
    if i != 3:  # Removing x label for the first two plots for better visualization
        plt.xlabel('')
    else:
        plt.xlabel('Year')
    plt.legend(loc='upper right', bbox_to_anchor=(1.12, 1.2), ncol=1)

plt.tight_layout()
plt.show()


